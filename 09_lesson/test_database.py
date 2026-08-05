from sqlalchemy import create_engine, text


db_connection_string = "postgresql://postgres:qqq@localhost:5432/QA"
db = create_engine(db_connection_string)


def test_insert():
    connection = db.connect()
    transaction = connection.begin()

    sql_statement = text("insert into subject(\"subject_title\") values (:ns)")
    params = {
        'ns': 'Psychologia'
    }
    connection.execute(sql_statement, params)

    sql = "select * from subject where subject_title = 'Psychologia'"
    result = connection.execute(text(sql))
    assert result.rowcount == 1

    transaction.rollback()
    connection.close()


def test_update():
    connection = db.connect()
    transaction = connection.begin()

    sql_statement = text("insert into subject(\"subject_title\") values (:ns)")
    params = {
        'ns': 'Psychologia'
    }
    connection.execute(sql_statement, params)

    sql = "UPDATE subject SET subject_id = :id WHERE subject_title = :name"
    connection.execute(text(sql), {"id": 20, "name": "Psychologia"})

    sql_text = "select * from subject where subject_title = 'Psychologia'"
    result = connection.execute(text(sql_text))
    rows = result.mappings().all()
    row1 = rows[0]
    assert row1["subject_id"] == 20

    transaction.rollback()
    connection.close()


def test_delete():
    connection = db.connect()
    transaction = connection.begin()

    sql_statement = text("insert into subject(\"subject_title\") values (:ns)")
    params = {
        'ns': 'Psychologia'
    }
    connection.execute(sql_statement, params)

    sql = "select * from subject where subject_title = 'Psychologia'"
    result = connection.execute(text(sql))
    assert result.rowcount == 1

    sql_del = text("DELETE FROM subject WHERE subject_title = 'Psychologia'")
    connection.execute(sql_del)
    result = connection.execute(text(sql))
    assert result.rowcount == 0

    transaction.commit()
    connection.close()
