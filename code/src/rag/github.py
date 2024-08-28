"""
This script provides functionality for cloning a repository searching for
markdown files and converting them to plain text.

Author: Rodrigo Prestes Machado
"""

import os
import shutil
import markdown2
from bs4 import BeautifulSoup

# Repository
URL = "https://github.com/orion-services/"
PROJECT = "ai"
REPOSITORY = URL + PROJECT

def show_list_files(file_array):
    """
    Prints the content of the array of files

    files: array of files
    """
    print(file_array)

def delete_folder(folder):
    """
    Deletes a folder if it exists

    folder: folder to be deleted
    """
    if os.path.exists(folder):
        shutil.rmtree(folder)

# Delete the folder if it exists
delete_folder("ai")
delete_folder("text_files")

# Clone repository
os.system("git clone " + REPOSITORY)

# Search only for .md files in doc folder
files = []
for root, directories, filenames in os.walk(PROJECT+ "/doc"):
    for filename in filenames:
        if filename.endswith(".md"):
            files.append(os.path.join(root, filename))

# Remove index.md from the list
files = [file for file in files if "index.md" not in file]

# Show the files
show_list_files(files)

# Create a directory in the root of the project to store the new text files
output_dir = "text_files"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# For each md file remove the markdown elements and create a new text plain file
for file in files:
    # Read the file
    with open(file, "r", encoding='utf-8') as f:
        content = f.read()
    # Convert markdown to html
    html = markdown2.markdown(content)
    # Remove html tags
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    # Remove {: .fs-3 } and {: .fs-4 } from the text
    text = text.replace("{: .fs-2 }", "")
    text = text.replace("{: .fs-3 }", "")
    text = text.replace("{: .fs-4 }", "")
    text = text.replace("{: .label .label-red }", "")
    # Remove some lines of the text
    text = text.split("\n", 4)[4]

    # Create a new file in the output directory
    new_file = os.path.join(output_dir, os.path.basename(file).replace(".md", ".txt"))
    with open(new_file, "w", encoding='utf-8') as f:
        f.write(text)

# Delete the folder if it exists
delete_folder(PROJECT)
