from flask import redirect, render_template, request, jsonify, flash
from db_helper import reset_db
from repositories.todo_repository import get_todos, create_todo, set_done, delete
from config import app, test_env
from util import validate_todo

@app.route("/")
def index():
    todos = get_todos()
    unfinished = len([todo for todo in todos if not todo.done])
    return render_template("index.html", todos=todos, unfinished=unfinished) 

@app.route("/new_todo")
def new():
    return render_template("new_todo.html")

@app.route("/create_todo", methods=["POST"])
def todo_creation():
    content = request.form.get("content")

    try:
        validate_todo(content)
        create_todo(content)
        return redirect("/")
    except Exception as error:
        flash(str(error))
        return  redirect("/new_todo")

@app.route("/toggle_todo/<todo_id>", methods=["POST"])
def toggle_todo(todo_id):
    set_done(todo_id)
    return redirect("/")

# testausta varten oleva reitti
if test_env:
    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return jsonify({ 'message': "db reset" })

@app.route("/delete/<int:citations_id>", methods=["GET", "POST"]) #muokkaa lähde.id jos pitää
def delete(citations_id):
    citations = todo_repositorys.get_citations(citations_id) #oletus mistä lähde löytyy

    if request.method == "GET":
        return render_template("poisto.html", citations=citations)
    
    if request.method == "POST":
        if "delete" in request.form:
            todo_repository.delete(citations["id"])  #oletus miten lähde poistetaan, forum = todo_repository?
        return redirect("/aloitussivu/" + str(citations["aloitussivu_id"])) #vaihda oletus aloittussivu/thread