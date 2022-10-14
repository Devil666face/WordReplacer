import sqlite3
import uuid
from pathlib import Path

class Database:
    def __init__(self, abs_path, db_file_name='database.db') -> None:
        self.abs_path = abs_path
        self.db = Path(abs_path, db_file_name)
        self.connection = sqlite3.connect(self.db)
        self.cursor = self.connection.cursor()


    def get_data_for_context(self, template_name):
        with self.connect:
            pass


    def save_template_with_random_name(self, template_id):
        with self.connection:
            docx_file_name = f'{uuid.uuid4()}.docx'
            self.cursor.execute('SELECT word FROM Template WHERE id=?', (template_id,))
            with open(Path(self.abs_path,docx_file_name),'wb') as docx_file:
                docx_file.write(self.cursor.fetchone()[0])
        return docx_file_name

    def get_data_for_context(self, template_id):
        with self.connection:
            self.cursor.execute('SELECT tag, value FROM Replace WHERE template_id=?', (template_id,))
        return self.cursor.fetchall()