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

def ticket(update, context):
    cd = context.chat_data
    query = update.callback_query
    Chat = update.effective_chat
    if update.effective_chat.type !=Chat.PRIVATE:
        update.message.reply_text('use this command in PM/DM')
        return -1
    print('enter phase1 ')
    user = update.effective_user.name
    cd['id'] = update.effective_user.id
    context.bot.send_message(chat_id = update.effective_chat.id, text = "<b>Please send your questions or inquiry in the next message</b>\n\n<i>Admins will get back to you very soon</i>", parse_mode = ParseMode.HTML)
    print('phase1 done')
    return TWO
  
def ticket2(update , context):
    query = update.callback_query
    cd = context.chat_data
    print('enter phase2')
    inquiry = update.message.text
    cd['msgid'] = msgid = update.effective_message.message_id
    cd['fromid'] = fromid = update.effective_chat.id
    context.bot.forward_message(chat_id = -753748989,from_chat_id=fromid,message_id=msgid)
    print('phase2 done')
    return ticket3(update , context)
  
def ticket3(update , context):
    cd = context.chat_data
    query = update.callback_query
    fromid = cd['fromid']
    print('enter phase3')
    answer = update.message.reply_text
    id = cd['id']
    context.bot.send_message(chat_id =fromid, text = answer)
    ConversationHandler.END
    
ticket_handler = ConversationHandler(
    entry_points=[CommandHandler('ticket', ticket)],
    states={
       ''' ONE:
            [
                CallbackQueryHandler(ticket3, pattern=".")
            ],'''
           TWO:
            [MessageHandler(Filters.text, ticket2)]
    },
    fallbacks=[]
)


dispatcher.add_handler(ticket_handler)
