from flask import request, redirect, url_for, render_template, abort
from config import app
from repositories.references_repository import (
    get_references,
    add_new_reference,
    update_reference,
    get_reference,
    delete_reference,
)
from reference_data import reference_data, ReferenceType
import os
from db_helper import reset_db

test_env = os.getenv("TEST_ENV") == "true"


@app.route("/")
def index():
    references = get_references()
    return render_template("index.html", references=references)


# Viitteen tyyppi saadaan piilotetuista kentistä lomakkeissa, get metodissa voi myös käyttää url query parametria. Jos tyyppi puuttuu tai on virheellinen, sovellus kaatuu, korjataan myöhemmin :D
@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "GET":
        reference_type = ReferenceType(request.args.get("type"))

        return render_template("add.html", reference_type=reference_type)

    if request.method == "POST":
        reference_type = ReferenceType(request.form.get("reference_type"))

        fields = {}
        for field in reference_data[reference_type]["fields"]:
            value = request.form.get(field.value, "")

            fields[field] = value if value else None

        add_new_reference(reference_type, fields)

    return redirect(url_for("index"))


@app.route("/edit/<int:reference_id>", methods=["GET", "POST"])
def edit(reference_id):
    reference = get_reference(reference_id)

    if not reference:
        abort(404)

    if request.method == "GET":
        return render_template("edit.html", reference=reference)

    if request.method == "POST":
        fields = {}
        for field in reference_data[reference.type]["fields"]:
            value = request.form.get(field.value, "")

            fields[field] = value if value else None

        update_reference(reference_id, fields)

    return redirect(url_for("index"))


@app.route("/delete/<int:reference_id>", methods=["GET", "POST"])
def delete(reference_id):
    reference = get_reference(reference_id)
    if not reference:
        abort(404)

    if request.method == "GET":
        return render_template("delete.html", reference=reference)

    if request.method == "POST":
        delete_reference(reference_id)

    return redirect(url_for("index"))


if test_env:

    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return "OK"

if __name__ == "__main__":
    app.run(debug=True)
