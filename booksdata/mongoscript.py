from pymongo import MongoClient
import datetime

# Local Host String 
client = MongoClient("mongodb://localhost:27017/")


db = client.scrapy_books

posts = db.book_data

doc = post = {"author": "Vivek",
        "text": "My second blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

post_id = posts.insert_one(post).inserted_id

print(post_id)