from imhotep.tools import Tool
from collections import defaultdict
import json
import os


class JSHintDiff(Tool):
	def invoke(self, dirname, filenames=set(), linter_configs=set()):
		retval = defaultdict(lambda: defaultdict(list))
		config = ''
		for config_file in linter_configs:
			config = '--config=%s ' % config_file
		if len(filenames) == 0:
			print 'No files to lint'
			return retval
		else:
			files = []
			for filename in filenames:
				if '.js' in filename:
					files.append('%s/%s' % (dirname, filename))

			cmd = 'jshint %s %s' % (config, ' '.join(files))
		try:
			output = self.executor(cmd)
			for line in output.split('\n'):
				path, line, column, message = line.split(':')
				file_name = os.path.abspath(path)
				file_name = file_name.replace(dirname, '')[1:]
				retval[str(file_name)][line].append(message.lstrip(' '))
		except:
			pass
		return retval
