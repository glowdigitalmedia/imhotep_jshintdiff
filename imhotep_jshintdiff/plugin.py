import re

from imhotep.tools import Tool


class JSHintDiff(Tool):

    def __init__(self, *args, **kwargs):
        super(JSHintDiff, self).__init__(*args, **kwargs)
        self.linter = 'jshint'
        self.config = '.jscsrc'
        self.extension = 'js'
        self.regex = re.compile(
            r'(?P<filename>.*): line (?P<line_num>\d+), col \d+, (?P<message>.*)'
        )

    def format_linter_output(self, repo_dir, linter_output, linter_errors):
        """ Returns a dict of linter errors """
        for line in linter_output:
            match = self.regex.search(line)
            if match is not None:
                filename = match.group('filename')[len(repo_dir) + 1:]
                linter_errors[filename][match.group('line_num')].append(
                    match.group('message')
                )
        return linter_errors
