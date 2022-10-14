import sqlite3


class Database:
    def __init__(self, db_file_name='database.db') -> None:
        self.db = db_file_name
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()
        self.cursor.execute('PRAGMA foreign_keys=1')
        
    def insert_template(self):
        name = 'Инструкция'

        with open('Инструкция.docx', 'rb') as word_file:
            word=word_file.read()

        with self.connection:
            self.cursor.execute(f"INSERT INTO Template (name, word) VALUES (?, ?)", (name, word, ))
        self.connection.commit()

    def insert_replace(self, template_id, label, tag, value):
        with self.connection:
            self.cursor.execute(f"INSERT INTO Replace (template_id, label, tag, value) VALUES (?, ?, ?, ?)", (template_id, label, tag, value))

        self.connection.commit()

if __name__=='__main__':
    db = Database()
    # db.insert_template()
    # db.insert_replace(24,'имя','name','Иван Иванов')
    # db.insert_replace(24,'телефон','phone','77777777777')
    # db.insert_replace(24,'имя','date','02.02.2028')