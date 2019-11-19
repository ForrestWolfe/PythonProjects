from random import randint
import json
from cryptography.fernet import Fernet
import os

# i need to hash the password I think

"""PassGen creates a randomized password for you, all you have to do is define the length and
PassGen will generate it create a json file containing your data and finally encrypt it."""


# defining the account name, username and length of password
# self.path = the path to your database
# self.secpath is the creates your encryption key file
# self.file path is the directory path plus the newly created file ex. Gmail.json
# self.file opens the new json file for writing purposes
# self.key will generate a new key and save it to your key.key file

class PassGen:
    def __init__(self, DirPath):
        self.account = input('Enter the account name(Gmail, Facebook, Youtube ect..):   ')
        self.username = input('Enter the username associated with the account:   ')
        self.length = int(input('Enter the length of your password:   '))
        self.password = ''
        self.path = DirPath
        self.secpath = self.path + 'key.key'
        self.filePath = DirPath + self.account + '.json'
        self.file = open(self.filePath, 'w')
        self.key = Fernet.generate_key()

    # This is the password generator function
    # for character in range of the length of the password
    # RandomDigit just grabs a random number in between 64 and 123 because those are mostly just alphabet chars
    # random character takes that random digit and uses it to generate a new character
    # self.password is a string each random_character will be added to that string

    def generate(self):
        for char in range(self.length):
            RandomDigit = randint(64, 123)
            random_character = chr(RandomDigit)
            self.password += random_character

    # structure function transforms the data into json syntax
    # dump just makes the data json style and then we use self.file.write to write the data dump
    # MUST close folder otherwise the encryption will not write over your plain text

    def structure(self):
        data = {
            "Account": self.account,
            "Username": self.username,
            "Password": self.password,
        }
        dump = json.dumps(data)
        self.file.write(dump)
        self.file.close()

        # write_key is called when the user doesn't have a key available it is used to generate a new key
        # and write it to the key.key file wb stands for write bytes

    def write_key(self):
        path = self.secpath
        file = open(path, 'wb')
        file.write(self.key)

    # load key is used to generate the encryption itself.
    # return open(key.key file in read bytes) this returns the data from the file

    def load_key(self):
        path = self.secpath
        return open(path, "rb").read()

    # encrypt function encrypts your folder
    # it grabs the key opens the new json file, reads it, and then encrypts it
    # with your new database file still open it writes over the  unencrypted data with encrypted data

    def encrypt(self):
        f = Fernet(self.key)
        file = open(self.filePath, 'rb')
        file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(self.filePath, 'wb') as file:
            file.write(encrypted_data)
        file_data = str(file_data).replace('b', 'Your account information (copy and paste your new password) : ')
        print('\033[3;35;47m' + file_data)



# Decrypter object decrypts the data file that is encrypted


class Decrypter:
    # load key will return the key that will allow the decryption of the data
    @staticmethod
    def load_key(key_directory):
        key = key_directory + '/key.key'
        return open(key, "rb").read()

    # decryption of the data and then finally printing it out for the user to see.
    @staticmethod
    def decrypt(filename, key):
        f = Fernet(key)
        with open(filename, 'rb') as file:
            # read encrypted data
            encrypted_data = file.read()
        # decrypt data
        decrypted_data = f.decrypt(encrypted_data)
        decrypted_data = str(decrypted_data)
        decrypted_data = '\033[3;35;48m' + decrypted_data.replace("b'", ' Decrypted for your desire : ')
        print(decrypted_data)



# The user interface just allows the user to decide whether they want to encrypt or decrypt their data
# then calls the encryption or decryption process
# crypt_key function is the ignition that starts this whole process
# calls all of the functions in the PassGen
def crypt_key(directory, secret_file):
    key = PassGen(directory)
    key.generate()
    key.structure()
    for file in os.listdir(directory):
        if file != secret_file:
            key.write_key()
    key.load_key()
    key.encrypt()

# just a simple ui to ask the user whether they want ot encrypt or decrypt then it performs the functions


def user_interface():
    user_inp = input('Encrypt or Decrypt? :\t')
    user_inp = user_inp.lower()
    if user_inp.__contains__('encrypt'):
        # crypt
        direct = # directory where your key will be stored
        secret = 'key.key'
        crypt_key(direct, secret)
    if user_inp.__contains__('decrypt'):
        # decrypt
        decry = Decrypter()
        key_directory = # directory where your key.key file is
        cryptKey = decry.load_key(key_directory=key_directory)
        fileName = input('Enter the name of the account associated with the file(don\'t enter .json extension) :\t')
        fileName = key_directory + fileName + '.json'
        decry.decrypt(filename=fileName, key=cryptKey)


user_interface()