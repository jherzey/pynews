import time
import threading
import schedule
import telegram
from telegram.ext import (
    Updater,
    Dispatcher,
    CommandHandler,
    MessageHandler,
    CallbackQueryHandler,
)
import utils.config as config
from controllers.appHandlers import AppHandlers, NewsCaster

appKey = config.botConfig["token"]
app = telegram.Bot(appKey)
updater = Updater(appKey)
dispatcher = updater.dispatcher
apphandlers = AppHandlers()
newsCast = NewsCaster(app)


def getApp():
    print(app.getMe().first_name)


def job():
    newsCast.castNews()


def newsTime():
    schedule.every().day.at("07:56").do(job)
    schedule.every().day.at("07:45").do(job)
    schedule.every().day.at("07:47").do(job)
    while True:
        schedule.run_pending()


def main():

    castNewsThread = threading.Thread(target=newsTime)
    getApp()

    dispatcher.add_handler(CommandHandler("start", apphandlers.handleStart))
    dispatcher.add_handler(CommandHandler("subscribe", apphandlers.handleSubscribe))
    dispatcher.add_handler(CommandHandler("instantNews", apphandlers.handleInstantNews))
    dispatcher.add_handler(CommandHandler("addcategory", apphandlers.addCategory))
    dispatcher.add_handler(CommandHandler("dropcategory", apphandlers.dropCategory))
    # dispatcher.add_handler(CommandHandler("subnews", apphandlers.subnews))
    dispatcher.add_handler(CallbackQueryHandler(apphandlers.handleNewsQueryCallback))

    updater.start_polling()
    castNewsThread.start()


if __name__ == "__main__":
    main()
