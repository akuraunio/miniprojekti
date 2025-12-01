import os
from flask import request, redirect, url_for, render_template, abort, Response
from config import app
from repositories.references_repository import (
    get_references,
    add_new_reference,
    update_reference,
    get_reference,
    delete_reference,
    search_references,
)
from db_helper import reset_db
from bibtex_transform import references_to_bibtex
from reference_data import (
    reference_data,
    reference_fields,
    ReferenceType,
    ReferenceFieldType,
    TestReferenceType,
    test_reference_data,
    test_reference_fields,
)

test_env = os.getenv("TEST_ENV") == "true"


@app.route("/")
def index():
    query = request.args.get("query", "").strip()
    field = request.args.get("field", "").strip()

    field_names = {
        "title": "Otsikko",
        "author": "Tekijä",
        "year": "Vuosi",
        "journal": "Lehti",
        "booktitle": "Kirjan nimi",
        "publisher": "Kustantaja",
        "editor": "Toimittaja",
        "school": "Koulu",
        "organization": "Organisaatio",
        "key": "Viiteavain",
        "note": "Huomautus",
    }

    if query or field:
        search_results = search_references(query, field if field else None)
        return render_template(
            "index.html",
            search_results=search_results,
            search_query=query,
            search_field=field,
            search_field_name=field_names.get(field, ""),
        )

    references = get_references()
    return render_template("index.html", references=references)


# Viitteen tyyppi saadaan piilotetuista kentistä lomakkeissa
# get metodissa voi myös käyttää url query parametria
@app.route("/add", methods=["POST", "GET"])
def add():
    reference_type = None

    if request.method == "GET":
        reference_type = request.args.get("type")
    if request.method == "POST":
        reference_type = request.form.get("reference_type")

    if not reference_type or reference_type not in [rt.value for rt in ReferenceType]:
        abort(400, "Virheellinen tai puuttuva viitteen tyyppi")
    reference_type = ReferenceType(reference_type)

    if request.method == "GET":
        return render_template("add.html", reference_type=reference_type)

    if request.method == "POST":
        _validate_required_fields(reference_type, request.form)

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

    _validate_required_fields(reference.type, request.form)

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


# routet bibtex-näkymälle ja lataukselle
@app.route("/bibtex")
def bibtex():
    references = get_references()
    bibtex_reference = references_to_bibtex(references)
    return render_template("bibtex.html", bibtex_reference=bibtex_reference)


@app.route("/bibtex/download")
def bibtex_download():
    references = get_references()
    bibtex_reference = references_to_bibtex(references)
    return Response(
        bibtex_reference,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment; filename=references.bib"},
    )

# validointien apufunktiot
def _validate_required(field_name, field_value, required):
    if required and not field_value:
        abort(400, f"Täytä kaikki pakolliset kentät: {field_name}")

def _validate_number(field_name, field_value):
    value = str(field_value).strip()
    if not value.lstrip("-").isdigit():
        abort(400,f"{field_name} täytyy olla numero")

    if int(value) < 0:
        abort(400, "Vuosi ei voi olla negatiivinen")

def _validate_text(field_value, field_name):
    if not any(char.isalnum()for char in field_value):
        abort(400,f"{field_name} ei voi sisältää vain erikoismerkkejä")

def _validate_single_field(field_name, field_type, field_value):
    if field_type == ReferenceFieldType.NUMBER:
        _validate_number(field_name, field_value)

    if field_type in (ReferenceFieldType.TEXT, ReferenceFieldType.TEXTAREA):
        _validate_text(field_value, field_name)

# viitteiden kenttien validointi
def _validate_required_fields(reference_type, form):
    if isinstance(reference_type, TestReferenceType):
        data_dict = test_reference_data
        fields_dict = test_reference_fields
    else:
        data_dict = reference_data
        fields_dict = reference_fields
  
    for field, meta in data_dict[reference_type]["fields"].items():
        field_value = form.get(field.value)
        field_name = fields_dict[field]["name"]
        field_type = fields_dict[field]["type"]

        _validate_required(field_name, field_value, meta["required"])

        if not field_value:
            continue

        _validate_single_field(field_name, field_type, field_value)

if test_env:

    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return "OK"


if __name__ == "__main__":
    app.run(debug=True)
