def ertek():
    nap = input('Add meg a nét napját: ')
    ora = input('Add meg az óra nevét: ')
    jegy = int(input('Add meg a jegyet: '))
    print('I/A,B:')
    print(f'\tA hét napja: {nap}')
    print(f'\tAz óra neve: {ora}')
    if jegy <= 0:
      print('Az értékelés nem lehet negatív!')
    elif jegy > 5:
        print('5 pont feletti értékelés nem elfogadható!')
    else:
        print('Köszönjük az értékelést!')



