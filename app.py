from flask import Flask, render_template, request, session, make_response
import os
from slugify import slugify
from articles import Article
import hashlib

app = Flask(__name__)

app.secret_key = "thisisverysecret"

# Authentication
# Cookie

articles = Article.all()

users={
    "admin": "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"
}

@app.route("/")
def blog():
    return render_template("blog.html", articles=articles)



@app.get("/admin")
def admin_page():
    if "user" in session:
        return "you are already authenticated"
    
    return render_template("login.html")
@app.get("/logout")
def logout():
    del session["user"]
    return "logged out"

@app.post("/admin")
def admin_login():
    username = request.form["username"]
    password = request.form["password"]
    if username not in users:
        return render_template("login.html", error="username/password incorrect")
    hashed = hashlib.sha256(password.encode()).hexdigest()
    
    if users[username] != hashed:
        return render_template("login.html", error="username/password incorrect")
    
    session["user"] = username
    return "you are now authenticated"    
    
    

@app.route("/blog/<zslug>")
def article(slug: str):
    article = articles[slug]
   
    return render_template("article.html", article=article)

if __name__ == "__main__":
    app.run(port=4200, debug=True)
