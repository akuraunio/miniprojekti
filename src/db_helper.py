from config import db, app
from sqlalchemy import text
from reference_data import (
    reference_fields,
    reference_data,
    ReferenceFieldType,
    ReferenceField,
)


def reset_db():
    print(f"Clearing contents from table Reference")
    sql = text(f"DELETE FROM Reference")
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

    table_column_definitions = []

    for f in ReferenceField:
        sql_type = (
            "INT"
            if reference_fields[f]["type"] == ReferenceFieldType.NUMBER
            else "TEXT"
        )
        table_column_definitions.append(f"{f.value} {sql_type}")

    schema_sql = f"CREATE TABLE Reference (id SERIAL PRIMARY KEY, reference_type TEXT NOT NULL, CHECK (reference_type IN ({', '.join([f"'{t.value}'" for t in reference_data.keys()])})), {', '.join(table_column_definitions)});"

    sql = text(schema_sql)
    db.session.execute(sql)
    db.session.commit()


def search(query):
    sql = text(
        """ 
        SELECT * FROM Reference
        WHERE title ILIKE :query 
            OR author ILIKE :query 
            OR journal ILIKE :query
            OR booktitle ILIKE :query 
            OR publisher ILIKE :query 
            OR note ILIKE :query
            OR CAST(year AS TEXT) ILIKE :query
            OR key_field ILIKE :query
    """
    )
    search_query = f"%{query}%"
    result = db.session.execute(sql, {"query": search_query})
    return result.fetchall()


if __name__ == "__main__":
    with app.app_context():
        setup_db()
