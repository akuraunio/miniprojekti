from config import db, app
from sqlalchemy import text
import os
from reference_data import reference_data, reference_fields, ReferenceFieldType


def reset_db():
    print(f"Clearing contents from all tables")

    tables_in_db = tables()
    if len(tables_in_db) > 0:
        print(f"Tables exist, dropping: {', '.join(tables_in_db)}")
        for table in tables_in_db:
            sql = text(f"DROP TABLE {table}")
            db.session.execute(sql)
        db.session.commit()


def tables():
    """Returns all table names from the database except those ending with _id_seq"""
    sql = text(
        "SELECT table_name "
        "FROM information_schema.tables "
        "WHERE table_schema = 'public' "
        "AND table_name NOT LIKE '%_id_seq'"
    )

    result = db.session.execute(sql)
    return [row[0] for row in result.fetchall()]


def setup_db():
    """
    Creating the database
    If database tables already exist, those are dropped before the creation
    """
    tables_in_db = tables()
    if len(tables_in_db) > 0:
        print(f"Tables exist, dropping: {', '.join(tables_in_db)}")
        for table in tables_in_db:
            sql = text(f"DROP TABLE {table}")
            db.session.execute(sql)
        db.session.commit()

    print("Creating database")

    # Read schema from schema.sql file
    schema_path = os.path.join(os.path.dirname(__file__), "schema.sql")
    with open(schema_path, "r") as f:
        schema_sql = f.read().strip()

    additional_sql_parts = []

    for tbl, vals in reference_data.items():
        table_columns = []

        for field, data in vals["fields"].items():
            table_columns.append(
                f"{field.value} {"INT" if reference_fields[field]["type"] == ReferenceFieldType.INT else "TEXT"}{' NOT NULL' if data.get('required') else ''}"
            )

        additional_sql_parts.append(
            f"CREATE TABLE {tbl} (id SERIAL PRIMARY KEY, {', '.join(table_columns)});"
        )

    if additional_sql_parts:
        schema_sql = schema_sql + "\n\n" + "\n\n".join(additional_sql_parts)

    sql = text(schema_sql)
    db.session.execute(sql)
    db.session.commit()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
