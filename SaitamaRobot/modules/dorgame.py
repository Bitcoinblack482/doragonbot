
ONE , TWO , THREE , FOUR , FIRST , SECOND,  *_ = range(50)


def janken(update: Update, context: CallbackContext):
    cd = context.chat_data
    
    cd['fighter'] = name = update.effective_user.first_name
    cd['fighterid'] = fid = update.effective_user.id
    
    cd['round'] = 1
    cd['fromhp'] = 3
    cd['tohp'] = 3
   
    keyboard = [
        [
            InlineKeyboardButton("Play", callback_data=str('play')),
            InlineKeyboardButton("Rules", callback_data=str('rules'))]
        ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    

    update.message.reply_text(f'*{name}* created a mini game\n\n'
                              f'*Game :* Fun\n\n'
                              f'*Lives :* 3', reply_markup = reply_markup , parse_mode = ParseMode.MARKDOWN_V2)
    return ONE
    
def rules(update: Update, context: CallbackContext):
    cd = context.chat_data
    f = cd['fighter']
    fid = cd['fighterid']
   
    query = update.callback_query
    query.answer('1.🐉Carrier beats 🏹RainOfFire , 🏹RainOfFire beats 🦇SkyPatrols , 🦇SkyPatrols beats 🐉Carrier', show_alert = True)
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

    keyboard = [
        [
            InlineKeyboardButton("🐉Carrier", callback_data=str('rock')),
            InlineKeyboardButton("🦇SkyPatrols", callback_data=str('paper')),
            InlineKeyboardButton("🏹RainOfFire", callback_data=str('scissor'))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    query.edit_message_text(
        text=f"_*Round : {cd['round']}*_\n\n"
             f"{f}❤ : {cd['fromhp']}\n{t}❤ : {cd['tohp']}\n\n"
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
            InlineKeyboardButton("🐉Carrier", callback_data=str('rock')),
            InlineKeyboardButton("🦇SkyPatrols", callback_data=str('paper')),
            InlineKeyboardButton("🏹RainOfFire", callback_data=str('scissor'))
        ]
    ]
    
    reply_markup2 = InlineKeyboardMarkup(keyboard)
    if update.callback_query.from_user.id != fid:
        query.answer('player 2 not ur turn')
        print(f'callback userid is {update.callback_query.from_user.id} and fid is {fid}')
        return None
    if update.callback_query.from_user.id == fid:
     query.edit_message_text(
        text=f"_*Round : {cd['round']}*_\n\n"
             f"{f}❤ : {cd['fromhp']}\n{t}❤ : {cd['tohp']}\n\n"
             f"*{t}* Make your decision\n", reply_markup=reply_markup2, parse_mode = ParseMode.MARKDOWN_V2
    )
    cd['round']+=1
    cd['choice1'] = query.data
    if tid == 163494588:
     context.bot.send_message(chat_id=163494588, text = f'{f} choose : {query.data}')
    if tid == 652962567:
     context.bot.send_message(chat_id=652962567, text=f'{f} choose : {query.data}')
    print('player 1 choose : '+str(cd['choice1'])+ ',id : ' + str(update.callback_query.from_user.id))
    return TWO

def res(update: Update, context: CallbackContext):
    cd = context.chat_data
    query = update.callback_query
    query.answer()
    cd['choice2'] = query.data
    f = cd['fighter']
    t = cd['to_name']
    fid = cd['fighterid']
    tid = cd['to_id']
    fchose = cd['choice1']
    tchose = cd['choice2']
    
    keyboard = [
        [
            InlineKeyboardButton("🐉Carrier ", callback_data=str('rock')),
            InlineKeyboardButton("🦇SkyPatrols ", callback_data=str('paper')),
            InlineKeyboardButton("🏹RainOfFire ", callback_data=str('scissor'))
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    if update.callback_query.from_user.id != tid:
        query.answer('player 2 not ur turn')
        return None
    choice = {
            "rock": "🐉",
            "paper": "🦇",
             "scissor": "🏹"
                        }

    a = choice[cd['choice1']]
    b = choice[cd['choice2']]
    if update.callback_query.from_user.id != tid:
        query.answer('player 1 not ur turn')
        return None
      
    if cd['choice1'] == cd['choice2']:
        cd['fromhp'] -= 1
        cd['tohp'] -= 1
        query.message.edit_text(f'*{f}* chose {fchose}{a} and *{t}* chose {tchose}{b}\n'
                                f'_its a Draw_\n\n'
                                f"_*Round : {cd['round']}*_\n"
             f"❤{f} : {cd['fromhp']}\n❤{t} : {cd['tohp']}\n\n"
             f"*{f}*Make you decision\n"
                                f'{t}', parse_mode=ParseMode.MARKDOWN_V2, reply_markup= reply_markup)

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
     
    elif cd['choice1'] == 'rock' and cd['choice2'] == 'scissor':
        cd['fromhp'] -= 0
        cd['tohp'] -= 1
        query.message.edit_text(f'*{f}* chose {fchose}{a} and *{t}* chose {tchose}{b}\n'
                                f'_[{f}](tg://user?id={fid}) wins_\n\n'
                                f"_*Round : {cd['round']}*_\n"
             f"❤{f} : {cd['fromhp']}\n❤{t} : {cd['tohp']}\n\n"
             f"*{f}*Make you decision\n"
                                , parse_mode=ParseMode.MARKDOWN_V2,reply_markup= reply_markup)

        if cd['fromhp'] == 0 or cd['tohp'] == 0:
          if cd['fromhp'] > cd['tohp']:
                if type == 'white':
                    query.message.edit_text(f"{f} ❤️Hp : {cd['fromhp']}\n{t} ❤️Hp: {cd['tohp']}\n\n"
                                        f"{f} win !!\n"
                                        f'{f} gets a cookies\n')
                
          elif cd['tohp'] > cd['fromhp']:
                    query.message.edit_text(f"{f} ❤️Hp : {cd['fromhp']}\n{t} ❤️Hp: {cd['tohp']}\n\n"
                                        f"{t} win !!\n"
                                        f'{t} gets a cookies\n')
          else:
                
                query.message.edit_text(f"{f} ❤️Hp : {cd['fromhp']}\n{t} ❤️Hp: {cd['tohp']}\n\n"
                                        f" Draw !!\n")
          return ConversationHandler.END

        return ONE

    elif cd['choice1'] == 'scissor' and cd['choice2'] == 'rock':
        cd['fromhp'] -= 1
        cd['tohp'] -= 0
        query.message.edit_text(f'*{f}* chose {fchose}{a} and *{t}* chose {tchose}{b}\n'
                                f'_[{t}](tg://user?id={tid}) wins_\n\n'
                                f"_*Round : {cd['round']}*_\n"
             f"❤{f} : {cd['fromhp']}\n❤{t} : {cd['tohp']}\n\n"
             f"*{f}*Make you decision\n"
                                , parse_mode=ParseMode.MARKDOWN_V2,reply_markup= reply_markup)

        if cd['fromhp'] == 0 or cd['tohp'] == 0:
          if cd['fromhp'] > cd['tohp']:
                if type == 'white':
                    query.message.edit_text(f"{f} ❤️Hp : {cd['fromhp']}\n{t} ❤️Hp: {cd['tohp']}\n\n"
                                        f"{f} win !!\n"
                                        f'{f} gets a cookies\n')               
          elif cd['tohp'] > cd['fromhp']:
                    query.message.edit_text(f"{f} ❤️Hp : {cd['fromhp']}\n{t} ❤️Hp: {cd['tohp']}\n\n"
                                        f"{t} win !!\n"
                                        f'{t} gets a cookies\n')
          else:
                
                query.message.edit_text(f"{f} ❤️Hp : {cd['fromhp']}\n{t} ❤️Hp: {cd['tohp']}\n\n"
                                        f" Draw !!\n")
          return ConversationHandler.END

        return ONE

    elif cd['choice1'] == 'rock' and cd['choice2'] == 'paper':
        cd['fromhp'] -= 1
        cd['tohp'] -= 0
        query.message.edit_text(f'*{f}* chose {fchose}{a} and *{t}* chose {tchose}{b}\n'
                                f'_[{t}](tg://user?id={tid}) wins_\n\n'
                                f"_*Round : {cd['round']}*_\n"
             f"❤{f} : {cd['fromhp']}\n❤{t} : {cd['tohp']}\n\n"
             f"*{f}*Make you decision\n"
                                , parse_mode=ParseMode.MARKDOWN_V2,reply_markup= reply_markup)

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
                                        f" Draw !!\n")
          return ConversationHandler.END

        return ONE

    elif cd['choice1'] == 'paper' and cd['choice2'] == 'rock':
        cd['fromhp'] -= 0
        cd['tohp'] -= 1
        query.message.edit_text(f'*{f}* chose {fchose}{a} and *{t}* chose {tchose}{b}\n'
                                f'_[{f}](tg://user?id={fid}) wins_\n\n'
                                f"_*Round : {cd['round']}*_\n"
             f"❤{f} : {cd['fromhp']}\n❤{t} : {cd['tohp']}\n\n"
             f"*{f}*Make you decision\n"
                                , parse_mode=ParseMode.MARKDOWN_V2,reply_markup= reply_markup)

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

    elif cd['choice1'] == 'paper' and cd['choice2'] == 'scissor':
        cd['fromhp'] -= 1
        cd['tohp'] -= 0
        query.message.edit_text(f'*{f}* chose {fchose}{a} and *{t}* chose {tchose}{b}\n'
                                f'_[{t}](tg://user?id={tid}) wins_\n\n'
                                f"_*Round : {cd['round']}*_\n"
             f"❤{f} : {cd['fromhp']}\n❤{t} : {cd['tohp']}\n\n"
             f"*{f}*Make you decision\n"
                                , parse_mode=ParseMode.MARKDOWN_V2,reply_markup= reply_markup)

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

    elif cd['choice1'] == 'scissor' and cd['choice2'] == 'paper':
        cd['fromhp'] -= 0
        cd['tohp'] -= 1
        query.message.edit_text(f'*{f}* chose {fchose}{a} and *{t}* chose {tchose}{b}\n'
                                f'_[{f}](tg://user?id={fid}) wins_\n\n'
                                f"_*Round : {cd['round']}*_\n"
             f"❤{f} : {cd['fromhp']}\n❤{t} : {cd['tohp']}\n\n"
             f"*{f}*Make you decision\n"
                                , parse_mode=ParseMode.MARKDOWN_V2,reply_markup= reply_markup)

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
      
janken_handler = ConversationHandler(
        entry_points=[CommandHandler('game', game)],
        states={
            ONE: [
                CallbackQueryHandler(play, pattern='^' + str('play') + '$'),
                CallbackQueryHandler(rules, pattern='^' + str('rules') + '$'),
                CallbackQueryHandler(first, pattern='^' + str('rock') + '$'),
                CallbackQueryHandler(first, pattern='^' + str('scissor') + '$'),
                CallbackQueryHandler(first, pattern='^' + str('paper') + '$')
            ],
            TWO: [
                CallbackQueryHandler(res, pattern='^' + str('rock') + '$'),
                CallbackQueryHandler(res, pattern='^' + str('scissor') + '$'),
                CallbackQueryHandler(res, pattern='^' + str('paper') + '$')

            ],
        },
        fallbacks=[],

    allow_reentry=True,
    per_user=False,
    run_async=True
    )

dispatcher.add_handler(janken_handler)
