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

list = []
caller = [163494588, 1610096351]

def opt_in(update , context):
  global list
  chatid = update.effective_chat.id
  user = update.effective_user.first_name
  users = update.effective_user.name
  
  d = {chatid:user}
  list.append(d)
  update.message.reply_text(f'{users} you have opt in : group id {chatid}!')
  

def opt_out(update , context):
  global list
  chatid = update.effective_chat.id
  user = update.effective_user.first_name
  users = update.effective_user.name
  
  list = [i for i in list if not i[chatid] == str(user)]
  
  update.message.reply_text(f'{users} you have opt out : group id {chatid}!')
  
  
def all(update , context):
  id = user = update.effective_user.id
  query = update.callback_query
  chatid = update.effective_chat.id
  if id not in caller:
    update.message.reply_text('Not authorised')
    return -1
  
  text = ''
  
  for i in list:
    text += i[chatid] + '\n'
    
  update.message.reply_text(f'Doragon summon you all : \n\n{text}')
    
  
 
dispatcher.add_handler(CommandHandler("opt_in", op_in))

dispatcher.add_handler(CommandHandler("opt_out", op_out))

dispatcher.add_handler(CommandHandler("all", all))




