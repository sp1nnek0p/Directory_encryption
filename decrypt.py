from crypto import decrypt
import os

WORKING_DIR = 'C:/Users/Administrator/AppData/Local/'
KEY_FILE = WORKING_DIR + 'key.key'
DIRS_FILE = WORKING_DIR + 'dirs.txt'


if os.path.isfile(DIRS_FILE):
    with open( DIRS_FILE, "r") as file:
        directories = file.readlines()
        file.close()
    directories = [x.strip() for x in directories]

    for dir in directories:
        decrypt(dir, KEY_FILE)