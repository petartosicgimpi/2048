import pyautogui as pg # omogućava automatizaciju kontrolisanja kursora i unosa putem tastature
import time # pauziranje izvršavanja koda

grid = []

def unesi_podatke():
    while True:
        row = input('Unesite red: ')
        if len(row) != 9 or not row.isdigit():
            print("Nevažeći unos. Unesite tačno 9 cifara.")
            continue

        ints = [int(n) for n in row]
        grid.append(ints)

        if len(grid) == 9:
            break
        print('Red ' + str(len(grid)) + ' - Sledeći red')

def moguće(x, y, n):
    # Proveri red
    for i in range(9):
        if grid[y][i] == n:
            return False

    # Proveri kolonu
    for i in range(9):
        if grid[i][x] == n:
            return False

    # Proveri 3x3 kutiju
    x0, y0 = (x // 3) * 3, (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[y0 + i][x0 + j] == n:
                return False

    return True

def prikaži_mrežu(matrica):
    for red in matrica:
        print(" ".join(str(num) for num in red))
    print()

def klikni_startnu_poziciju():
    # Pomeri miš na početnu poziciju Sudoku mreže u vašem pregledaču.
    # Zamenite (x, y) koordinatama prve ćelije Sudoku mreže.
    x, y = 100, 200  # Primer koordinata
    pg.click(x, y)

def prikaži_rešenje(matrica):
    str_fin = [str(num) for red in matrica for num in red]

    for i, num in enumerate(str_fin):
        pg.press(num)
        pg.hotkey('right')
        if (i + 1) % 9 == 0:
            pg.hotkey('down')
            for _ in range(8):
                pg.hotkey('left')

def reši():
    global grid
    for y in range(9):
        for x in range(9):
            if grid[y][x] == 0:
                for n in range(1, 10):
                    if moguće(x, y, n):
                        grid[y][x] = n
                        reši()
                        grid[y][x] = 0
                return
    prikaži_rešenje(grid)
    input("Još?")

# Glavna izvršna funkcija
unesi_podatke()
print("Početna Sudoku mreža:")
prikaži_mrežu(grid)
time.sleep(1)

# Osigurajte da je pregledač aktivan i pomerite kursor na startnu poziciju
input("Pritisnite Enter da biste započeli unos rešenja u pregledač...")
klikni_startnu_poziciju()
reši()
