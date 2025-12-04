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
from repositories.tags_repository import get_tag_by_name
from repositories.referencetaglinks_repository import (
    add_new_referencetaglink,
    get_tags_for_reference,
    delete_referencetaglink,
)
from db_helper import reset_db
<<<<<<< HEAD
from bibtex_transform import ReferenceToBibtex
=======
from bibtex_transform import references_to_bibtex
>>>>>>> 217cbb4 (DOI täyttää osan viitteen kenistä ja editor muutettu e ivälttämättömäksi kentäksi (DOI datasta ei löydy monesta viitteestä editoria))
from reference_data import reference_data, ReferenceType, ReferenceField
from validators import _validate_required_fields
import requests
from requests.utils import quote

test_env = os.getenv("TEST_ENV") == "true"


@app.route("/")
def index():
    query = request.args.get("query", "").strip()
    field = request.args.get("field", "").strip()
    tag = request.args.get("tag", "").strip()

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

    tag_names = {
        "kandityö": "Kandidaatintutkielma",
        "gradu": "Pro gradu -tutkielma",
        "väitöskirja": "Väitöskirja",
    }

    if query or field or tag:
        search_results = []

        if tag:
            tag_obj = get_tag_by_name(tag)
            if tag_obj:
                from repositories.referencetaglinks_repository import (
                    get_references_with_tag,
                )

                tag_results = get_references_with_tag(tag_obj.id)
            else:
                tag_results = []
        else:
            tag_results = None

        if query or field:
            text_results = search_references(query, field if field else None)
        else:
            text_results = None

        if tag_results is not None and text_results is not None:
            search_results = [
                ref
                for ref in text_results
                if any(tr.id == ref.id for tr in tag_results)
            ]
        elif tag_results is not None:
            search_results = tag_results
        elif text_results is not None:
            search_results = text_results

        return render_template(
            "index.html",
            search_results=search_results,
            search_query=query,
            search_field=field,
            search_field_name=field_names.get(field, ""),
            search_tag=tag,
            search_tag_name=tag_names.get(tag, ""),
            ReferenceField=ReferenceField,
        )

    references = get_references()
    return render_template(
        "index.html", references=references, ReferenceField=ReferenceField
    )


# Viitteen tyyppi saadaan piilotetuista kentistä lomakkeissa
# get metodissa voi myös käyttää url query parametria
@app.route("/add", methods=["GET", "POST"])
def add():

    reference_type = None
    if request.method == "GET":
        reference_type = request.args.get("type")
    if request.method == "POST":
        reference_type = request.form.get("reference_type")

    if not reference_type or reference_type not in [rt.value for rt in ReferenceType]:
        abort(400, "Virheellinen tai puuttuva viitteen tyyppi")

    reference_type = ReferenceType(reference_type)

    # DOI-haku Crossrefista
    doi = request.args.get("doi")
    prefill_data = {}

    if doi:
        url = f"https://api.crossref.org/works/{quote(doi)}"
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()["message"]

            crossref_to_fields = {
                "title": ReferenceField.TITLE,
                "author": ReferenceField.AUTHOR,
                "publisher": ReferenceField.PUBLISHER,
                "container-title": ReferenceField.JOURNAL,
                "volume": ReferenceField.VOLUME,
                "issue": ReferenceField.NUMBER,
                "page": (ReferenceField.PAGES_FROM, ReferenceField.PAGES_TO),
                "DOI": ReferenceField.DOI,
                "ISSN": ReferenceField.ISSN,
                "ISBN": ReferenceField.ISBN,
                "editor": ReferenceField.EDITOR,
            }

            for key, field in crossref_to_fields.items():
                if key in data:

                    if key == "author":
                        authors = [
                            f"{a.get('given', '')} {a.get('family', '')}".strip()
                            for a in data["author"]
                        ]
                        prefill_data[str(field.value)] = " and ".join(authors)

                    elif key == "editor":
                        editors = [
                            f"{e.get('given', '')} {e.get('family', '')}".strip()
                            for e in data["editor"]
                        ]
                        prefill_data[str(field.value)] = " and ".join(editors)

                    elif key == "page" and isinstance(field, tuple):
                        pages = data["page"].split("-")
                        if len(pages) >= 1:
                            prefill_data[str(field[0].value)] = pages[0].strip()
                        if len(pages) >= 2:
                            prefill_data[str(field[1].value)] = pages[1].strip()

                    else:
                        value = data[key]
                        if isinstance(value, list) and len(value) > 0:
                            value = value[0]
                        prefill_data[str(field.value)] = str(value) if value else ""

            year = None
            if "published-print" in data and data["published-print"].get("date-parts"):
                year = data["published-print"]["date-parts"][0][0]
            elif "published-online" in data and data["published-online"].get(
                "date-parts"
            ):
                year = data["published-online"]["date-parts"][0][0]
            elif "published" in data and data["published"].get("date-parts"):
                year = data["published"]["date-parts"][0][0]

            if year:
                prefill_data[str(ReferenceField.YEAR.value)] = str(year)

    if request.method == "GET":
        return render_template(
            "add.html", reference_type=reference_type, prefill_data=prefill_data
        )
    if request.method == "POST":
        _validate_required_fields(reference_type, request.form)
        fields = {}
        for field in reference_data[reference_type]["fields"]:
<<<<<<< HEAD
            if field.value != "tag":
                value = request.form.get(field.value, "")
                fields[field] = value if value else None

        reference_id = add_new_reference(reference_type, fields)

        tag_name = request.form.get("tag")
        if tag_name:
            tag = get_tag_by_name(tag_name)
            if tag:
                add_new_referencetaglink(reference_id, tag.id)

    return redirect(url_for("index"))
=======
            value = request.form.get(field.value, "")
            fields[field] = value if value else None
        add_new_reference(reference_type, fields)
        return redirect(url_for("index"))
>>>>>>> 217cbb4 (DOI täyttää osan viitteen kenistä ja editor muutettu e ivälttämättömäksi kentäksi (DOI datasta ei löydy monesta viitteestä editoria))


@app.route("/edit/<int:reference_id>", methods=["GET", "POST"])
def edit(reference_id):
    reference = get_reference(reference_id)

    if not reference:
        abort(404)

    if request.method == "GET":
        current_tags = get_tags_for_reference(reference_id)
        reference.current_tag = current_tags[0] if current_tags else None
        return render_template("edit.html", reference=reference)

    _validate_required_fields(reference.type, request.form)

    if request.method == "POST":

        fields = {}
        for field in reference_data[reference.type]["fields"]:
            if field.value != "tag":
                value = request.form.get(field.value, "")
                fields[field] = value if value else None

        update_reference(reference_id, fields)

        current_tags = get_tags_for_reference(reference_id)
        for tag in current_tags:
            delete_referencetaglink(reference_id, tag.id)

        tag_name = request.form.get("tag")
        if tag_name:
            tag = get_tag_by_name(tag_name)
            if tag:
                add_new_referencetaglink(reference_id, tag.id)

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
    bibtex_exporter = ReferenceToBibtex()
    bibtex_reference = bibtex_exporter.references_to_bibtex(references)
    return render_template("bibtex.html", bibtex_reference=bibtex_reference)


@app.route("/bibtex/download")
def bibtex_download():
    references = get_references()
    bibtex_exporter = ReferenceToBibtex()
    bibtex_reference = bibtex_exporter.references_to_bibtex(references)
    return Response(
        bibtex_reference,
        mimetype="text/plain",
        headers={"Content-Disposition": "attachment; filename=references.bib"},
    )


if test_env:

    @app.route("/reset_db")
    def reset_database():
        reset_db()
        return "OK"


if __name__ == "__main__":
    app.run(debug=True)
