from crypto import encrypt, decrypt
import os

WORKING_DIR = 'C:/Users/Administrator/AppData/Local/'

def dir_list():
        if os.path.isfile(WORKING_DIR + "Dirs.txt"):
            with open( WORKING_DIR + "Dirs.txt", "r") as file:
                directories = file.readlines()
                file.close()
            return [x.strip() for x in directories]


def dir_append(dir_lst = []):
    
    pass

def create_dir_list():
    # This must change to take in the Directories list and append to them

    dir_answer = input("Would you like to add directories to encrypt y/n?: ")
    new_directories = list()
    if dir_answer.lower() == 'y':
        while True:
            dir = input("Input the directory with / inplace of \\ or type done: ")
            
            new_directories.append(dir)
            
            if new_directories[len(new_directories) -1] == 'done':
                new_directories.pop(len(new_directories) -1 )

                with open(WORKING_DIR + "Dirs.txt", 'w') as file:
                    file.writelines("%s\n" % d for d in new_directories)
                    file.close()

                return new_directories      
    else:
        print("Program will now exit")
        quit()



if __name__ == '__main__':

    keyfilepath = WORKING_DIR + "key.key"
    # -----------------------------------------
    # Check to see if the Dirs file exists
    if os.path.isfile(WORKING_DIR + "Dirs.txt"):
        with open( WORKING_DIR + "Dirs.txt", "r") as file:
            directories = file.readlines()
            file.close()
        directories = [x.strip() for x in directories]
    else:
        # -----------------------------------
        directories = create_dir_list()

    for dir in directories:
        print(dir)
    answer = input("Type e to encrypt or d to decrypt or a to add files in given directories: ")

    if answer.lower() == 'e':
        pw_enquiry = input("Password Protect Encrypted files y/n?: ")    
        if pw_enquiry.lower() == 'y':
            pw_answer = input("Input a password: ")
            with open(WORKING_DIR + "Key.pwd", "w") as f:
                f.write(pw_answer)
                f.close()

            for dir in directories:
                print("Encrypting " + dir)
                encrypt(dir, keyfilepath)

        elif pw_enquiry.lower() == 'n':
            for dir in directories:
                print("Encrypting " + dir)
                encrypt(dir, keyfilepath)

    elif answer.lower() == 'd':
        if os.path.isfile(WORKING_DIR + "Key.pwd"):
            with open( WORKING_DIR + "Key.pwd", 'r') as f:
                passw = f.read()
                f.close()
            passw_answer = input("Input the password to Decrypt: ")
                
            if passw == passw_answer:
                for dir in directories:
                    print("Decrypting " + dir)
                    decrypt(dir, keyfilepath)
            else:
                print("Incorect Password Provided, program will exit")   
                quit()     
        else:
            for dir in directories:
                print("Decrypting " + dir)
                decrypt(dir, keyfilepath)
