from enum import Enum


class ReferenceFieldType(Enum):
    TEXT = "text"
    LONG_TEXT = "long_text"
    INT = "int"


class ReferenceField(Enum):
    KEY = "key"
    ADDRESS = "address"
    ANNOTE = "annote"
    AUTHOR = "author"
    BOOKTITLE = "booktitle"
    CHAPTER = "chapter"
    CROSSREF = "crossref"
    EDITION = "edition"
    DOI = "doi"
    ISSN = "issn"
    ISBN = "isbn"
    EDITOR = "editor"
    EMAIL = "email"
    HOWPUBLISHED = "howpublished"
    INSTITUTION = "institution"
    JOURNAL = "journal"
    MONTH = "month"
    NOTE = "note"
    NUMBER = "number"
    ORGANIZATION = "organization"
    PAGES_FROM = "pagesFrom"
    PAGES_TO = "pagesTo"
    PUBLISHER = "publisher"
    SCHOOL = "school"
    SERIES = "series"
    TITLE = "title"
    TYPE = "type"
    VOLUME = "volume"
    YEAR = "year"


reference_fields = {
    ReferenceField.KEY: {"type": ReferenceFieldType.TEXT, "name": "Viiteavain"},
    ReferenceField.ADDRESS: {"type": ReferenceFieldType.TEXT, "name": "Osoite"},
    ReferenceField.ANNOTE: {"type": ReferenceFieldType.LONG_TEXT, "name": "Huomautus"},
    ReferenceField.AUTHOR: {"type": ReferenceFieldType.TEXT, "name": "Tekijä"},
    ReferenceField.BOOKTITLE: {"type": ReferenceFieldType.TEXT, "name": "Kirjan nimi"},
    ReferenceField.CHAPTER: {"type": ReferenceFieldType.INT, "name": "Luku"},
    ReferenceField.CROSSREF: {
        "type": ReferenceFieldType.TEXT,
        "name": "Ristiinviittaus",
    },
    ReferenceField.EDITION: {"type": ReferenceFieldType.TEXT, "name": "Painos"},
    ReferenceField.DOI: {"type": ReferenceFieldType.TEXT, "name": "DOI"},
    ReferenceField.ISSN: {"type": ReferenceFieldType.TEXT, "name": "ISSN"},
    ReferenceField.ISBN: {"type": ReferenceFieldType.TEXT, "name": "ISBN"},
    ReferenceField.EDITOR: {"type": ReferenceFieldType.TEXT, "name": "Toimittaja"},
    ReferenceField.EMAIL: {"type": ReferenceFieldType.TEXT, "name": "Sähköposti"},
    ReferenceField.HOWPUBLISHED: {
        "type": ReferenceFieldType.TEXT,
        "name": "Julkaisumuoto",
    },
    ReferenceField.INSTITUTION: {
        "type": ReferenceFieldType.TEXT,
        "name": "Organisaatio",
    },
    ReferenceField.JOURNAL: {"type": ReferenceFieldType.TEXT, "name": "Lehti"},
    ReferenceField.MONTH: {"type": ReferenceFieldType.TEXT, "name": "Kuukausi"},
    ReferenceField.NOTE: {"type": ReferenceFieldType.LONG_TEXT, "name": "Huomautus"},
    ReferenceField.NUMBER: {"type": ReferenceFieldType.INT, "name": "Numero"},
    ReferenceField.ORGANIZATION: {
        "type": ReferenceFieldType.TEXT,
        "name": "Organisaatio",
    },
    ReferenceField.PAGES_FROM: {"type": ReferenceFieldType.INT, "name": "Sivut alkaen"},
    ReferenceField.PAGES_TO: {"type": ReferenceFieldType.INT, "name": "Sivut asti"},
    ReferenceField.PUBLISHER: {"type": ReferenceFieldType.TEXT, "name": "Kustantaja"},
    ReferenceField.SCHOOL: {"type": ReferenceFieldType.TEXT, "name": "Koulu"},
    ReferenceField.SERIES: {"type": ReferenceFieldType.TEXT, "name": "Sarja"},
    ReferenceField.TITLE: {"type": ReferenceFieldType.TEXT, "name": "Otsikko"},
    ReferenceField.TYPE: {"type": ReferenceFieldType.TEXT, "name": "Tyyppi"},
    ReferenceField.VOLUME: {"type": ReferenceFieldType.INT, "name": "Vuosikerta"},
    ReferenceField.YEAR: {"type": ReferenceFieldType.INT, "name": "Vuosi"},
}

reference_data = {
    "article": {
        "name": "Artikkeli",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.JOURNAL: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.VOLUME: {"required": False},
            ReferenceField.NUMBER: {"required": False},
            ReferenceField.PAGES_FROM: {"required": False},
            ReferenceField.PAGES_TO: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
    "book": {
        "name": "Kirja",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.EDITOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.PUBLISHER: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.VOLUME: {"required": False},
            ReferenceField.NUMBER: {"required": False},
            ReferenceField.PAGES_FROM: {"required": False},
            ReferenceField.PAGES_TO: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
    "booklet": {
        "name": "Kirjanen",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.HOWPUBLISHED: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.EDITOR: {"required": False},
            ReferenceField.VOLUME: {"required": False},
            ReferenceField.NUMBER: {"required": False},
            ReferenceField.SERIES: {"required": False},
            ReferenceField.ORGANIZATION: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
    "inbook": {
        "name": "Artikkeli kokoomateoksessa",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.BOOKTITLE: {"required": True},
            ReferenceField.PUBLISHER: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.EDITOR: {"required": False},
            ReferenceField.VOLUME: {"required": False},
            ReferenceField.NUMBER: {"required": False},
            ReferenceField.SERIES: {"required": False},
            ReferenceField.ADDRESS: {"required": False},
            ReferenceField.PAGES_FROM: {"required": False},
            ReferenceField.PAGES_TO: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
    "inproceedings": {
        "name": "Artikkeli konferenssijulkaisussa",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.BOOKTITLE: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.EDITOR: {"required": False},
            ReferenceField.VOLUME: {"required": False},
            ReferenceField.NUMBER: {"required": False},
            ReferenceField.SERIES: {"required": False},
            ReferenceField.ADDRESS: {"required": False},
            ReferenceField.PAGES_FROM: {"required": False},
            ReferenceField.PAGES_TO: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.ORGANIZATION: {"required": False},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
    "manual": {
        "name": "Käsikirja",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.AUTHOR: {"required": False},
            ReferenceField.ORGANIZATION: {"required": False},
            ReferenceField.EDITION: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
    "mastersthesis": {
        "name": "Pro gradu -tutkielma",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.SCHOOL: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TYPE: {"required": False},
            ReferenceField.ADDRESS: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
    "misc": {
        "name": "Muu",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.AUTHOR: {"required": False},
            ReferenceField.HOWPUBLISHED: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.YEAR: {"required": False},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
    "phdthesis": {
        "name": "Väitöskirja",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.SCHOOL: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TYPE: {"required": False},
            ReferenceField.ADDRESS: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
    "proceedings": {
        "name": "Konferenssijulkaisu",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.EDITOR: {"required": False},
            ReferenceField.VOLUME: {"required": False},
            ReferenceField.NUMBER: {"required": False},
            ReferenceField.SERIES: {"required": False},
            ReferenceField.ADDRESS: {"required": False},
            ReferenceField.PUBLISHER: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
    "techreport": {
        "name": "Tekninen raportti",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.INSTITUTION: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TYPE: {"required": False},
            ReferenceField.NUMBER: {"required": False},
            ReferenceField.ADDRESS: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
    "unpublished": {
        "name": "Julkaisematon",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.NOTE: {"required": False},
            ReferenceField.ANNOTE: {"required": False},
            ReferenceField.MONTH: {"required": False},
            ReferenceField.YEAR: {"required": False},
            ReferenceField.DOI: {"required": False},
            ReferenceField.ISSN: {"required": False},
            ReferenceField.ISBN: {"required": False},
        },
    },
}
