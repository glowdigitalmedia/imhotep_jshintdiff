from setuptools import setup, find_packages

setup(
	name='imhotep_jshintdiff',
	version='0.0.1',
	packages=find_packages(),
	url='https://github.com/glowdigitalmedia/imhotep_jshintdiff',
	license='MIT',
	author='Viky Guerra',
	author_email='viky@thisisglow.com',
	description='An imhotep plugin for javascript validation',
	entry_points={
		'imhotep_linters': [
			'.py = imhotep_jshintdiff.plugin:JSHintDiff'
		],
	},
)
