import requests
from SaitamaRobot import CASH_API_KEY, dispatcher
from telegram import Update, ParseMode
from telegram.ext import CallbackContext, CommandHandler, run_async
import logging
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import CommandHandler, InlineQueryHandler, ConversationHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode
from telegram.ext import Updater, CallbackQueryHandler, CallbackContext
import random
import time
from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)


ONE , TWO , THREE, FOUR , FIVE, *_ = range(1000)

BOTID = 1338281900
maingroup = -753748989
def ticket(update, context):
    cd = context.bot_data
    query = update.callback_query
    Chat = update.effective_chat
    if update.effective_chat.type != Chat.PRIVATE:
        update.message.reply_text('use this command in PM/DM')
        return -1
    user = update.effective_user.name
    cd['id'] = update.effective_user.id
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Please send your questions or inquiry in the next message, do not send 'Hi' or 'hello'</b>\n\n<i>Admins will get back to you very soon</i>",
                             parse_mode=ParseMode.HTML)
    return 0


def ticket2(update, context):
    cd = context.bot_data
    query = update.callback_query
    Chat = update.effective_chat
    if update.effective_chat.type != Chat.PRIVATE:
        return -1
    cd = context.chat_data
    cd['msgid'] = msgid = update.effective_message.message_id
    cd['fromid'] = fromid = update.effective_chat.id
    context.bot.forward_message(chat_id=maingroup, from_chat_id=fromid, message_id=msgid)


def isreply(msg):
  return msg.reply_to_message is not None

def reply(update, context):
    a = update.message.text.split()[1:]
    c= " ".join(a)
    b = update.effective_user.first_name
    if update.effective_chat.id != maingroup:
        return None
    try:
        id = update.message.reply_to_message.forward_from.id

    except AttributeError:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'this user has forward privacy turned on, unable to track user')
        return -1
    if isreply(update.message):
        print(update.message.reply_to_message.from_user.id)
        if update.message.reply_to_message.from_user.id == BOTID:
           context.bot.send_message(chat_id = id , text = f"{c}\n\n<i>Answered by :</i> {b}\n\n<code>want to continue conversation? create another /ticket</code>", parse_mode = ParseMode.HTML)

dispatcher.add_handler(CommandHandler("reply", reply))
dispatcher.add_handler(CommandHandler("ticket", ticket))
dispatcher.add_handler(MessageHandler(Filters.text, ticket2))
