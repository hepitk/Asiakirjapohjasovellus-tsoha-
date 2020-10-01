from app import app
from db import db
from flask import render_template, request, redirect
import users

@app.route("/")
def index():    
    sql = "SELECT id, docuname FROM documents ORDER BY id ASC"
    result = db.session.execute(sql)
    polls = result.fetchall()
    return render_template("index.html",polls=polls)

@app.route("/new")
def new():    
    sql = "SELECT phrase from phrases"
    result = db.session.execute(sql)
    list = result.fetchall()
    return render_template("new.html",count=len(list),phrases=list)

@app.route("/new_document")
def new_document():
    return render_template("new_document.html")

@app.route("/send", methods=["post"])
def send():
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
    return redirect("/new")

@app.route("/create", methods=["POST"])
def create():
    topic = request.form["topic"]
    user_id = users.user_id()
    if user_id == 0:
        return render_template("error.html",message="Asiakirjan luonti ei onnistunut, sillä et ole kirjautunut sisään")
    if len(topic) > 100:
        return render_template("error.html",message="Asiakirjan luonti ei onnistunut, sillä sen nimi on liian pitkä. Asiakirjan nimen enimmäispituus on 100 merkkiä.")
    if not (topic and topic.strip()):
        return render_template("error.html",message="Asiakirjan luonti ei onnistunut, sillä asiakirjan nimi ei saa olla tyhjä.")
    sql = "INSERT INTO documents (docuname) VALUES (:topic) RETURNING id"
    result = db.session.execute(sql, {"topic":topic})
    poll_id = result.fetchone()[0]
    db.session.commit()
    return redirect("/")

@app.route("/add_phrase/<int:id>")
def poll(id):
    sql = "SELECT docuname FROM documents WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT id, phrase FROM phrases ORDER BY id ASC"
    result = db.session.execute(sql, {"id":id})
    choices = result.fetchall()
    return render_template("add_phrase.html",id=id,topic=topic,choices=choices)

@app.route("/add", methods=["POST"])
def answer():
    poll_id = request.form["id"]
    if "add" in request.form:
        choice_id = request.form["add"]
        print (choice_id)
        sql = "UPDATE phrases SET document_id=:poll_id WHERE id=:choice_id"
        db.session.execute(sql, {"poll_id":poll_id,"choice_id":choice_id})
        db.session.commit()
    return redirect("/show_document/"+str(poll_id))

@app.route("/show_document/<int:id>")
def result(id):
    sql = "SELECT docuname FROM documents WHERE id=:id"
    result = db.session.execute(sql, {"id":id})
    topic = result.fetchone()[0]
    sql = "SELECT phrase FROM phrases WHERE document_id=:id"
    result = db.session.execute(sql, {"id":id})
    choices = result.fetchall()
    return render_template("show_document.html",topic=topic,choices=choices)

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
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

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",message="Rekisteröinti ei onnistunut")
