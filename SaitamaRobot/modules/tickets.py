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

BOTID = 1338281900
maingroup = -753748989
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
    print(f'message is sent from : {fromid}')
    context.bot.forward_message(chat_id=maingroup, from_chat_id=fromid, message_id=msgid)
    return -1

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
        print(id)
    except AttributeError:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'this user has forward privacy turned on, unable to track user')
        return -1
    if isreply(update.message):
           context.bot.send_message(chat_id = id , text = f"{c}\n\n<i>Answered by :</i> {b}", parse_mode = ParseMode.HTML)
           return -1
    print('phase3 ends')


dispatcher.add_handler(CommandHandler("reply", reply))
ticket_handler = ConversationHandler(
    entry_points = [CommandHandler("ticket", ticket)],
    states = {
        0: [MessageHandler(Filters.text, ticket2)]
    },

    fallbacks = [],
    allow_reentry = True,
    per_chat=False
)
dispatcher.add_handler(ticket_handler)


