from ref_app import app
from reference_data import (
    reference_fields,
    reference_data,
    ReferenceField,
    ReferenceFieldType,
    ReferenceType,
)

if __name__ == "__main__":
    app.jinja_env.globals["reference_fields"] = reference_fields
    app.jinja_env.globals["reference_data"] = reference_data
    app.jinja_env.globals["ReferenceField"] = ReferenceField
    app.jinja_env.globals["ReferenceFieldType"] = ReferenceFieldType
    app.jinja_env.globals["ReferenceType"] = ReferenceType

    app.run(port=5001, host="0.0.0.0", debug=True)
