from Lotto import Lotto
lista_szamok = []
def beolvas():
    f= open('hatos.txt',"r",encoding="utf-8")
    f.readline()

    sorok = f.readlines()

    f.close()
    i = 0
    while(i < len(sorok)):
        sor = sorok[i].strip().split('@')
        lista_szamok.append(Lotto(sor))
        i += 1
    print(lista_szamok[2])
    print('III/A, B:')
    print(f'\tA húzások száma: {i}')

def huzasok_szama():

    return len(lista_szamok)

def huzott_atlag():
    j = 0
    gyujto =0
    atl = 0

    while (j< len(lista_szamok)):
        if lista_szamok[j].het == 42:
            #
            gyujto =lista_szamok[j].szam1+lista_szamok[j].szam2+lista_szamok[j].szam3+lista_szamok[j].szam4+lista_szamok[j].szam5+lista_szamok[j].szam6

        j += 1
    atl = gyujto/6
    print(gyujto)
    print(f'{atl:.2f}')

def legnagyobb():
    j = 0
    szam = 0
    het = 0
    huzas = 0
    while (j < len(lista_szamok)):
        if lista_szamok[j].szam1 > szam:
            szam = lista_szamok[j].szam1
            het = lista_szamok[j].het
            huzas = lista_szamok[j].huzas
        elif lista_szamok[j].szam2 > szam:
            szam = lista_szamok[j].szam2
            het = lista_szamok[j].het
            huzas = lista_szamok[j].huzas
        elif lista_szamok[j].szam3 > szam:
            szam = lista_szamok[j].szam3
            het = lista_szamok[j].het
            huzas = lista_szamok[j].huzas
        elif lista_szamok[j].szam3 > szam:
            szam = lista_szamok[j].szam3
            het = lista_szamok[j].het
            huzas = lista_szamok[j].huzas
        elif lista_szamok[j].szam4 > szam:
            szam = lista_szamok[j].szam4
            het = lista_szamok[j].het
            huzas = lista_szamok[j].huzas
        elif lista_szamok[j].szam5 > szam:
            szam = lista_szamok[j].szam5
            het = lista_szamok[j].het
            huzas = lista_szamok[j].huzas
        elif lista_szamok[j].szam6 > szam:
            szam = lista_szamok[j].szam6
            het = lista_szamok[j].het
            huzas = lista_szamok[j].huzas
        j +=1
    print(f'szám: {szam}, hét: {het}, húzás: {huzas}')