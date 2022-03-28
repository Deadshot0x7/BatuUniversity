import time  as t 
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
def personal(update, c):
    update.message_text("Welcome to the Personal Function")

    return "Welcome to the Personal function"


def acdemic():
    return "Welcome to the Acedmic Selection"