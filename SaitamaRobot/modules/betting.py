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
c = []
list = []
status = 0
fees1 = 0
fees2 = 0
total = 0
share1 = 0
share2 = 0

def startbet(update , context):
  global status 
  name = update.effective_user.name
  id = update.effective_user.id
  try:
   c1 = update.message.text.split()[1]
   c2 = update.message.text.split()[2]
  except IndexError:
    update.message.reply_text('Please provide 2 users to compete')
    return -1

  if id not in boss:
        update.message.reply_text('Not authorised')
        return -1
    
  c.append(c1)
  c.append(c2)
  status +=1
    
  update.message.reply_text(f'Bet event created between {c1} and {c2}')
    
def betboard(update , context):
    global list
    global c
    n = 0
    m = 0
    text1 = ''
    text2 = ''
    
    fees1 = total*0.02
    fees2 = total*0.15
    shares = total*0.83
    
    for i in list:
     print(len(c))
     if len(c)==0:
        update.message.reply_text('No competition going on right now')
        return -1
    try:
     update.message.reply_text(f'<b>Ongoing competitions\n\n</b>'
                              f'<b>{c[0]}</b>\nV.s.\n'
                              f'<b>{c[1]}</b>\n\n'
                              f'Total pot = {total}\n'
                              f'Middle man fees = {fees1}\n'
                              f'Winner pot = {fees2}\n'
                              f'Total pot for shares = {shares}\n', parse_mode = ParseMode.HTML)
    except IndexError:
      update.message.reply_text('No competition going on right now')
      return -1 
    
    
def bet(update , context):
    global status 
    # 1 is on and 2 is off
    cd = context.chat_data
    query = update.callback_query
    cd['name'] = name = update.effective_user.name
    id = update.effective_user.id
    
    if len(c)==0:
        update.message.reply_text('No competition going on right now')
        return -1
    
    if status ==2:
        update.message.reply_text('sorry , the registration is now closed, wait for next one')
        return -1
    
    try:
    
     cd['bet_on'] = bet_on = update.message.text.split()[1]
     if bet_on not in c:
        update.message.reply_text(f'currently you can bet on {c[0]}, or {c[1]}, write either one, correct spelling')
        return -1
     cd['amount'] = amount = update.message.text.split()[2]
    except IndexError:
     update.message.reply_text(f'use it like this /bet <bet on who> <amount>\n\n'
                              f'currently you can bet on {c[0]}, or {c[1]}')
     return -1
    
    keyboard = [[InlineKeyboardButton('Approve', callback_data='approve')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(f'You bet on {bet_on} with {amount} DOR\n\n <b>waiting for admin to check and approve</b>', parse_mode=ParseMode.HTML,
                            reply_markup=reply_markup)
    return ONE
    
def bet2(update , context):
    global list
    cd = context.chat_data
    query = update.callback_query
    
    bet_on = cd['bet_on']
    amount = cd['amount']
    name  = cd['name']
    
    
    if update.callback_query.from_user.id not in boss:
        query.answer('Not authroised')
        return None
    
    total += amount
    d = {'user':name, 'bet_on':bet_on, 'amount':amount}
    list.append(d)
    
    query.edit_message_text(f'<b>Your bet on {bet_on} with {amount} DOR has been approved</b>', parse_mode=ParseMode.HTML)
    return ConversationHandler.END


def register(update , context):
    global status
    # 1 is on and 2 is off
    
    id = update.effective_user.id
    if id not in boss:
        update.message.reply_text('Not authorised')
        return -1
    
    try: 
     signal = update.message.text.split()[1]
     if signal == 'on' and status ==1:
         update.message.reply_text('Registration is already on')
         return -1
     if signal == 'on' and status ==2:
         update.message.reply_text('Registration turned on')
         status -=1
         return -1
     if signal == 'off' and status ==1:
         update.message.reply_text('Registration is now off')
         status +=1
         return -1
     if signal == 'off' and status ==2:
         update.message.reply_text('Registration is already off')
         return -1
    except IndexError:
     update.message.reply_text('Please enter /register on \nor\n/register off')
     return -1
        
    


def mybet(update , context):
    global share1
    global share2
    cd = context.chat_data
    query = update.callback_query
    name = update.effective_user.name
    id = update.effective_user.id
    ratio = 0
    reward = 0
    
    for i in list:
     if i['bet_on'] == c[0]:
      share1 += i['amount']
     if i['bet_on'] == c[1]:
      share2 += i['amount']
    
    for i in list:
     if i['user'] == name:
      if i['bet_on'] == c[0]:
       ratio += i['amount']/share1
      if i['bet_on'] == c[1]:
       ratio += i['amount']/share2
    
    for i in list:
     if i['user'] == name:
      if i['bet_on'] == c[0]:
        reward +=share1*ratio
     if i['user'] == name:
      if i['bet_on'] == c[1]:
        reward +=share2*ratio
    
    
    text = ''
    
    for i in list:
        if i['user'] == name:
            text+= f'{name}\nYour bet amount :{i["amount"]}\nYou bet on {i["bet_on"]}\n\nExpected reward if i["bet_on"] win : {reward} DOR'
    if text == '': 
     update.message.reply_text('You dont have ongoing bet yet')
     return -1
    else:
     update.message.reply_text(text)
      
    
    

dispatcher.add_handler(CommandHandler("startbet", startbet))
BET_HANDLER = ConversationHandler(
        entry_points=[CommandHandler('bet', bet, pass_user_data=True)],
        states={
            ONE: [CallbackQueryHandler(bet2, pattern="approve", pass_user_data=True),]
        },
        fallbacks=[],
        allow_reentry=True,
        per_user=False
    )

dispatcher.add_handler(BET_HANDLER)
dispatcher.add_handler(CommandHandler("register", register))
dispatcher.add_handler(CommandHandler("mybet", mybet))
dispatcher.add_handler(CommandHandler("betboard", betboard))


