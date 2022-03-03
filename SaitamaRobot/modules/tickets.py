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
def ticket(update, context):
    cd = context.bot_data
    query = update.callback_query
    Chat = update.effective_chat
    if update.effective_chat.type != Chat.PRIVATE:
        update.message.reply_text('use this command in PM/DM')
        return -1
    print('enter phase1 ')
    user = update.effective_user.name
    cd['id'] = update.effective_user.id
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="<b>Please send your questions or inquiry in the next message</b>\n\n<i>Admins will get back to you very soon</i>",
                             parse_mode=ParseMode.HTML)
    print('phase1 done')
    return 0


def ticket2(update, context):
    cd = context.bot_data
    query = update.callback_query
    Chat = update.effective_chat
    if update.effective_chat.type != Chat.PRIVATE:
        return -1
    cd = context.chat_data
    print('enter phase2')
    cd['msgid'] = msgid = update.effective_message.message_id
    cd['fromid'] = fromid = update.effective_chat.id
    print(fromid)
    #context.bot.forward_message(chat_id=-1001507825630, from_chat_id=fromid, message_id=msgid)
    context.bot.forward_message(chat_id=-753748989, from_chat_id=fromid, message_id=msgid)
    print('phase2 done')
    #context.bot.send_message(chat_id=)
    return 1

def isreply(msg):
  return msg.reply_to_message is not None

def ticket3(update, context):
    cd = context.bot_data
    query = update.callback_query
    print('enter phase3')
    a =  update.message.text
    b = update.effective_user.first_name
    try:
       id = update.message.reply_to_message.forward_from.id

    except AttributeError:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'this user has forward privacy turned on, unable to track user')
        return -1
    if isreply(update.message):
        if update.message.reply_to_message.from_user.id == BOTID:
           context.bot.send_message(chat_id = id, text = f"{a}\n\n<i>Answered by :</i> {b}", parse_mode = ParseMode.HTML)


ticket_handler = ConversationHandler(
    entry_points = [CommandHandler("ticket", ticket)],
    states = {
        0: [MessageHandler(Filters.text, ticket2)],
        1:[MessageHandler(Filters.text,ticket3)]
    },

    fallbacks = [],
    allow_reentry = True,
    per_chat=False
)
dispatcher.add_handler(ticket_handler)
