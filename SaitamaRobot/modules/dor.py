import requests
from pycoingecko import CoinGeckoAPI

from telegram.ext import (
    Updater,
    CommandHandler,
    MessageHandler,
    Filters,
    ConversationHandler,
    CallbackContext,
)

from SaitamaRobot import dispatcher
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update, Message

cg = CoinGeckoAPI()
b = cg.get_coins_list()




#ad = dor['doragonland']['usd']


def dor(update , context):
    dor = cg.get_price(ids='doragonland', vs_currencies='usd',include_market_cap='true', include_24hr_vol='true', include_24hr_change='true')
    aa = dor['doragonland']['usd']
    ab = round(dor['doragonland']['usd_24h_vol'],2)
    ac = round(dor['doragonland']['usd_24h_change'],2)
    ad = ''
    try:
        num = update.message.text.split()[1]
        update.message.reply_text(chat_id = update.effective_chat.id, text =f'<code>Converting {num}DOR to USD.......</code>\n\n --{num*aa}', parse_mode = ParseMode.HTML)
        return -1
        
    except KeyError:
        pass

    if ac <0:
        ad = '😢'
    if ac>5 and ac<=10:
        ad ='😃'
    if ac>10 and ac<=30:
        ad ='🎊'
    if ac>30:
        ad ='🌙'
    
    
    tt = f'<b>Name :</b> DOR \n\n<b>Price :</b> {aa}$\n<b>24 hour volume :</b>{ab}$\n<b>24 hour percent change :</b> {ac}% {ad}'
    
    context.bot.send_message(chat_id = update.effective_chat.id, text =tt, parse_mode = ParseMode.HTML)
    
    
    
dispatcher.add_handler(CommandHandler("secret", dor))

