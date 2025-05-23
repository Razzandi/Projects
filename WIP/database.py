import sqlite3

class Person:



    def __init__(self, id_number, first, last, age):
        self.id_number = id_number
        self.first = first
        self.last = last
        self.age = age
        self.connection = sqlite3.connect('mydata.db')
        self.cursor = self.connection.cursor()
    
    def load_person(self, id_number):
        self.cursor.execute("""
        SELECT * FROM people
        WHERE id = []
        """.format(id_number))

        results = self.cursor.fetchone()
        self.id_number = id_number
        self.first = results[1]
        self.last = results[2]
        self.age = results[3]
    
    def insert_person(self):
        self.cursor.execute("""
        INSERT INTO people VALUES
        ((), '()', '()', ())
        """.format(self.id_number, self.first, self.last, self.age))
        self.connection.commit()


connection = sqlite3.connect('mydata.db')
cursor = connection.cursor()        

cursor.execute("""
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")

cursor.execute("""
INSERT INTO people VALUES
(1,'Paul', 'Smith', 24),
(2,'Mark', 'Johnson', 42),
(3,'Anna', 'Smith', 34)
""")

cursor.execute("""
SELECT * FROM people
WHERE last_name = 'Smith'
""")

rows = cursor.fetchall()
print(rows)

connection.commit()

connection.close()