__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

###########################################MAIN!!###########################################
import os
from zipfile import ZipFile

def clean_cache():
    dir = os.path.join(os.getcwd(), "files", "cache")
    if not os.path.exists(dir):
        os.mkdir(dir)
    if os.path.exists(dir):
        file = os.path.join("files", "cache")
        files = os.listdir(file)
        for i in files:
            os.remove( os.path.join("files", "cache", i))

def cache_zip(zippie_path, chache_path):
    with ZipFile(zippie_path, 'r') as zipObj:
        zipObj.extractall(chache_path)

def cached_files():
    abs_path = os.path.abspath("files\cache")
    files = os.listdir(abs_path)
    all_file_paths = []
    for file in files:
            file_path = os.path.join(abs_path, file)
            if os.path.isfile(file_path):
                if not file_path in all_file_paths:
                    all_file_paths.append(file_path)
    return (all_file_paths)

def find_password(cached_files):
    all_file_paths = cached_files
    for i in all_file_paths:
        with open(i) as openfile:
            for line in openfile:
                if "password" in line:
                    line_sepperated = line.split(' ')
                    password = line_sepperated[1]
                    password = password.strip()
                    return (password)

zippie_path = os.path.join(os.getcwd(), "files", "data.zip")
chache_path = os.path.join(os.getcwd(), "files", "cache")
clean_cache()
cache_zip(zippie_path, chache_path)
cached_files()
find_password(cached_files())

###########################################Questions!!###########################################
""" 1) clean_cache: takes no arguments and creates an empty folder named cache in the current directory. If it already exists, it deletes everything in the cache folder."""

""" 2) cache_zip: takes a zip file path (str) and a cache dir path (str) as arguments, in that order. The function then unpacks the indicated zip file into a clean cache folder, You can test this with data.zip file."""

""" 3) cached_files: takes no arguments and returns a list of all the files in the cache. The file paths should be specified in absolute terms. Search the web for what this means! 
No folders should be included in the list. You do not have to account for files within folders within the cache directory."""

""" 4) find_password: takes the list of file paths from cached_files as an argument. This function should read the text in each one to see if the password is in there. 
Surely there should be a word in there to indicate the presence of the password? Once found, find_password should return this password string."""
