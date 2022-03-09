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

dor = cg.get_price(ids='doragonland', vs_currencies='usd',include_market_cap='true', include_24hr_vol='true', include_24hr_change='true')

aa = dor['doragonland']['usd']
ab = round(dor['doragonland']['usd_24h_vol'],2)
ac = round(dor['doragonland']['usd_24h_change'],2)
#ad = dor['doragonland']['usd']

tt = f'Name : DOR \nPRICE : {aa}$\n24 hour volume :{ab}$\n24 hour percent change : {ac}%'
def info(update , context):
    context.bot.send_message(chat_id = update.effective_chat.id, text =tt, parse_mode = ParseMode.HTML )
    
    
    
dispatcher.add_handler(CommandHandler("info", info))

