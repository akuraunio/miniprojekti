from enum import Enum
import os
import sys


# ReferenceFieldType on kaikki kenttätyypit joita viitekentässä voi olla
# Kentät on määritelty html input elementtien mukaan
class ReferenceFieldType(Enum):
    TEXT = "text"
    TEXTAREA = "textarea"
    NUMBER = "number"


# ReferenceType on kaikki viitteiden kentät joita voi olla
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
    PAGES_FROM = "pages_from"
    PAGES_TO = "pages_to"
    PUBLISHER = "publisher"
    SCHOOL = "school"
    SERIES = "series"
    TAG = "tag"
    TITLE = "title"
    TYPE = "type"
    VOLUME = "volume"
    YEAR = "year"


# ReferenceType on kaikki viitetyypit joita voi olla
class ReferenceType(Enum):
    ARTICLE = "article"
    BOOK = "book"
    BOOKLET = "booklet"
    INBOOK = "inbook"
    INPROCEEDINGS = "inproceedings"
    MANUAL = "manual"
    MASTERSTHESIS = "mastersthesis"
    MISC = "misc"
    PHDTHESIS = "phdthesis"
    PROCEEDINGS = "proceedings"
    TECHREPORT = "techreport"
    UNPUBLISHED = "unpublished"


# Määritellään lisätietoja kullekin kentälle, kuten tyyppi ja ui:ssa näkyvä nimi
reference_fields = {
    ReferenceField.KEY: {"type": ReferenceFieldType.TEXT, "name": "Viiteavain"},
    ReferenceField.ADDRESS: {"type": ReferenceFieldType.TEXT, "name": "Osoite"},
    ReferenceField.ANNOTE: {"type": ReferenceFieldType.TEXTAREA, "name": "Annotaatio"},
    ReferenceField.AUTHOR: {"type": ReferenceFieldType.TEXT, "name": "Tekijä"},
    ReferenceField.BOOKTITLE: {"type": ReferenceFieldType.TEXT, "name": "Kirjan nimi"},
    ReferenceField.CHAPTER: {"type": ReferenceFieldType.NUMBER, "name": "Luku"},
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
    ReferenceField.NOTE: {"type": ReferenceFieldType.TEXTAREA, "name": "Merkintä"},
    ReferenceField.NUMBER: {"type": ReferenceFieldType.NUMBER, "name": "Numero"},
    ReferenceField.ORGANIZATION: {
        "type": ReferenceFieldType.TEXT,
        "name": "Organisaatio",
    },
    ReferenceField.PAGES_FROM: {
        "type": ReferenceFieldType.NUMBER,
        "name": "Sivut alkaen",
    },
    ReferenceField.PAGES_TO: {"type": ReferenceFieldType.NUMBER, "name": "Sivut asti"},
    ReferenceField.PUBLISHER: {"type": ReferenceFieldType.TEXT, "name": "Kustantaja"},
    ReferenceField.SCHOOL: {"type": ReferenceFieldType.TEXT, "name": "Koulu"},
    ReferenceField.SERIES: {"type": ReferenceFieldType.TEXT, "name": "Sarja"},
    ReferenceField.TAG: {"type": ReferenceFieldType.TEXT, "name": "Tagi"},
    ReferenceField.TITLE: {"type": ReferenceFieldType.TEXT, "name": "Otsikko"},
    ReferenceField.TYPE: {"type": ReferenceFieldType.TEXT, "name": "Tyyppi"},
    ReferenceField.VOLUME: {"type": ReferenceFieldType.NUMBER, "name": "Vuosikerta"},
    ReferenceField.YEAR: {"type": ReferenceFieldType.NUMBER, "name": "Vuosi"},
}


# Määritellään lisätietoja kullekin viitetyypille
# Esimerkiksi ui:ssa näkyvä nimi ja siihen kuuluvat kentät
reference_data = {
    ReferenceType.ARTICLE: {
        "name": "Artikkeli",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.JOURNAL: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TAG: {"required": True},
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
    ReferenceType.BOOK: {
        "name": "Kirja",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.EDITOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.PUBLISHER: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TAG: {"required": True},
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
    ReferenceType.BOOKLET: {
        "name": "Kirjanen",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.HOWPUBLISHED: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TAG: {"required": True},
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
    ReferenceType.INBOOK: {
        "name": "Artikkeli kokoomateoksessa",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.BOOKTITLE: {"required": True},
            ReferenceField.PUBLISHER: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TAG: {"required": True},
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
    ReferenceType.INPROCEEDINGS: {
        "name": "Artikkeli konferenssijulkaisussa",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.BOOKTITLE: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TAG: {"required": True},
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
    ReferenceType.MANUAL: {
        "name": "Käsikirja",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.TAG: {"required": True},
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
    ReferenceType.MASTERSTHESIS: {
        "name": "Pro gradu -tutkielma",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.SCHOOL: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TAG: {"required": True},
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
    ReferenceType.MISC: {
        "name": "Muu",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.TAG: {"required": True},
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
    ReferenceType.PHDTHESIS: {
        "name": "Väitöskirja",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.SCHOOL: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TAG: {"required": True},
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
    ReferenceType.PROCEEDINGS: {
        "name": "Konferenssijulkaisu",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TAG: {"required": True},
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
    ReferenceType.TECHREPORT: {
        "name": "Tekninen raportti",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.INSTITUTION: {"required": True},
            ReferenceField.YEAR: {"required": True},
            ReferenceField.TAG: {"required": True},
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
    ReferenceType.UNPUBLISHED: {
        "name": "Julkaisematon",
        "fields": {
            ReferenceField.KEY: {"required": True},
            ReferenceField.AUTHOR: {"required": True},
            ReferenceField.TITLE: {"required": True},
            ReferenceField.TAG: {"required": True},
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


# Käytetään testauksessa, ei oikea viitetyyppi
class TestReferenceType(Enum):
    TEST = "test"


# Käytetään testauksessa, ei oikeita viitekenttiä
class TestReferenceField(Enum):
    TEST_TEXT = "test_text"
    TEST_TEXT_REQUIRED = "test_text_required"
    TEST_NUMBER = "test_number"
    TEST_NUMBER_REQUIRED = "test_number_required"
    TEST_TEXTAREA = "test_textarea"
    TEST_TEXTAREA_REQUIRED = "test_textarea_required"

    # Etusivun listassa näkyvät kentät
    TITLE = "title"
    YEAR = "year"
    AUTHOR = "author"
    PAGES_FROM = "pages_from"
    PAGES_TO = "pages_to"
    KEY = "key"


test_reference_fields = {
    TestReferenceField.KEY: {
        "type": ReferenceFieldType.TEXT,
        "name": "Test Key",
    },
    TestReferenceField.TEST_TEXT_REQUIRED: {
        "type": ReferenceFieldType.TEXT,
        "name": "Test Text Required",
    },
    TestReferenceField.TEST_NUMBER: {
        "type": ReferenceFieldType.NUMBER,
        "name": "Test Number",
    },
    TestReferenceField.TEST_NUMBER_REQUIRED: {
        "type": ReferenceFieldType.NUMBER,
        "name": "Test Number Required",
    },
    TestReferenceField.TEST_TEXTAREA: {
        "type": ReferenceFieldType.TEXTAREA,
        "name": "Test Textarea",
    },
    TestReferenceField.TEST_TEXTAREA_REQUIRED: {
        "type": ReferenceFieldType.TEXTAREA,
        "name": "Test Textarea Required",
    },
    TestReferenceField.TITLE: {
        "type": ReferenceFieldType.TEXT,
        "name": "Otsikko",
    },
    TestReferenceField.YEAR: {
        "type": ReferenceFieldType.NUMBER,
        "name": "Vuosi",
    },
    TestReferenceField.AUTHOR: {
        "type": ReferenceFieldType.TEXT,
        "name": "Tekijä",
    },
    TestReferenceField.PAGES_FROM: {
        "type": ReferenceFieldType.NUMBER,
        "name": "Test pages from",
    },
    TestReferenceField.PAGES_TO: {
        "type": ReferenceFieldType.NUMBER,
        "name": "Test pages to",
    },
}

test_reference_data = {
    TestReferenceType.TEST: {
        "name": "Test Reference",
        "fields": {
            TestReferenceField.KEY: {"required": True},
            TestReferenceField.TEST_TEXT: {"required": False},
            TestReferenceField.TEST_TEXT_REQUIRED: {"required": True},
            TestReferenceField.TEST_NUMBER: {"required": False},
            TestReferenceField.TEST_NUMBER_REQUIRED: {"required": True},
            TestReferenceField.TEST_TEXTAREA: {"required": False},
            TestReferenceField.TEST_TEXTAREA_REQUIRED: {"required": True},
            TestReferenceField.TITLE: {"required": False},
            TestReferenceField.AUTHOR: {"required": False},
            TestReferenceField.YEAR: {"required": False},
            TestReferenceField.PAGES_FROM: {"required": False},
            TestReferenceField.PAGES_TO: {"required": False},
        },
    },
}


def set_reference_data(app):
    if os.getenv("USE_TEST_REFERENCE_DATA") == "true":
        app.jinja_env.globals["reference_data"] = test_reference_data
        app.jinja_env.globals["reference_fields"] = test_reference_fields
        app.jinja_env.globals["ReferenceField"] = TestReferenceField
        app.jinja_env.globals["ReferenceType"] = TestReferenceType
        app.jinja_env.globals["ReferenceFieldType"] = ReferenceFieldType

        if "reference_data" in sys.modules:
            sys.modules["reference_data"].reference_data = test_reference_data
            sys.modules["reference_data"].reference_fields = test_reference_fields
            sys.modules["reference_data"].ReferenceField = TestReferenceField
            sys.modules["reference_data"].ReferenceType = TestReferenceType
            sys.modules["reference_data"].ReferenceFieldType = ReferenceFieldType
        return

    app.jinja_env.globals["reference_fields"] = reference_fields
    app.jinja_env.globals["reference_data"] = reference_data
    app.jinja_env.globals["ReferenceField"] = ReferenceField
    app.jinja_env.globals["ReferenceFieldType"] = ReferenceFieldType
    app.jinja_env.globals["ReferenceType"] = ReferenceType
