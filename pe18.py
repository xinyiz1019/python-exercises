'''
Exercise 18

Create a program that will play the "cows and bulls" game with the user. The game works like this:

Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a "cow". For every digit the user guessed correctly in the wrong place is a "bull". Every time the user makes a guess, tell them how many "cows" and "bulls" they have. Once the user makes throughout the game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:
    Welcome to the Cows and Bulls Game!
    Enter a number:
    >>>1234
    2 cows, 0 bulls
    >>>1256
    1 cows, 1 bulls
    ...
Until the user guesses the number.
'''

import random

def cb(r):
    t=0
    a=int(input('Enter a number: '))
    while a not in range(1000,10000):
        a=int(input('Enter a number: '))
    b=str(a)
    c=str(r)
    nc=0
    nb=0
    for i in range(4):
        if b[i]==c[i]:
            nc+=1
    d=[e for e in b if e in c]
    nb=len(d)
    print(nc,' cows',nb,' bulls')
    if nc==4:
        t=1
    return t

if __name__=="__main__":
    print('Welcome to the Cows and Bulls Game!')
    number=[0,1,2,3,4,5,6,7,8,9]
    r1=random.sample(number,4)
    r=[]
    for rr1 in r1:
        r.append(str(rr1))
    r="".join(r)
    #print(r)
    t=cb(r)
    g=1
    while t!=1:
        g+=1
        t=cb(r)
    print('Cong!','Only',g,'guesses!')