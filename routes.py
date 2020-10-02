from app import app
from db import db
from flask import render_template, request, redirect
import users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/new_phrase")
def new_phrase_page():
    return render_template("new_phrase.html")

@app.route("/new_phrase",methods=["post"])
def new_phrase_create():
    content = request.form["content"]
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html",message="Fraasin luonti ei onnistunut, sillä et ole kirjautunut sisään")
    if len(content) > 5000:
        return render_template("error.html",message="Fraasin luonti ei onnistunut, sillä se on liian pitkä. Fraasin enimmäispituus on 5000 merkkiä.")
    if not (content and content.strip()):
        return render_template("error.html",message="Fraasin luonti ei onnistunut, sillä se ei saa olla tyhjä.")
    sql = "INSERT INTO phrases (phrase) VALUES (:content)"
    db.session.execute(sql, {"content":content})
    db.session.commit()
    return redirect("/show_phrase_list")

@app.route("/show_phrase_list")
def show_phrase_list_page():    
    sql = "SELECT phrase from phrases"
    result = db.session.execute(sql)
    phrases = result.fetchall()
    return render_template("show_phrase_list.html",count=len(phrases),phrases=phrases)

@app.route("/new_document")
def new_document_page():
    return render_template("new_document.html")

@app.route("/new_document",methods=["post"])
def new_document_create():
    content = request.form["content"]
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html",message="Asiakirjan luonti ei onnistunut, sillä et ole kirjautunut sisään")
    if len(content) > 100:
        return render_template("error.html",message="Asiakirjan luonti ei onnistunut, sillä sen nimi on liian pitkä. Asiakirjan nimen enimmäispituus on 100 merkkiä.")
    if not (content and content.strip()):
        return render_template("error.html",message="Asiakirjan luonti ei onnistunut, sillä asiakirjan nimi ei saa olla tyhjä.")
    sql = "INSERT INTO documents (docuname) VALUES (:content) RETURNING id"
    result = db.session.execute(sql, {"content":content})
    poll_id = result.fetchone()[0]
    db.session.commit()
    return redirect("/show_document_list")

@app.route("/add_phrase/<int:id>")
def add_phrase_page(id):
    sql = "SELECT docuname FROM documents WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    docuname = result.fetchone()[0]
    sql = "SELECT id, phrase FROM phrases ORDER BY id ASC"
    result = db.session.execute(sql, {"id":id})
    phrases = result.fetchall()
    return render_template("add_phrase.html",id=id,docuname=docuname,phrases=phrases)

@app.route("/show_document_list")
def show_document_list_page():
    sql = "SELECT id,docuname FROM documents ORDER BY id ASC"
    result = db.session.execute(sql)
    documents = result.fetchall()
    return render_template("show_document_list.html",documents=documents)

@app.route("/add_phrase",methods=["post"])
def add_phrase():
    document_id = request.form["id"]
    if "add" in request.form:
        phrase_id = request.form["add"]        
        sql = "UPDATE phrases SET document_id=:document_id WHERE id=:phrase_id"
        db.session.execute(sql, {"document_id":document_id,"phrase_id":phrase_id})
        db.session.commit()
    return redirect("/show_document/"+str(document_id))

@app.route("/show_document/<int:id>")
def show_document_page(id):
    sql = "SELECT docuname FROM documents WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    docuname = result.fetchone()[0]
    sql = "SELECT phrase FROM phrases WHERE document_id=:id"
    result = db.session.execute(sql, {"id":id})
    phrases = result.fetchall()
    return render_template("show_document.html",docuname=docuname,phrases=phrases)

@app.route("/login",methods=["get","post"])
def login():
    if request.method == "get":
        return render_template("login.html")
    if request.method == "post":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Väärä tunnus tai salasana")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register",methods=["get","post"])
def register():
    if request.method == "get":
        return render_template("register.html")
    if request.method == "post":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")
