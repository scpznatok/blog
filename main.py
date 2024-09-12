from flask import Flask, redirect, render_template, request
import db

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/categories")
def category_list():
    return render_template("category_list.html",
                           category_list=db.getCategories())

@app.route("/posts", methods=["GET", "POST"])
def post_list():
    
    if request.method == "POST":
        category_id = request.form.get("category_id")
        text = request.form.get("text")
        #validate category id
        db.addPost(category_id, text)
        
        return redirect(f"/posts")
    
    
    
    return render_template("post_list.html",
                           post_list=db.getPosts())
    
    

@app.route("/categories/<id>", methods=["GET", "POST"])
def posts_by_category(id):
    
    if request.method == "POST":
        category_id = request.form.get("category_id")
        text = request.form.get("text")
        #validate category id
        db.addPost(category_id, text)
        
        return redirect(f"/categories/{id}")
    
    
    return render_template("post_list.html",
                           post_list=db.getPostsByCategory(id))

    
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")