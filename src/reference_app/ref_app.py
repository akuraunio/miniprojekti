from config import app, db
from flask import Flask, request, redirect, url_for, render_template
from repositories.references_repository import get_references, add_new_reference

@app.route("/")
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


@app.route('/edit/<int:reference_id>', methods=['POST'])
def edit_reference(reference_id):
    reference = references_repository.get_reference(reference_id)

    if not reference:
        abort(404)

    reference["title"] = request.form["title"]
    reference["authors"] = request.form["authors"]
    reference["year"] = request.form["year"]
    reference["isbn"] = request.form["isbn"]
    reference["publisher"] = request.form["publisher"]

    return redirect("/reference/" + str(reference_id))

if __name__ == "__main__":
    app.run(debug=True)
