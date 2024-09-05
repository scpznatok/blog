from flask import Flask, render_template
import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/categories")
def category_list():
    return render_template("category_list.html",
                           category_list=db.getCategories())

@app.route("/posts")
def post_list():
    return render_template("post_list.html",
                           post_list=db.getPosts())

@app.route("/categories/<id>")
def posts_by_category(id):
    return render_template("post_list.html",
                           post_list=db.getPostsByCategory(id))

    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")