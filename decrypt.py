from crypto import decrypt
import os
"""
The idea behind separate encrypt and decrypt files is to
run then independently given that the key file exists and
rhe dirs.txt file exist in the given directories
"""
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
