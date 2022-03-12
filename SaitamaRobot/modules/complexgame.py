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


def game(update: Update, context: CallbackContext):
    cd = context.chat_data
    if not update.message.reply_to_message:
             update.message.reply_text('reply to someone')
             return -1
    if update.message.reply_to_message.from_user.id == 5210931684:
        update.message.reply_text('u cant play with bot')
        
    cd['fighter'] = name = update.effective_user.first_name
    cd['fighterid'] = fid = update.effective_user.id
    
    cd['round'] = 1
    cd['fromhp'] = 20
    cd['tohp'] = 20
    cd['tomana'] = 5
    cd['frommana'] = 5
    cd['tobuild'] = 0
    cd['frombuild'] = 0
   
    keyboard = [
        [
            InlineKeyboardButton("Play", callback_data=str('play')),
            InlineKeyboardButton("Rules", callback_data=str('rules'))]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    

    update.message.reply_text(f'*{name}* created a game\n\n'
                              f'*Game :* Pro version\n'
                              f'*Lives : 20 ❤️*', reply_markup = reply_markup , parse_mode = ParseMode.MARKDOWN_V2)
    return ONE
    
def rules(update: Update, context: CallbackContext):
    cd = context.chat_data
    f = cd['fighter']
    fid = cd['fighterid']
   
    query = update.callback_query
    query.answer('Play as if you are on the field, but simpler', show_alert = True)
    return None

def play(update: Update, context: CallbackContext):
    cd = context.chat_data
    query = update.callback_query
    
    cd['to_id'] = toid =update.callback_query.from_user.id
    cd['to_name'] = toname = update.callback_query.from_user.first_name
    print(toid)
    
    f = cd['fighter']
    fid = cd['fighterid']
    tid =cd['to_id']
    t =cd['to_name']
 
    if update.callback_query.from_user.id == fid:
        query.answer('Cannot accept own invitation', show_alert = True)
        print(f'callback userid is {update.callback_query.from_user.id} and fid is {fid}')
        return None

    keyboard = [
        [
            InlineKeyboardButton("🐉Carrier", callback_data=str('carrier')),
            InlineKeyboardButton("🦇SkyPatrols", callback_data=str('sky patrol')),
            InlineKeyboardButton("🛕Splashy Tower", callback_data=str('splashy tower'))
        ],
        [
            InlineKeyboardButton("🐲Doragon", callback_data=str('doragon')),
            InlineKeyboardButton("⏱ SKIP ", callback_data=str('skip'))
        ]        
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(
        text=f"_*Round : {cd['round']}*_\n\n"
             f"{f}❤ : {cd['fromhp']}\n🌀Mana : {cd['frommana']}\n🛕Splashy Tower : {cd['frombuild']}\n\n{t}❤ : {cd['tohp']}\n🌀Mana : {cd['tomana']}\n🛕Splashy Tower : {cd['tobuild']}\n\n"
             f"*{f}* make your decision\n", reply_markup=reply_markup,parse_mode = ParseMode.MARKDOWN_V2
    )
    return ONE

def first(update: Update, context: CallbackContext):
    cd = context.chat_data
    query = update.callback_query
    f = cd['fighter']
    t = cd['to_name']
    fid = cd['fighterid']
    tid = cd['to_id']


    keyboard = [
        [
            InlineKeyboardButton("🐉Carrier", callback_data=str('carrier')),
            InlineKeyboardButton("🦇SkyPatrols", callback_data=str('sky patrol')),
            InlineKeyboardButton("🛕Splashy Tower", callback_data=str('splashy tower'))
        ],
        [
            InlineKeyboardButton("🐲Doragon", callback_data=str('doragon')),
            InlineKeyboardButton("⏱ SKIP ", callback_data=str('skip'))
        ]        
    ]
    
    reply_markup2 = InlineKeyboardMarkup(keyboard)
    if update.callback_query.from_user.id != fid:
        query.answer('player 2 not ur turn')
        print(f'callback userid is {update.callback_query.from_user.id} and fid is {fid}')
        return None
    if update.callback_query.from_user.id == fid:
     if query.data == 'carrier' and cd['frommana'] <5:
       query.answer('Not enough mana', show_alert = True)
       return None
     if query.data == 'sky patrol' and cd['frommana'] <3:
       query.answer('Not enough mana', show_alert = True)
       return None
     if query.data == 'splashy tower' and cd['frommana'] <5:
       query.answer('Not enough mana', show_alert = True)
       return None
     if query.data == 'doragon' and cd['frommana'] <3:
       query.answer('Not enough mana', show_alert = True)
       return None
     else:
      query.edit_message_text(
        text=f"_*Round : {cd['round']}*_\n\n"
             f"{f}❤ : {cd['fromhp']}\n🌀Mana : {cd['frommana']}\n🛕Splashy Tower : {cd['frombuild']}\n\n{t}❤ : {cd['tohp']}\n🌀Mana : {cd['tomana']}\n🛕Splashy Tower : {cd['tobuild']}\n\n"
             f"*{t}* Make your decision\n", reply_markup=reply_markup2, parse_mode = ParseMode.MARKDOWN_V2
    )
    cd['round']+=1
    cd['frommana']+=2
    cd['choice1'] = query.data
    
    if tid == 163494588:
     context.bot.send_message(chat_id=163494588, text = f'{f} choose : {query.data}')
    if tid == 652962567:
     context.bot.send_message(chat_id=652962567, text=f'{f} choose : {query.data}')
    print('player 1 choose : '+str(cd['choice1'])+ ',id : ' + str(update.callback_query.from_user.id))
    print(query.data)
    return TWO

def res(update: Update, context: CallbackContext):
    cd = context.chat_data
    query = update.callback_query
    query.answer()
    if query.data == 'carrier' and cd['frommana'] <5:
       query.answer('Not enough mana', show_alert = True)
       return None
    if query.data == 'sky patrol' and cd['frommana'] <3:
       query.answer('Not enough mana', show_alert = True)
       return None
    if query.data == 'splashy tower' and cd['frommana'] <5:
       query.answer('Not enough mana', show_alert = True)
       return None
    if query.data == 'doragon' and cd['frommana'] <3:
       query.answer('Not enough mana', show_alert = True)
       return None
    
    cd['choice2'] = query.data
    cd['tomana']+=2
    f = cd['fighter']
    t = cd['to_name']
    fid = cd['fighterid']
    tid = cd['to_id']
    fchose = cd['choice1']
    tchose = cd['choice2']
    print('res1')
    keyboard = [
        [
            InlineKeyboardButton("🐉Carrier", callback_data=str('carrier')),
            InlineKeyboardButton("🦇SkyPatrols", callback_data=str('sky patrol')),
            InlineKeyboardButton("🛕Splashy Tower", callback_data=str('splashy tower'))
        ],
        [
            InlineKeyboardButton("🐲Doragon", callback_data=str('doragon')),
            InlineKeyboardButton("⏱ SKIP ", callback_data=str('skip'))
        ]        
    ]
    print(tid)
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query.from_user.id != tid:
        query.answer('player 2 not ur turn')
        return None
    choice = {
            "carrier": "🐉",
            "sky patrol": "🦇",
             "splashy tower": "🛕",
             "doragon": "🐲",
             "skip": "⏱"
                        }

    a = choice[cd['choice1']]
    b = choice[cd['choice2']]
    if update.callback_query.from_user.id != tid:
        query.answer('player 1 not ur turn')
        return None

    if cd['choice1'] == 'carrier' and cd['tobuild'] == 0 and cd['choice2'] != 'sky patrol':
       cd['frommana'] -=5
       cd['tohp']-=6
        
    if cd['choice2'] == 'carrier' and cd['frombuild'] == 0 and cd['choice1'] != 'sky patrol':
       cd['tomana'] -=5
       cd['fromhp']-=6
        
    if cd['choice1'] == 'carrier' and cd['tobuild'] >0 and cd['choice2'] != 'sky patrol':
       cd['frommana'] -=5    
       cd['tobuild'] ==0
    if cd['choice2'] == 'carrier' and cd['frombuild'] >0 and cd['choice1'] != 'sky patrol':
       cd['tomana'] -=5
       cd['frombuild'] == 0
        
    ###############################################################
    if cd['choice1'] == 'carrier' and cd['tobuild'] == 0 and cd['choice2'] == 'sky patrol':
       cd['frommana'] -=5
       cd['tomana'] -=3
       cd['fromhp'] -=1
       cd['tohp']-=4
        
    if cd['choice2'] == 'carrier' and cd['frombuild'] == 0 and cd['choice1'] == 'sky patrol':
       cd['tomana'] -=5
       cd['frommana'] -=3
       cd['tohp'] -=1
       cd['fromhp']-=4
        
    if cd['choice1'] == 'carrier' and cd['tobuild'] >0 and cd['choice2'] == 'sky patrol':
       cd['frommana'] -=5  
       cd['tomana'] -=4
       cd['fromhp'] -=1
       cd['tobuild'] == 0
        
    if cd['choice2'] == 'carrier' and cd['frombuild'] >0 and cd['choice1'] == 'sky patrol':
       cd['tomana'] -=5  
       cd['frommana'] -=4
       cd['tohp'] -=1
       cd['frombuild'] == 0
        
     ###############################################################
    if cd['choice1'] == 'doragon' and cd['tobuild'] == 0:
       cd['frommana'] -=3
       cd['tohp']-=3
        
    if cd['choice2'] == 'doragon' and cd['frombuild'] == 0:
       cd['tomana'] -=3
       cd['fromhp']-=3
        
    if cd['choice1'] == 'doragon' and cd['tobuild'] >0:
       cd['frommana'] -=5    
       cd['tobuild'] == 0 
        
    if cd['choice2'] == 'doragon' and cd['frombuild'] >0:
       cd['tomana'] -=5
       cd['frombuild'] == 0

    ###############################################################
    if cd['choice1'] == 'sky patrol' and cd['tobuild'] == 0:
       cd['frommana'] -=3
       cd['tohp']-=2
        
    if cd['choice2'] == 'sky patrol' and cd['frombuild'] == 0:
       cd['tomana'] -=3
       cd['fromhp']-=2
        
    if cd['choice1'] == 'sky patrol' and cd['tobuild'] >0:
       cd['frommana'] -=5    
       cd['tobuild'] == 0 
        
    if cd['choice2'] == 'sky patrol' and cd['frombuild'] >0:
       cd['tomana'] -=5
       cd['frombuild'] == 0
     
    ###############################################################
    if cd['choice1'] == 'skip' and cd['tobuild'] == 0:
       cd['frommana'] -=3
       cd['tohp']-=3
        
    if cd['choice2'] == 'skip' and cd['frombuild'] == 0:
       cd['tomana'] -=3
       cd['fromhp']-=3
        
    if cd['choice1'] == 'skip' and cd['tobuild'] >0:
       cd['frommana'] -=5    
       cd['tobuild'] -=1
        
    if cd['choice2'] == 'skip' and cd['frombuild'] >0:
       cd['tomana'] -=5
       cd['frombuild'] -=1
        
        
    ###############################################################
    if cd['choice1'] == 'splashy tower':
       cd['frommana'] -=4
       cd['frombuild'] +=2
        
    if cd['choice2'] == 'splashy tower':
       cd['tomana'] -=4
       cd['tobuild']+=2
        
    query.message.edit_text(f'<b>{f}</b> chose {fchose}{a} and <b>{t}</b> chose {tchose}{b}\n'
                                f'results for this round\n\n'
                                f"<i><b>Round : {cd['round']}</b></i>\n\n"
                                f"❤<b>{f}</b> : {cd['fromhp']}\n🌀Mana : {cd['frommana']}\n🛕Splashy Tower : {cd['frombuild']}\n\n❤<b>{t}</b> : {cd['tohp']}\n🌀Mana : {cd['tomana']}\n🛕Splashy Tower : {cd['tobuild']}\n\n"
                                f"<b>{f} Make your decision</b>\n"
                                f'', parse_mode = ParseMode.HTML, reply_markup= reply_markup)
        
    if cd['fromhp'] == 0 or cd['tohp'] == 0:
          if cd['fromhp'] > cd['tohp']:
                    query.message.edit_text(f"{f} ❤️Hp : {cd['fromhp']}\n{t} ❤️Hp: {cd['tohp']}\n\n"
                                        f"{f} win !!\n"
                                        f'{f} gets a cookies\n')                
          elif cd['tohp'] > cd['fromhp']:
                    query.message.edit_text(f"{f} ❤️Hp : {cd['fromhp']}\n{t} ❤️Hp: {cd['tohp']}\n\n"
                                        f"{t} win !!\n"
                                        f'{t} gets a cookies\n')
          else:        
                query.message.edit_text(f"{f} ❤️Hp : {cd['fromhp']}\n{t} ❤️Hp: {cd['tohp']}\n\n"
                                        f" Draw!!\n")
          return ConversationHandler.END 
    return ONE
      
game_handler = ConversationHandler(
        entry_points=[CommandHandler('pro', game)],
        states={
            ONE: [
                CallbackQueryHandler(play, pattern='^' + str('play') + '$'),
                CallbackQueryHandler(rules, pattern='^' + str('rules') + '$'),
                CallbackQueryHandler(first, pattern='^' + str('carrier') + '$'),
                CallbackQueryHandler(first, pattern='^' + str('sky patrol') + '$'),
                CallbackQueryHandler(first, pattern='^' + str('splashy tower') + '$'),
                CallbackQueryHandler(first, pattern='^' + str('doragon') + '$'),
                CallbackQueryHandler(first, pattern='^' + str('skip') + '$')
            ],
            TWO: [
                CallbackQueryHandler(res, pattern='^' + str('carrier') + '$'),
                CallbackQueryHandler(res, pattern='^' + str('sky patrol') + '$'),
                CallbackQueryHandler(first, pattern='^' + str('splashy tower') + '$'),
                CallbackQueryHandler(first, pattern='^' + str('doragon') + '$'),
                CallbackQueryHandler(first, pattern='^' + str('skip') + '$')

            ],
        },
        fallbacks=[],

    allow_reentry=True,
    per_user=False
    )

dispatcher.add_handler(game_handler)
