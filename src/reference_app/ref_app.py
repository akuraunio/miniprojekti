from flask import Flask, request, redirect, url_for, render_template
from repositories.references_repository import get_references, add_new_reference


app = Flask(__name__)


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


if __name__ == "__main__":
    app.run(debug=True)
