# CLI File Encryption with Fernet

## Description

While this is still my first ever python script I wrote, I have come a long way and started refactoring the code.

This script will encrypt or decrypt all the files from a pre-set list of directories stored in the Dirs.txt file. When you start main.py you will be asked if you want to add Directories to be encrypted and then you proceed to add directories to the list when you are done adding directories you type in "done", and the list of directories will be displayed to you as well as a confirmation message asking if you would like to encrypt them. The working directory where the key.key file and dirs.txt file are stored is currently stored in a constant.

Now like I said the code has been refactored, the first version was a single file mess, I have since seperated the code into different modules, crypto.py handles the actual encryption and decryption of files in the directories passed to encrypt/decrypt functions as an argument.

I created 2 quiet modules encrypt.py and decrypt.py. These files should quicly encrypt and decrypt files, the Dirs.txt and key.key files should allready exist for this to work

## How to Use/Run

This was writen in Python 3.10 on windows 10, so should run fine on your system if you have python 3.10 installed.
This app was not tested on Linux or Max, you are more than welcome to modify the code for your OS and to let me know if it works.

Simply run main.py

### Additional modules needed

- Fernet Python Library

### Screenshots

I will add some later

### Features

- Encrypt and decrypt all files contained in given directories

### Files Included

> main.py
> - This is the main application where you can create the initial Key file and Dirs.txt files
>
> crypto.py
> - This handles most of encryption and decryption functions and is required to run any of the other modules in the project
> 
> encrypt.py and decrypt.py
> - Quiet modules, that run quicly and silently without user interaction (key.key and Dirs.txt file should exist)


---

<p align="center"> <a href="https://twitter.com/paulstryd" target="blank"><img src="https://img.shields.io/twitter/follow/paulstryd?logo=twitter&style=for-the-badge" alt="paulstryd" /></a> </p>

<p align="center"><a href="https://www.buymeacoffee.com/paulsmts"> <img align="center" src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" height="50" width="210" alt="paulsmts" /></a></p><br><br>
