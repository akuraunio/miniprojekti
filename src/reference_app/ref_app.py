from config import app, db
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)
references = []

@app.route('/')
def index():
    citations = get_references()
    return render_template("index.html", citations=citations)

@app.route("/new_reference")
def new_reference():
    return render_template("add.html")

@app.route("/add", methods=["POST"])
def add_reference():
    if request.method == 'POST':

        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        references.append({'title': title, 'author': author, 'year': year})
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == "__main__":
    app.run(debug=True)
