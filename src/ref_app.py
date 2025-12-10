import os
from flask import request, redirect, url_for, render_template, abort, Response
import requests
from requests.utils import quote
from config import app
from repositories.references_repository import (
    get_references,
    add_new_reference,
    update_reference,
    get_reference,
    delete_reference,
    search_references,
)
from repositories.referencetaglinks_repository import (
    add_new_referencetaglink,
    get_tags_for_reference,
    delete_referencetaglink,
    get_references_with_tags,
)
from repositories.tags_repository import (
    get_tag_by_name,
    get_tags,
)
from db_helper import reset_db
from bibtex_transform import ReferenceToBibtex
from reference_data import reference_data, ReferenceType, ReferenceField
from validators import _validate_required_fields


test_env = os.getenv("TEST_ENV") == "true"


def crossref_author_or_editor(data, key):  # pragma: no cover
    if key not in data:
        return ""
    persons = [
        f"{person.get('given', '')} {person.get('family', '')}".strip()
        for person in data[key]
    ]
    return " and ".join(persons) if persons else None


def crossref_pages(page_string):
    pages = page_string.split("-")
    pages_from = pages[0].strip() if len(pages) >= 1 else None
    pages_to = pages[1].strip() if len(pages) >= 2 else None
    return pages_from, pages_to


def crossref_year(data):
    date_fields = ["published-print", "published-online", "published"]
    for field in date_fields:
        if field in data and data[field].get("date-parts"):
            return str(data[field]["date-parts"][0][0])
    return ""


def doi_data(doi):
    """Fetch reference data from Crossref API using DOI."""
    url = f"https://api.crossref.org/works/{quote(doi)}"
    try:
        r = requests.get(url, timeout=5)
        if r.status_code == 200:
            return r.json()["message"]
    except (requests.RequestException, KeyError):
        pass
    return {}


def edit_data(reference_id):
    reference = get_reference(reference_id)
    if reference:
        prefill_data = {}
        for field, value in reference.fields.items():
            if value is not None:
                prefill_data[str(field.value)] = str(value)
        return prefill_data
    return {}


def process_field(data, key, field, prefill_data):
    if key not in data:
        return
    value = data[key]
    if isinstance(value, list) and len(value) > 0:
        value = value[0]
    if value:
        prefill_data[str(field.value)] = str(value)


def crossref_data(data):
    prefill_data = {}

    crossref_to_fields = {
        "title": ReferenceField.TITLE,
        "publisher": ReferenceField.PUBLISHER,
        "container-title": ReferenceField.JOURNAL,
        "volume": ReferenceField.VOLUME,
        "issue": ReferenceField.NUMBER,
        "DOI": ReferenceField.DOI,
        "ISSN": ReferenceField.ISSN,
        "ISBN": ReferenceField.ISBN,
    }

    for key, field in crossref_to_fields.items():
        process_field(data, key, field, prefill_data)

    author = crossref_author_or_editor(data, "author")
    if author:
        prefill_data[str(ReferenceField.AUTHOR.value)] = author

    editor = crossref_author_or_editor(data, "editor")
    if editor:
        prefill_data[str(ReferenceField.EDITOR.value)] = editor

    if "page" in data:
        pages_from, pages_to = crossref_pages(data["page"])
        if pages_from:
            prefill_data[str(ReferenceField.PAGES_FROM.value)] = pages_from
        if pages_to:
            prefill_data[str(ReferenceField.PAGES_TO.value)] = pages_to

    year = crossref_year(data)
    if year:
        prefill_data[str(ReferenceField.YEAR.value)] = year

    return prefill_data


def _get_field_names():
    """Get mapping of field names to their display names."""
    return {
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


def _get_tag_names():
    """Get mapping of tag names to their display names."""
    return {
        "kandityö": "Kandidaatintutkielma",
        "gradu": "Pro gradu -tutkielma",
        "väitöskirja": "Väitöskirja",
    }


def _perform_search(query, field, tag):
    """Perform search based on query, field, and tag parameters."""
    tag_results = None
    if tag:
        tag_obj = get_tag_by_name(tag)
        tag_results = get_references_with_tags([tag_obj.id]) if tag_obj else []

    text_results = None
    if query or field:
        text_results = search_references(query, field if field else None)

    result = []
    if tag_results is not None and text_results is not None:
        result = [
            ref for ref in text_results if any(tr.id == ref.id for tr in tag_results)
        ]
    elif tag_results is not None:
        result = tag_results
    elif text_results is not None:
        result = text_results

    return result


@app.route("/")
def index():
    query = request.args.get("query", "").strip()
    field = request.args.get("field", "").strip()
    tag = request.args.get("tag", "").strip()

    field_names = _get_field_names()
    tag_names = _get_tag_names()

    if query or field or tag:
        search_results = _perform_search(query, field, tag)
        for reference in search_results:
            reference.tags = get_tags_for_reference(reference.id)
        return render_template(
            "index.html",
            search_results=search_results,
            search_query=query,
            search_field=field,
            search_field_name=field_names.get(field, ""),
            search_tag=tag,
            search_tag_name=tag_names.get(tag, ""),
            tag_names=tag_names,
        )

    # Lisätään viitelistaan tägit
    references = get_references()
    for reference in references:
        reference.tags = get_tags_for_reference(reference.id)

    return render_template(
        "index.html",
        references=references,
        tag_names=tag_names,
    )


def _get_reference_type():
    """Get and validate reference type from request."""
    reference_type = None
    if request.method == "GET":
        reference_type = request.args.get("type")
    elif request.method == "POST":
        reference_type = request.form.get("reference_type")

    if not reference_type or reference_type not in [rt.value for rt in ReferenceType]:
        abort(400, "Virheellinen tai puuttuva viitteen tyyppi")

    return ReferenceType(reference_type)


def _get_prefill_data(reference_id=None, doi=None):
    """Get prefill data from DOI or reference ID."""
    if doi:
        data = doi_data(doi)
        if data:
            return crossref_data(data)
    elif reference_id:
        return edit_data(reference_id)
    return {}


def _process_add_form(reference_type):
    """Process the add form submission."""
    _validate_required_fields(reference_type, request.form)

    fields = {}
    for field in reference_data[reference_type]["fields"]:
        if field.value != "tag":
            value = request.form.get(field.value, "")
            fields[field] = value if value else None

    reference_id = add_new_reference(reference_type, fields)

    tag_names = request.form.getlist("tag")
    if tag_names:
        for tag_name in tag_names:
            tag = get_tag_by_name(tag_name)
            if tag:
                add_new_referencetaglink(reference_id, tag.id)


# Viitteen tyyppi saadaan piilotetuista kentistä lomakkeissa
# get metodissa voi myös käyttää url query parametria
@app.route("/add", methods=["GET", "POST"])
def add():
    reference_type = _get_reference_type()
    prefill_data = _get_prefill_data(doi=request.args.get("doi"))
    tag_names = _get_tag_names()

    if request.method == "GET":
        return render_template(
            "add.html",
            reference_type=reference_type,
            prefill_data=prefill_data,
            tag_names=tag_names,
        )

    if request.method == "POST":
        _process_add_form(reference_type)
        return redirect(url_for("index"))

    return abort(405)


def collect_fields(reference_type, form):
    fields = {}
    for field in reference_data[reference_type]["fields"]:
        value = form.get(field.value, "")
        fields[field] = value if value else None
    return fields


def _process_edit_form(reference_id, reference):
    """Process the edit form submission."""
    _validate_required_fields(reference.type, request.form)

    # Collect fields excluding tag (merge both approaches)
    fields = collect_fields(reference.type, request.form)

    # Update reference with collected fields
    update_reference(reference_id, fields)

    # Remove existing tags
    current_tags = get_tags_for_reference(reference_id)
    for tag in current_tags:
        delete_referencetaglink(reference_id, tag.id)

    # Add new tags if provided
    tag_names = request.form.getlist("tag")
    if tag_names:
        for tag_name in tag_names:
            tag = get_tag_by_name(tag_name)
            if tag:
                add_new_referencetaglink(reference_id, tag.id)


@app.route("/edit/<int:reference_id>", methods=["GET", "POST"])
def edit(reference_id):
    reference = get_reference(reference_id)

    if not reference:
        abort(404)

    tag_names = _get_tag_names()

    if request.method == "GET":
        current_tags = get_tags_for_reference(reference_id)
        reference.current_tags = current_tags
        prefill_data = _get_prefill_data(reference_id=reference_id)
        return render_template(
            "edit.html",
            reference=reference,
            prefill_data=prefill_data,
            tag_names=tag_names,
        )

    _process_edit_form(reference_id, reference)
    return redirect(url_for("index"))


@app.route("/delete/<int:reference_id>", methods=["POST"])
def delete(reference_id):
    reference = get_reference(reference_id)
    if not reference:
        abort(404)

    delete_reference(reference_id)

    return redirect(url_for("index"))


# routet bibtex-näkymälle ja lataukselle
@app.route("/bibtex")
def bibtex():
    selected_tags = request.args.getlist("tags")
    tag_names = _get_tag_names()

    if selected_tags:
        references = get_references_with_tags(selected_tags)
    else:
        references = get_references()

    all_tags = get_tags()

    bibtex_exporter = ReferenceToBibtex()
    bibtex_reference = bibtex_exporter.references_to_bibtex(references)
    return render_template(
        "bibtex.html",
        bibtex_reference=bibtex_reference,
        tags=all_tags,
        selected_tags=selected_tags,
        tag_names=tag_names,
    )


@app.route("/bibtex/download")
def bibtex_download():
    selected_tags = request.args.getlist("tags")

    if selected_tags:
        references = get_references_with_tags(selected_tags)
    else:
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
