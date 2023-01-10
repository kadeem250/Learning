#https://geekflare.com/password-generator-python-code/
#https://geekflare.com/handle-files-in-python/

import secrets
import string
import pyperclip

letters = string.ascii_letters
digits = string.digits
special_char = string.punctuation
Secured_for = string
alphabet = letters + digits + special_char

pwd_length =15
pwd = ''

#color codes
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


#Main function
for i in range(pwd_length):
    pwd += ''.join(secrets.choice(alphabet))
print ("Your Password is: ", color.RED + pwd + '\033[0m')
print("The password has been copied to the clipboard.")
pyperclip.copy(pwd)

with open('Python Generated Passwords.txt', 'a') as file:
    Secured_for = input("What is this password for: ")
    name = [Secured_for]
    books = [pwd]
    file.writelines( "\n")
    file.writelines("% s\n" % data for data in name)
    file.writelines("% s\n" % data for data in books)

if(str(Secured_for) =="Overide 1A"):
    print("I understand what to do")
    lines=file.readline()
    lines=lines[:-2]