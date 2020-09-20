from app import app
from db import db
from flask import render_template, request, redirect
import phrases, users

@app.route("/")
def index():    
    sql = "SELECT id, docuname FROM documents ORDER BY id ASC"
    result = db.session.execute(sql)
    polls = result.fetchall()
    return render_template("index.html",polls=polls)

@app.route("/new")
def new():
    list = phrases.get_list()
    return render_template("new.html",count=len(list),phrases=list)

@app.route("/new_document")
def new_document():
    return render_template("new_document.html")

@app.route("/send", methods=["post"])
def send():
    content = request.form["content"]
    if phrases.send(content):
        return redirect("/new")
    else:
        return render_template("error.html",message="Fraasin luonti ei onnistunut")

@app.route("/create", methods=["POST"])
def create():
    topic = request.form["topic"]
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
