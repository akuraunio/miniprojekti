from flask import Flask, request, redirect, url_for, render_template

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

@app.route("/delete/<int:ref_id>", methods=["GET", "POST"])
def delete_reference(ref_id):
    reference = references[ref_id]

    if request.method == "GET":
        return render_template('delete.html', reference=reference, ref_id=ref_id)
    
    if request.method == "POST":
        if "delete" in request.form:
            references.pop(ref_id)
        return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
