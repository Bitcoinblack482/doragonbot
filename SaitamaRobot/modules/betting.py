from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
    CallbackQueryHandler,
)

from SaitamaRobot import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update, Message

ONE , TWO , THREE , FOUR , FIRST , SECOND,  *_ = range(50)

boss = [163494588, 1610096351]
c1 = []
c2 = []

def startbet(update , context):
  c1 = update.message.text.split()[1]
  c2 = update.message.text.split()[2]
  
  
    












START_HANDLER = CommandHandler('startbet', startbet)


