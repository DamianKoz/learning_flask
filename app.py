from flask import Flask, request

app = Flask(__name__)

articles = [
    {
        "title": "Das Problem mit Angebot und Nachfrage",
        "summary": """Es ist nicht gerecht, mehr zu verlangen, nur weil der 
        freie Markt das erlaubt""",
        "content": "lorem ipsum",
        "comments": [
            {
                "commentator": "Damian",
                "content": "Good article",
                "likes": 5,
            },
            {
                "commentator": "Macadamian",
                "content": "Good article",
                "likes": 0,
            },
        ],
    }
]


@app.get("/article")
def get_articles():
    return {"articles": articles}


@app.get("/article/<string:title>")
def get_article(title):
    for article in articles:
        if article.get("title") == title:
            return article, 200
    return {"message": "Article not found"}, 404


@app.get("/article/<string:title>/comments")
def get_article_comments(title):
    for article in articles:
        if article.get("title") == title:
            return article["comments"], 200
    return {"message": "Article not found"}, 404


@app.post("/article")
def create_article():
    data = request.get_json()
    new_article = {
        "title": data.get("title"),
        "summary": data.get("summary"),
        "content": data.get("content"),
    }
    print(new_article)
    articles.append(new_article)
    return new_article, 201


@app.post("/article/<string:title>/comment")
def create_comment(title):
    data = request.get_json()
    for article in articles:
        if article.get("title") == title:
            new_comment = {
                "commentator": data.get("commentator"),
                "content": data.get("content"),
                "likes": 0,
            }
            article["comments"].append(new_comment)
            print(articles)
            return new_comment, 201
    return {"message": "Article not found"}, 404
