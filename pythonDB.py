from pymongo import MongoClient

db = MongoClient(
    "mongodb+srv://TechZ:shreyash123@websitedata.wdycbvp.mongodb.net/?retryWrites=true&w=majority&appName=WebsiteData"
).AnimeThumb.WebsiteViews


def increaseViews(website):
    db.update_one({"website": website}, {"$inc": {"Views": 10}}, upsert=True)


from flask import Flask, request
from urllib.parse import urlparse
import requests

app = Flask(__name__)


@app.route("/increaseViews")
def increaseViewsRoute():
    website = request.headers.get("Referer")
    if website is None:
        website = request.headers.get("referer")

    if website is None:
        website = "direct"
    else:
        try:
            website = urlparse(website).netloc
        except Exception as e:
            requests.get(
                "https://worker-curly-math-37b8.techzbots1.workers.dev/rM8kBk5lzLropzqxZsaxc3L5ndgDzJ21t7lLreY5yG7sGRj2TH",
                headers={"text": "from pythondb" + str(e)},
            )
            pass
    print(website)
    increaseViews(website)
    return "Views increased by 10"


import os

if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
