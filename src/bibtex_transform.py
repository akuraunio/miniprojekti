from reference_data import ReferenceField


# Palauttaa yhden reference objektin tiedot stringinä joka on BibTex formaatissa
def reference_to_bibtex(ref):
    field_lines = []

    def _add_field(name, value):
        if value is None or value == "":
            return
        field_lines.append(f"{name} = {{{value}}},\n")

    def _pages(pages_from, pages_to):
        if pages_from is None and pages_to is None:
            return

        if pages_from is None and pages_to is not None:
            _add_field("pages", f"{pages_to}")
        elif pages_to is None:
            _add_field("pages", f"{pages_from}")
        else:
            _add_field("pages", f"{pages_from}--{pages_to}")

    _pages(
        ref.fields.get(ReferenceField.PAGES_FROM),
        ref.fields.get(ReferenceField.PAGES_TO),
    )

    for field_enum, field_value in ref.fields.items():
        if field_enum.value not in ["key", "pages_from", "pages_to"]:
            _add_field(field_enum.value, field_value)

    field_block = "".join(field_lines)
    return f"@{ref.type.value}{{{ref.fields.get(ReferenceField.KEY)},\n{field_block}}}"


# Palauttaa yhden stringin jossa kaikki viittaukset ovat BibTex formaatissa
def references_to_bibtex(references):
    return "\n\n".join(reference_to_bibtex(reference) for reference in references)
