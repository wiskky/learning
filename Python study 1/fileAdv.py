import os #from scandir
#"""
#Always using scandir in the below examples.
entry = os.listdir('C:/Users/pc/gitdoc/git')
for entries in entry:
    print(entries)
"""
"""""""""""""""""""""""""""""""*****,,,,,*******
with os.scandir('C:/Users/pc/gitdoc/') as entries:
    for entry in entries:
        print(entry.name)
"""
""",,,,,""""""""""
from pathlib import Path

entries = Path('C:/Users/pc/gitdoc/')
for entry in entries.iterdir():
    print(entry.name)
"""
"""
#Fro m now we will be using only scandir as our example

# List all files in a directory using scandir()
basepath = 'C:/Users/pc/gitdoc/'
with os.scandir(basepath) as entries:
    for entry in entries:
        if entry.is_file():   #use entry.is_dir() to list all the directories
            print(entry.name)
"""

#creating empty directory in python
dirc = os.mkdir('C:/Users/pc/gitdoc/example1/')
if True:
    print("Dirctory created successfully")
else:
    print("Directory creation failed")

import os
os.rmdir('C:/Users/pc/gitdoc/example2/')
if True:
    print("Dirctory created successfully")
