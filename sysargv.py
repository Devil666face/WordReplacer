import sys
from database import Database


class SysArgv:
    def __init__(self, argv):
        self.abs_path = argv[0]
        self.template_id = argv[1]
        self.template_name = self.save_word_template_from_db(self.template_id)
        self.output_file_path = argv[2]


    def save_word_template_from_db(self, template_id):
        return Database(self.abs_path).save_template_with_random_name(template_id)


    def __str__(self):
        return ''.join(f'{key}={self.__dict__[key]}\n' for key in self.__dict__)