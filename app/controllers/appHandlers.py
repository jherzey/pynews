import telegram
from telegram.ext import Updater, Dispatcher, CommandHandler, MessageHandler
import utils.config as config
from extops import newsQuery
from controllers.callbackquery import CallbackQueryHandlers
from database.databaseHandlers import Database
from static.appInteractions import AppInteractions


appKey = config.botConfig["token"]
app = telegram.Bot(appKey)
updater = Updater(appKey)
dispatcher = updater.dispatcher
callbackController = CallbackQueryHandlers()
db = Database()
appRes = AppInteractions()
newsQueryData = config.newsApiConfig
nQ = newsQuery.NewsQuery()


class AppHandlers:
    def __init__(self):
        self.appKey = config.botConfig["token"]
        self.app = telegram.Bot(appKey)
        self.updater = Updater(appKey)
        self.dispatcher = updater.dispatcher
        self.newsCategories = [
            "General",
            "Business",
            "Health",
            "Technology",
            "Sports",
            "Entertainment",
        ]

    def handleStart(self, app, update):
        app.sendMessage(
            update.message.chat_id,
            appRes.startReply,
            reply_markup=appRes.startNewsKeyboard,
        )

    def handleSubscribe(self, app, update):
        chatId = update.message.chat_id
        userInfo = {
            "chatId": chatId,
            "userName": update.message.chat.first_name,
            "preferedCategories": ["none"],
        }
        db.createUser(userInfo)
        app.sendMessage(
            chatId, appRes.languageOptionReply, reply_markup=appRes.newsCountryKeyboard
        )

    def handleInstantNews(self, app, update):
        chatId = update.message.chat_id
        app.sendMessage(
            chatId,
            appRes.newsCategoryReply,
            reply_markup=appRes.instantCategoryKeyboard,
        )

    def addCategory(self, app, update):
        chatId = update.message.chat_id
        app.sendMessage(
            chatId, appRes.newsCategoryReply, reply_markup=appRes.categoryKeyboard
        )

    def dropCategory(self, app, update):
        chatId = update.message.chat_id
        app.sendMessage(
            chatId, appRes.newsCategoryReply, reply_markup=appRes.deleteCategoryKeyboard
        )

    # def subnews(self, app, update):
    #     nc = NewsCaster(app)
    #     nc.castNews()

    def handleNewsQueryCallback(self, app, update):
        username = update.callback_query.message.chat.first_name
        chatId = update.callback_query.message.chat.id
        callbackQuery = update.callback_query.data
        if callbackController.handleStartCallback(callbackQuery) == "subscribe":
            userInfo = {
                "userName": username,
                "chatId": chatId,
                "preferedCategories": ["none"],
            }
            db.createUser(userInfo)
            app.sendMessage(
                chatId,
                appRes.languageOptionReply,
                reply_markup=appRes.newsCountryKeyboard,
            )
        elif callbackController.handleStartCallback(callbackQuery) == "instantNews":
            app.sendMessage(
                chatId,
                appRes.newsCategoryReply,
                reply_markup=appRes.instantCategoryKeyboard,
            )
        elif callbackController.handleStartCallback(callbackQuery) == "languageChosen":
            userInfo = {"chatId": chatId, "language": callbackQuery}
            db.setUserLanguage(userInfo)
            app.sendMessage(
                chatId, appRes.newsCategoryReply, reply_markup=appRes.categoryKeyboard
            )
        elif callbackQuery in self.newsCategories:
            userInfo = {
                "chatId": chatId,
                "preferedCategory": callbackQuery,
                "userName": username,
            }
            status = db.updateCatageryPrefs(userInfo)
            if status == "appended":
                app.sendMessage(chatId, appRes.addCategoryReply)
                db.placeInCategory(userInfo)
            elif status == "chosen":
                app.sendMessage(chatId, appRes.chosenCategoryReply)
            else:
                app.sendMessage(chatId, appRes.newCategoryReply)

        elif callbackQuery[7:] in self.newsCategories:
            newQueryData = newsQueryData[callbackQuery[7:]]
            language = db.getUserLanguage(chatId)
            if language != "en":
                newQueryData["params"]["language"] = language
                newQueryData["params"]["sources"] = ""
            app.sendMessage(chatId, appRes.pendingNewsReply)
            for newsRaw in nQ.orderNews(newQueryData):
                newsItem = f"\n {newsRaw['newsUrl']} \n \n Source: {newsRaw['source']} \n Author: {newsRaw['author']} \n Title: {newsRaw['title']} \n Description: {newsRaw['description']} \n \n Publish Time: {newsRaw['publishedAt']}"
                app.sendMessage(chatId, newsItem)

        elif callbackQuery[6:] in self.newsCategories:
            if db.dropUserCategory(chatId, callbackQuery[6:]) == True:
                app.sendMessage(chatId, appRes.droppedCategoryReply)
            else:
                app.sendMessage(chatId, appRes.notSubscriberReply)


class NewsCaster:
    def __init__(self, app):
        self.app = app
        self.newsCategories = [
            "General",
            "Business",
            "Health",
            "Technology",
            "Sports",
            "Entertainment",
        ]

    def prepareSubscriberInfo(self, category):
        subscribersInfo = []
        subscribers = db.getNewsSubscribers(category)
        for subscriber in subscribers:
            language = db.getUserLanguage(subscriber)
            subscriberInfo = {"chatId": subscriber, "language": language}
            subscribersInfo.append(subscriberInfo)
        return subscribersInfo

    def castNews(self):
        for category in self.newsCategories:
            newsBulletin = {"category": category, "items": []}
            newQueryData = newsQueryData[category]
            for subscriber in self.prepareSubscriberInfo(category):
                try:
                    if subscriber["language"] != "en":
                        newQueryData["params"]["language"] = subscriber["language"]
                        newQueryData["params"]["sources"] = ""
                    for newsRaw in nQ.orderNews(newQueryData):
                        newsItem = f"\n {newsRaw['newsUrl']} \n \n Source: {newsRaw['source']} \n Author: {newsRaw['author']} \n Title: {newsRaw['title']} \n Description: {newsRaw['description']} \n \n Publish Time: {newsRaw['publishedAt']}"
                        newsBulletin["items"].append(newsItem)
                    self.app.sendMessage(
                        subscriber["chatId"], newsBulletin["category"] + " News"
                    )
                    for item in newsBulletin["items"]:
                        self.app.sendMessage(subscriber["chatId"], item)
                except:
                    db.dropUser(subscriber["chatId"])

