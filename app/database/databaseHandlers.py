import pyrebase
from utils import config


class Database:
    def __init__(self):
        self.fbConfig = config.firebaseConfig
        self.firebase = pyrebase.initialize_app(self.fbConfig)
        self.database = self.firebase.database()

    def createUser(self, userInfo):
        self.database.child("Users").child(userInfo["chatId"]).set(userInfo)

    def dropUser(self, chatId):
        categories = [
            "General",
            "Business",
            "Health",
            "Technology",
            "Sports",
            "Entertainment",
        ]
        dropStatus = ""
        user = self.database.child("Users").child(chatId).get().val()
        try:
            if user:
                self.database.child("Users").child(chatId).remove()
                for category in categories:
                    self.database.child(category + "Subscribers").child(chatId).remove()
                    dropStatus = True
            else:
                dropStatus = False
        except:
            pass
        return dropStatus

    def setUserLanguage(self, languageInfo):
        self.database.child("Users").child(languageInfo["chatId"]).update(
            {"language": languageInfo["language"]}
        )

    def updateCatageryPrefs(self, userInfo):
        user = self.database.child("Users").child(userInfo["chatId"]).get().val()
        preferedCategories = user["preferedCategories"]
        feedback = ""
        if user["preferedCategories"][0] == "none":
            preferedCategories = [userInfo["preferedCategory"]]
            feedback = "appended"
        elif userInfo["preferedCategory"] in preferedCategories:
            feedback = "chosen"
        else:
            preferedCategories.append(userInfo["preferedCategory"])
            feedback = "appended"

        self.database.child("Users").child(userInfo["chatId"]).update(
            {"preferedCategories": preferedCategories}
        )
        return feedback

    def getUserLanguage(self, chatId):
        user = self.database.child("Users").child(chatId).get().val()
        return user["language"]

    def placeInCategory(self, userInfo):
        self.database.child(userInfo["preferedCategory"] + "Subscribers").child(
            userInfo["chatId"]
        ).set(userInfo)

    def dropUserCategory(self, chatId, category):
        dropStatus = ""
        user = self.database.child("Users").child(chatId).get().val()
        try:
            if category in user["preferedCategories"]:
                user["preferedCategories"].remove(category)
                self.database.child(category + "Subscribers").child(chatId).remove()
                self.database.child("Users").child(chatId).set(user)
                dropStatus = True
            else:
                dropStatus = False
        except:
            pass
        return dropStatus

    def getNewsSubscribers(self, category):
        users = self.database.child(category + "Subscribers").get().val()
        chatIds = []
        try:
            chatIds = users.keys()
        except AttributeError:
            pass
        return chatIds

