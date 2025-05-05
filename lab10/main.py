import psycopg2
from config import host,database,user, password
import logging

connection = psycopg2.connect(
    host = host,
    database =  database,
    user = user,
    password = password
)

print(connection)


sql_create_query = """CREATE TABLE IF NOT EXISTS account (
      account_id INT PRIMARY KEY,
      iin VARCHAR(255) NOT NULL,
      balance VARCHAR(255) NOT NULL, 
      created_at VARCHAR(255) NOT NULL
)
"""

sql_insert_query = """
    INSERT INTO  account(
        account_id,
        iin,
        balance, 
        created_at

    ) VALUES(
        2,'dsaffsd','fdsfg','asdfd'
    )

"""

sql_update_query = """
    UPDATE Customer set name = 'Adidas' where id = 1
"""


sql_select_query = """
    SELECT * FROM Customer
"""


pointer = connection.cursor()




try:
    # pointer.execute(sql_create_query)
    # pointer.execute(sql_insert_query)
    pointer.execute(sql_select_query)
    rows = pointer.fetchall()       #  Retrieve all rows of a result from a SELECT query.
    # for x in rows:
    #     print(x)
    print(rows)
    connection.commit()
    logging.info("DATA IS INSERTED")
except Exception as e:
    logging.error(" Error occurred: %s", e)

finally:
    connection.close()
