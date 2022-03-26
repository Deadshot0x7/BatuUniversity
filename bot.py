import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
PORT = int(os.environ.get('PORT', '8443'))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '5284073049:AAFIjNHJCPb5CoDOAa_jXEyQ4ahrVjgm73A'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Welcome to the  BATU Univeristy Bot ')
    update.message.reply_text('Developed By Sayyed Viquar Ahmed')    

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Welcome to the Univeristy Bot')
    
    update.message.reply_text('/start            Start the Telegram bot')
    update.message.reply_text("/PerInfo          show you personal Information with PRN Number ")
    

def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def mantasha (update, context):

    update.message.reply_text ('Hello Ahmed , I hope youre doing well today ')

def isue(update, context):

    update.message.reply_text ('Got a Issue Submit yout issue at ')




def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("issue",isue))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(
        listen="0.0.0.0",
        port=int(PORT),
        url_path=TOKEN,
        webhook_url='https://batuuniversitybot.herokuapp.com/' + TOKEN
    )

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()