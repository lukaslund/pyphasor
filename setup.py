from setuptools import setup, find_packages

setup(
	name='pyphasor',
	version='1.0.0',
	description='Phasors in Python',
	url='https://github.com/lukaslund/pyphasor',
	author='Lukas Lund',
	packages=find_packages(include=['pyphasor']),
	install_requires=[
		'numpy',
	],
)
