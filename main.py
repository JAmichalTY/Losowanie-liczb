import random

def gra():
    try:
        while True:

            x = random.randint(1, 10)
            ip = 2  # Liczba prób
            z = 0

            print(f'Zagrajmy w grę! Zgadnij liczbę naturalną z zakresu od 1 do 10 którą wygeneruje losowo!!!'
                  f' Będziesz miał {ip} prób')

            for i in range(ip):

                a = int(input('Podaj Twoją liczbę: '))
                r = (ip - 1) - z

                if a < x:
                    k = 'większa'
                else:
                    k = 'mniejsza'

                if a == x:
                    print('Gratulację udało ci się!!!')
                    break
                elif a != x and z < ip:
                    print(f'Niestety to nie ta liczba, wylosowana jest {k}, pozostała liczba szans : {r}')
                    z += 1

                if r == 0:
                    print(f'Przegrałeś, liczba to {x}')

            p = input('Czy chcesz zagrać ponownie ? Tak lub Nie ').strip().lower()

            if p != 'tak':
                break
    except ValueError:
        print('Powinieneś podać liczbę aby program działał prawidłowo')
        gra()
gra()