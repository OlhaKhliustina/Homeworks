'''
Practice
1.  a) Write a program that generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
    b) To each file append a random number between 1 and 100.
    c) Create a summary file (summary.txt) that contains name of the file and number in that file:
A.txt: 67
B.txt: 12
...
Z.txt: 98
'''
from random import randint

summary_file = open('summary.txt', 'w')
for i in range(ord('A'), ord('Z')+1):
    with open(chr(i)+'.txt', 'w') as alph:
        alph.write(str(randint(1, 100)))
        summary_file.write(f'{i}.txt: {alph}\n')
