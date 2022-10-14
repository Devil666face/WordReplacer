import os
from docxtpl import DocxTemplate
from sysargv import SysArgv
from database import Database


class WordReplacer:
    def __init__(self, argv:SysArgv):
        self.template = DocxTemplate(argv.template_name)

        data_for_context = Database(argv.abs_path).get_data_for_context(argv.template_id)
        self.context = {key[0]:key[1] for key in data_for_context}
        
        self.template.render(self.context)
        self.template.save(argv.output_file_path)
        os.remove(argv.template_name)