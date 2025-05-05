import psycopg2
from config import host,database,user, password

connection = psycopg2.connect(
    host = host,
    database =  database,
    user = user,
    password = password
)


print(connection)




sql_query = """ 
    CREATE TABLE Customer(
        ID INT PRIMARY KEY NOT NULL,
        NAME VARCHAR(10),
        AGE INT NOT NULL,
        ADDRESS CHAR(20)
        )
"""



pointer = connection.cursor()
pointer.execute(sql_query)
connection.commit()
print("Table is created")