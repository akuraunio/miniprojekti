from flask import Flask, request, redirect, url_for, render_template
from repositories import references_repository

app = Flask(__name__)
references = []

@app.route('/')
def index():
    return render_template('index.html', references=references)

@app.route('/add', methods=['POST'])
def add_reference():
    if request.method == 'POST':

        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        references.append({'title': title, 'author': author, 'year': year})
        return redirect(url_for('index'))
    return render_template('add.html')

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
