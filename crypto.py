from cryptography.fernet import Fernet
import os

def _return_key(keyfilepath: str, is_decrypting: bool) -> Fernet:
    # If the current operation is Decrypting 
    # We should not create a new key file
    # but rather read from the keyfile path
    
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


def encrypt(path: str, keyfilepath: str) -> None:
    """ 
    Public function encrypt. 
    Param: path takes a string path to encrypt
    Param: keyfilepath takes a string path to the key
    function will go trough every directory and 
    sub directory in path string and encrypt every file
    it finds 
    """
    fernet = _return_key(keyfilepath, False)
    # Find every file in every subdirectory
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


def decrypt(path: str, keyfilepath: str) -> None:

    fernet = _return_key(keyfilepath, True)

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