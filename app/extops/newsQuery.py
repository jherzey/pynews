import requests
import json


class NewsQuery:
    def fetchNews(self, queryData):
        queryResponse = requests.get(
            url=queryData["newsUrl"], params=queryData["params"]
        )
        resData = json.loads(queryResponse.content)
        return resData

    def orderNews(self, queryData):
        newsChunk = self.fetchNews(queryData)
        newsItems = []
        if newsChunk["status"] == "ok":
            for newsBit in newsChunk["articles"]:
                newsItem = {
                    "source": newsBit["source"]["name"],
                    "author": newsBit["author"],
                    "title": newsBit["title"],
                    "description": newsBit["description"],
                    "newsUrl": newsBit["url"],
                    "publishedAt": newsBit["publishedAt"],
                }
                newsItems.append(newsItem)
        elif newsChunk["status"] == "error":
            print(newsChunk["status"])
        return newsItems

