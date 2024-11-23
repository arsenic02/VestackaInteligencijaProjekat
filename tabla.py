import matplotlib.pyplot as plt
import tkinter as tk

def drawInitialTable(n):
    if n < 4 or n > 8:
        print("n mora biti između 4 i 8!")
        return

    # Parametri za crtanje
    start_x = 0  # Početna x koordinata
    start_y = 0  # Početna y koordinata
    spacing = 1  # Razmak između tačkica

    x_coords = []  # X koordinate tačkica
    y_coords = []  # Y koordinate tačkica

    current_row_length = n  # Broj tačkica u trenutnom redu
    x_offset = 0  # Pomak za levi početak svakog reda
    y = start_y  # Y koordinata trenutnog reda

    # Crtanje redova sa rastućom dužinom, FOR PETLJA JE DOBRA
    for i in range(n):#4
        x = start_x - x_offset
        for j in range(0,current_row_length):
            x_coords.append(x)
            y_coords.append(y)
            x += spacing

        print(y_coords)
        current_row_length += 1  # Povećaj dužinu reda
        x_offset += spacing / 2  # Pomeri početak sledećeg reda ulevo
        y -= spacing  # Pređi na sledeći red (idemo dole po grafiku)

    # Crtanje redova sa opadajućom dužinom
    current_row_length = n + n-1  # Početna dužina za opadajuće redove, n+3
    for i in range(n-1):
        x = start_x - x_offset+1 #bilo je -, za +1 radi samo za n=5
        for j in range(1,current_row_length):
            x_coords.append(x)
            y_coords.append(y)
            x += spacing
        current_row_length -= 1  # Smanji dužinu reda
        print(y_coords)
        x_offset -= spacing / 2  # Pomeri početak sledećeg reda udesno
        y -= spacing  # Pređi na sledeći red (idemo dole po grafiku)

    # Iscrtavanje tačkica
    plt.figure(figsize=(6, 6))
    plt.scatter(x_coords, y_coords, color='blue', s=50)  # s je veličina tačke
    plt.gca().invert_yaxis()  # Invertujemo Y osu da prati "dole" kao u matricama
    plt.axis('equal')  # Jednake proporcije
    plt.axis('off')  # Sakrijemo ose
    plt.show()


