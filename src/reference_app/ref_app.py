from flask import Flask, request, redirect, url_for, render_template, abort
from config import app, db
from repositories.references_repository import get_references, add_new_reference, update_reference, get_reference

@app.route('/')
def index():
    citations = get_references()
    return render_template("index.html", citations=citations)

@app.route("/new_reference")
def new_reference():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def add_reference():
    title = request.form["title"]
    authors = request.form["authors"]
    year = request.form["year"]
    isbn = request.form["isbn"]
    publisher = request.form["publisher"]

    add_new_reference(title, authors, year, isbn, publisher)

    return redirect(url_for("index"))

@app.route("/edit/<int:reference_id>", methods=["GET","POST"])
def edit_reference(reference_id):
    reference = get_reference(reference_id)

    if not reference:
        abort(404)

    if request.method == "GET":
        return render_template("edit.html", reference=reference)

    update_reference(reference_id,
        request.form["title"],
        request.form["authors"],
        request.form["year"],
        request.form["isbn"],
        request.form["publisher"]
    )

    return redirect(url_for("index"))

@app.route("/delete/<int:reference_id>", methods=["GET", "POST"])
def delete_reference(reference_id):
    reference = get_reference(reference_id)

    if not reference:
        abort(404)

    if request.method == "GET":
        return render_template("delete.html", reference=reference)
    
    sql = text("DELETE FROM citations WHERE id = :id")
    db.session.execute(sql, {"id": reference_id})
    db.session.commit()
    return redirect(url_for("index"))

    

if __name__ == "__main__":
    app.run(debug=True)
