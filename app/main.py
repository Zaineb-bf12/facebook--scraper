from fastapi import FastAPI

from facebook_scraper import get_posts
import pymongo

app = FastAPI()

# Variables de connexion à la base de données
client = pymongo.MongoClient("mongodb://mongo:27017/")
db = client["mydatabase"]
collection = db["facebook_posts"]

# Endpoint pour récupérer les données de la page Facebook
@app.get("/scrape")
async def scrape():
    # Set the Facebook page or group URL
    url = "Microsoft"
    # URL de la page Facebook à scraper
    extracted_pages = []
    for post in get_posts(url):
        # Print the post's text content and date
        text =post['text']
        time=post['time']
        video=post['video']
        likes = post['likes']
        comments = post['comments']
        shares = post['shares']
        p = {"text": text, "time": time,"video": video, "likes": likes,"comments": comments, "time": time}
        collection.insert_one(p)   
    return {"message": "Scrapping done!"}