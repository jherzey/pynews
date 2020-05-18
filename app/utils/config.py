import telegram

botConfig = 'bot token'

newsApiConfig = {
    "General": {
        "newsUrl": "https://newsapi.org/v2/top-headlines",
        "params": {
            "apiKey": "newsApiKey",
            "pageSize": "3",
            "sources": "bbc-news",
            "language": "en",
        },
    },
    "Business": {
        "newsUrl": "https://newsapi.org/v2/top-headlines",
        "params": {
            "apiKey": "newsApiKey",
            "pageSize": "3",
            "sources": "business-insider",
            "language": "en",
        },
    },
    "Health": {
        "newsUrl": "https://newsapi.org/v2/top-headlines",
        "params": {
            "apiKey": "newsApiKey",
            "pageSize": "3",
            "sources": "medical-news-today",
            "language": "en",
        },
    },
    "Technology": {
        "newsUrl": "https://newsapi.org/v2/top-headlines",
        "params": {
            "apiKey": "newsApiKey",
            "pageSize": "3",
            "sources": "engadget",
            "language": "en",
        },
    },
    "Sports": {
        "newsUrl": "https://newsapi.org/v2/top-headlines",
        "params": {
            "apiKey": "newsApiKey",
            "pageSize": "3",
            "sources": "bbc-sport",
            "language": "en",
        },
    },
    "Entertainment": {
        "newsUrl": "https://newsapi.org/v2/top-headlines",
        "params": {
            "apiKey": "newsApiKey",
            "pageSize": "3",
            "sources": "entertainment-weekly",
            "language": "en",
        },
    },
}

firebaseConfig = {
    "apiKey": "firebaseApiKey",
    "authDomain": "firebaseAuthDomain",
    "databaseURL": "firebaseDatabaseURL",
    "projectId": "firebaseProjectId",
    "storageBucket": "storageBucket",
    "messagingSenderId": "messageSenderId",
    "appId": "firebaseAppId",
}
