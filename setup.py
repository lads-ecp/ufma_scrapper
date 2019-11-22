
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
  name = 'ufma_scrapper',       
  packages = ['ufma_scrapper'],   # Chose the same as "name"
  version = '0.0.10',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'TYPE YOUR DESCRIPTION HERE',   # Give a short description about your library
  author = 'Sérgio Souza Costa',                   # Type in your name
  author_email = 'profsergiocosta@gmail.com',      # Type in your E-Mail
 long_description = long_description ,
 long_description_content_type = "text/markdown",
url = 'https://github.com/inovacampus/ufma_scrapper',   # Provide either the link to your github or to your website
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
   install_requires=[
          'requests',
          'bs4',
          'lxml',
          'unidecode'
        'pymarc',
    ],
   classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
