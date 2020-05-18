from static import appInteractions
from extops import newsQuery

appRes = appInteractions.AppInteractions()


class CallbackQueryHandlers:
    def __init__(self):
        self.newsLanguages = ["en", "ru", "fr", "it"]

    def handleStartCallback(self, callbackquery):
        callbackFeedback = ""
        if callbackquery == "subscribeOption":
            callbackFeedback = "subscribe"
        elif callbackquery == "getFeedOption":
            callbackFeedback = "instantNews"
        elif callbackquery in self.newsLanguages:
            callbackFeedback = "languageChosen"

        return callbackFeedback
