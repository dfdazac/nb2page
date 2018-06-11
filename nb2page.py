from sys import argv
import os
import datetime
import shutil

ASSETS_PATH = 'assets/img/'
POSTS_PATH = '_posts/'

# Read header with front matter, MathJax settings, etc.
with open('header.txt') as file:
    header = file.read()

# Read markdown body
nb_path = argv[1]
nb_name = os.path.basename(nb_path)
name = os.path.splitext(nb_name)[0]
dir_name = os.path.dirname(nb_path)
files_folder = name + '_files'
md_path = os.path.join(dir_name, name + '.md')
body = ''
asset_start = '!['
assets_to_copy = []
with open(md_path) as markdown:
    for line in markdown:
        new_line = line
        # Check for own or external assets
        if new_line.startswith(asset_start):
            # png are assumed to be in the files folder already
            if new_line.startswith('![png]('):
                new_line = new_line.replace('![png](', '![png](' + ASSETS_PATH)
            # External assets have to be copied to the files folder
            elif new_line.startswith('![Alt Text]('):
                asset = new_line[new_line.find('(') + 1:new_line.find(')')]
                new_line = '![Alt Text](' + os.path.join(ASSETS_PATH, files_folder, asset) + ')\n'
                assets_to_copy.append(asset)

        body += new_line

# Save updated file
print('Adding extra content')
with open(md_path, 'w') as markdown:
    markdown.write(header + body)

# Rename to include timestamp
date_str = '{:%Y-%m-%d}-'.format(datetime.date.today())
new_md_name = date_str + os.path.basename(md_path)
new_path = os.path.join(dir_name, new_md_name)
os.rename(md_path, new_path)

# Copy external assets to files folder
files_folder_path = os.path.join(dir_name, files_folder)
for asset in assets_to_copy:
    shutil.copy(os.path.join(dir_name, asset), files_folder_path)

# Move files to folders in page root
page_path = argv[2]
print('Moving to', page_path)

def move_replace(src, dest):
    """ Move src to dest (either files or directories recursively),
    asking for overwrite when required.
    """
    proceed = True
    if os.path.exists(dest):
        answer = ''
        while answer not in ('y', 'n'):
            answer = input('Warning:\n\t{:s}\nalready exists, do you want to overwrite it? (y/n): '.format(dest))
        if answer == 'y':
            # Check whether destination to be removed is
            # file or directory to proceed accordingly
            if os.path.isdir(dest):
                shutil.rmtree(dest)
            elif os.path.isfile(dest):
                os.remove(dest)
        else:
            proceed = False
            print('Cancelled writing.')
    if proceed:
        shutil.move(src, dest)

move_replace(new_path, os.path.join(page_path, POSTS_PATH, new_md_name))
move_replace(files_folder_path, os.path.join(page_path, ASSETS_PATH, files_folder))

print('Done')
