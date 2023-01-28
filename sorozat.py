import random

list = []
def tizes_sorozat():

    i = 0
    while i < 8:
        vel=int(random.random()*760-100)
        list.append(vel)
        i += 1
    #print(list)
    j = 0
    sz = ""
    while j < len(list):
        if j == len(list)-1:
            sz = sz + str(list[j])
        else:
            sz = sz + str(list[j]) + ";"
        j += 1
    print('II/A, B, C:')
    print(f'\t{sz}')
def tizzel_oszthatoak_szama():
    i = 0
    db = 0
    while(i < len(list)):
        if list[i] % 10 == 0:
            db += 1
        i += 1
    return db

def konzol_ir():
    print('II/D, E:')
    print(f'\tTízzel osztható számok száma: {tizzel_oszthatoak_szama()}.')

def fajlba_ir():
    f = open('vegeredmeny.txt',"w",encoding='utf-8')
    f.write(str(tizzel_oszthatoak_szama()))
    f.close()
