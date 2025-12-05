class ReferenceToBibtex:
    # Palauttaa yhden stringin jossa kaikki viittaukset ovat BibTex formaatissa
    def references_to_bibtex(self, references, tag=None):
        if tag:
            references = [ref for ref in references if ref.fields.get("tag") == tag]

        return "\n\n".join(
            self.reference_to_bibtex(reference) for reference in references
        )

    # Palauttaa yhden reference objektin tiedot stringinä joka on BibTex formaatissa
    def reference_to_bibtex(self, ref):
        field_lines = []

        key = None
        pages_from = None
        pages_to = None

        # muut kentät lisätään bibtexiin sellaisenaan,
        # paitsi alkusivu ja loppusivu jotka yhdistetään yhdeksi sivuväli -kentäksi
        # ja viitteen avain joka menee bibtex entryn "otsikoksi"
        for field_enum, field_value in ref.fields.items():
            if field_enum.value not in ["key", "pages_from", "pages_to"]:
                self._add_field(field_lines, field_enum.value, field_value)
            elif field_enum.value == "pages_to":
                pages_to = field_value
            elif field_enum.value == "pages_from":
                pages_from = field_value
            elif field_enum.value == "key":
                key = field_value

        self._pages(field_lines, pages_from, pages_to)

        field_block = "".join(field_lines)
        print(ref.fields.get("key"))
        return f"@{ref.type.value}{{{key},\n{field_block}}}"

    def _add_field(self, field_lines, name, value):
        if value is None or value == "":
            return
        field_lines.append(f"{name} = {{{value}}},\n")

    def _pages(self, field_lines, pages_from, pages_to):
        # Alku- ja loppusivu yhdeksi sivuväli kentäksi, jossa sivujen välillä "--""
        # tai pelkästään yksi sivunumero jos toista arvoa ei ole
        if pages_from is None and pages_to is None:
            return

        if pages_from is None and pages_to is not None:
            self._add_field(field_lines, "pages", f"{pages_to}")
        elif pages_to is None:
            self._add_field(field_lines, "pages", f"{pages_from}")
        else:
            self._add_field(field_lines, "pages", f"{pages_from}--{pages_to}")
