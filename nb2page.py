from sys import argv
import os
import datetime

# Read header with front matter, MathJax settings, etc.
with open('header.txt') as file:
    header = file.read()

# Read notebook body
file_path = argv[1]
with open(file_path) as notebook:
    body = notebook.read()
# Update images path
# TODO: Fix the name of the files folder
body = body.replace('![png](', '![png](assets/img/')

# Save updated file
md_path = file_path[:-5] + 'md'
with open(md_path, 'w') as notebook:
    notebook.write(header + body)

# Rename to include timestamp
date_str = '{:%Y-%m-%d}-'.format(datetime.date.today())
dir_name = os.path.dirname(md_path)
new_path = os.path.join(dir_name, date_str + os.path.basename(md_path))
os.rename(md_path, new_path)
