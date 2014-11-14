import os

from imhotep.tools import Tool


class JSHintDiff(Tool):

    def __init__(self, *args, **kwargs):
        super(JSHintDiff, self).__init__(*args, **kwargs)
        self.linter = 'jshint'
        self.config = '.jscsrc'
        self.extension = 'js'

    def format_linter_output(self, repo_dir, linter_output, linter_errors):
        """ Returns a dict of linter errors """
        for line in linter_output:
            path, line, column, message = line.split(':')
            file_name = os.path.abspath(path)
            file_name = file_name.replace(repo_dir, '')[1:]
            linter_errors[str(file_name)][line].append(message.lstrip(' '))
        return linter_errors
