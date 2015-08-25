from setuptools import setup, find_packages

def parse_requirements():
    with open('requirements.txt') as f:
        return f.read().splitlines()

setup(
    name = 'runescape',
    version = '0.1.0',
    packages = find_packages(),
    install_requires = parse_requirements(),
    author = 'Kyle Stevenson',
    author_email = 'kyle@kylestevenson.me',
    description = 'This package is a collection of RuneScape utilities.',
    keywords = 'runescape oldschool osrs hiscores utilities',
    license = 'MIT',
    url = 'https://github.com/kylestev/runescape-utils'
)
