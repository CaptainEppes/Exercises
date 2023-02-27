# https://open.kattis.com/problems/accessdenied

passSize = 0
t = '5'
while t == '5':
    passSize+=1
    print('A'*passSize)
    t = input()[15:-4]

if t != '': 
    alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    i = 0
    password = ''
    passFound = True
    filler = 'a'*(passSize-1)
    nextTime = '14'

    while passFound:
        while True:
            print(password + alpha[i] + filler)
            t = input()[15:-4]
            if t == '':
                passFound = False
                break
            elif t != nextTime:
                password += alpha[i]
                break
            i+=1
        i=0
        filler = filler[:-1]
        nextTime = str(int(nextTime)+9)
