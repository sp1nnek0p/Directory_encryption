from cryptography.fernet import Fernet
import os

def create_key(keyfilepath, is_decrypting):
    if is_decrypting and os.path.isfile(keyfilepath):
        with open(keyfilepath, 'rb') as filekey:
                key = filekey.read()
    elif is_decrypting and not os.path.isfile(keyfilepath):
        print("Key not found exiting")
        quit()
    elif not is_decrypting and os.path.isfile(keyfilepath):
        with open(keyfilepath, 'rb') as filekey:
            key = filekey.read()
    else:
        key = Fernet.generate_key()
        with open(keyfilepath, 'wb') as filekey:
            filekey.write(key)

    fernet = Fernet(key)
    return fernet

def encrypt(path, keyfilepath):
    fernet = create_key(keyfilepath, False)

    for subdir, dir, files in os.walk(path):
        for filename in files:
            filepath = subdir + "/" + filename
            # opening the original file to encrypt
            with open(filepath, 'rb') as file:
                original = file.read()
      
            # encrypting the file
            encrypted = fernet.encrypt(original)
  
            # writing the encrypted data
            with open(filepath, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)

def decrypt(path, keyfilepath):
    fernet = create_key(keyfilepath, True)

    for subdir, dir, files in os.walk(path):
        for filename in files:
            filepath = subdir + "/" + filename

            # opening the encrypted file
            with open(filepath, 'rb') as enc_file:
                encrypted = enc_file.read()
            # decrypting the file
            decrypted = fernet.decrypt(encrypted)  
            # writing the decrypted data
            with open(filepath, 'wb') as dec_file:
                dec_file.write(decrypted)

def create_dir_list():
    dir_answer = input("Would you like to add directories to encrypt y/n?: ")
    new_directories = list()
    if dir_answer.lower() == 'y':
        while True:
            dir = input("Input the directory with / inplace of \\ or type done: ")
            new_directories.append(dir)
            
            if new_directories[len(new_directories) -1] == 'done':
                new_directories.pop(len(new_directories) -1 )
                with open("AppData/Local/Dirs.txt", 'w') as file:
                    file.writelines("%s\n" % d for d in new_directories)
                file.close()
                return new_directories      
    else:
        print("Program will now exit")
        quit()

###############################################################
# TODO: Modify the code to take a custom directory from the user to store the key file
# ENCRYPT THE PW FILE AND THE DIRS FILE AFTER CREATING IT.
###############################################################

if __name__ == '__main__':
    keyfilepath = "AppData/Local/key.key"

    if os.path.isfile("AppData/Local/Dirs.txt"):
        with open("AppData/Local/Dirs.txt", "r") as file:
            Directories = file.readlines()
            file.close()
        Directories = [x.strip() for x in Directories]
    else:
                Directories = create_dir_list()

    for dir in Directories:
        print(dir)
    answer = input("Type e to encrypt or d to decrypt files in given Directories: ")

    if answer.lower() == 'e':
        pw_enquiry = input("Password Protect Encrypted files y/n?: ")    
        if pw_enquiry.lower() == 'y':
            pw_answer = input("Input a password: ")
            with open("AppData/Local/Key.pwd", "w") as f:
                f.write(pw_answer)
                f.close()

            for dir in Directories:
                print("Encrypting " + dir)
                encrypt(dir, keyfilepath)

        elif pw_enquiry.lower() == 'n':
            for dir in Directories:
                print("Encrypting " + dir)
                encrypt(dir, keyfilepath)

    elif answer.lower() == 'd':
        if os.path.isfile("AppData/Local/Key.pwd"):
            with open("AppData/Local/Key.pwd", 'r') as f:
                passw = f.read()
                f.close()
            passw_answer = input("Input the password to Decrypt: ")
                
            if passw == passw_answer:
                for dir in Directories:
                    print("Decrypting " + dir)
                    decrypt(dir, keyfilepath)
            else:
                print("Incorect Password Provided, program will exit")   
                quit()     
        else:
            for dir in Directories:
                print("Decrypting " + dir)
                decrypt(dir, keyfilepath)
