import random
from time import sleep
import sys

znaki = 'abcdefghijklmnoprstwqxyzABCDEFGHIJKLMNOPRSTWQXYZ1234567890!@#$%^&*'
serwis = input('Do jakiego serwisu potrzebujesz hasło ? ')

liczba = input('Ile haseł mam wygenerować ? ')
liczba = int(liczba)

dlugosc = input('Jak długie ma być twoje hasło ? ')
dlugosc = int(dlugosc)

for p in range(liczba) :
    haslo = ''
    for c in range(dlugosc) :
        haslo += random.choice(znaki)
print(haslo)

with open('hasła.txt' , "a") as f:
    f.write(serwis + ' ' + haslo + '\n')

print('Hasło zostało wygenerowane i zapisane w pliku tekstowym')

sleep(5)








