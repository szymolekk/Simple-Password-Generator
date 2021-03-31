import random
from time import sleep
import sys

signs = 'abcdefghijklmnoprstwqxyzABCDEFGHIJKLMNOPRSTWQXYZ1234567890!@#$%^&*'
question = input('Input a name for your password ')

number = input('How many password do you need ? ')
number = int(number)

length = input('How much characters should your password have ? ')
length = int(length)

for p in range(number) :
    password = ''
    for c in range(length) :
        password += random.choice(signs)
print(password)

with open('passwords.txt' , "a") as f:
    f.write(question + ' ' + password + '\n')

print('Password has been generated and saved to passwords.txt file')

sleep(5)








