import random
import sys
import os

print("You can generate password between the range of 1 to 20")
print("Make sure that you remember your randomly generated password before applying the password on your bank "
      "account,E-mail,etc.")
password_length = int(input("Enter password length: "))
password = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
            "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
            "_", "-", "+", "=", "{", "}", "|", "\\", ":", ";", "'", '"', "<", ",", ">", ".", "?", "/", "1", "2", "3",
            "4", "5", "6", "7", "8", "9", "10"]


def generate_pass(number):
    your_password = ''
    for i in range(0, number):
        your_password += random.choice(password)
    print("Your randomly generated password is {}".format(your_password))


generate_pass(password_length)
