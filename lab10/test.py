import psycopg2
from config import host,user,password,database
 
conn =psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )    
 
cur = conn.cursor()
 
conn.set_session(autocommit=True)

cur.execute("""CREATE TABLE if not exists snake(
            name VARCHAR(255),
            level INTEGER,
            score INTEGER
);
           """)
conn.commit()