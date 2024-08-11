from flask import Flask, render_template
import os

app = Flask(__name__)
articles=os.listdir("articles")


@app.route("/")
def blog():
    return render_template("blog.html", articles=articles)

@app.route("/blog/<slug>")
def article(slug: str):
    return render_template("article.html")

if __name__ == "__main__":
    app.run(port=4200, debug=True)
