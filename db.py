import sqlite3

db_name = "blog.db"
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
def close():
    cursor.close()
    conn.close()

def getCategories():
    open()
    cursor.execute("SELECT * FROM category")
    res = cursor.fetchall()
    close()
    return res

def getPosts():
    open()
    cursor.execute("SELECT * FROM post")
    res = cursor.fetchall()
    close()
    return res

def getPostsByCategory(category_id):
    open()
    cursor.execute("SELECT * FROM post WHERE category_id = ?", [category_id])
    res = cursor.fetchall()
    close()
    return res

def addPost(category_id, text):
    open()
    cursor.execute("INSERT INTO post (category_id, text) VALUES (?,?);", [category_id, text])
    conn.commit()
    close()