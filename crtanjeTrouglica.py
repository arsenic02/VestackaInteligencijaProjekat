# import matplotlib.pyplot as plt
# import matplotlib.patches as patches
#
# # Kreiranje figure
# fig, ax = plt.subplots()
#
# # Dodavanje trouglova različitih boja
# triangles = [
#     ((0, 0), (1, 0), (0.5, 1), 'red'),      # Koordinate i boja
#     ((1.5, 0), (2.5, 0), (2, 1), 'blue'),
#     ((3, 0), (4, 0), (3.5, 1), 'green')
# ]
#
# for t in triangles:
#     triangle = patches.Polygon([t[0], t[1], t[2]], closed=True, color=t[3])
#     ax.add_patch(triangle)
#
# # Podešavanje granica grafa
# ax.set_xlim(-1, 5)
# ax.set_ylim(-1, 2)
# ax.set_aspect('equal')
#
# # Prikaz
# plt.show()

#prikazuje  proces crtanja
# import turtle
#
# # Funkcija za crtanje trougla
# def draw_triangle(x, y, size, color):
#     turtle.penup()
#     turtle.goto(x, y)
#     turtle.pendown()
#     turtle.fillcolor(color)
#     turtle.begin_fill()
#     for _ in range(3):
#         turtle.forward(size)
#         turtle.left(120)
#     turtle.end_fill()
#
# # Inicijalizacija Turtle ekrana
# screen = turtle.Screen()
# screen.bgcolor("white")
#
# # Crtanje trouglova
# draw_triangle(-100, 0, 50, "red")
# draw_triangle(0, 0, 50, "blue")
# draw_triangle(100, 0, 50, "green")
#
# # Završetak
# turtle.done()

import matplotlib.pyplot as plt
import matplotlib.patches as patches


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

    # Crtanje redova sa rastućom dužinom
    for i in range(n):
        x = start_x - x_offset
        for j in range(current_row_length):
            x_coords.append(x)
            y_coords.append(y)
            x += spacing

        current_row_length += 1  # Povećaj dužinu reda
        x_offset += spacing / 2  # Pomeri početak sledećeg reda ulevo
        y -= spacing  # Pređi na sledeći red (idemo dole po grafiku)

    # Crtanje redova sa opadajućom dužinom
    current_row_length = n + n - 1  # Početna dužina za opadajuće redove
    for i in range(n - 1):
        x = start_x - x_offset + 1
        for j in range(current_row_length):
            x_coords.append(x)
            y_coords.append(y)
            x += spacing
        current_row_length -= 1  # Smanji dužinu reda
        x_offset -= spacing / 2  # Pomeri početak sledećeg reda udesno
        y -= spacing  # Pređi na sledeći red (idemo dole po grafiku)

    # Iscrtavanje tačkica i trouglova
    plt.figure(figsize=(6, 6))
    ax = plt.gca()

    # Dodavanje trouglova između tačkica
    for i in range(len(x_coords) - n):  # Prolazak kroz tačkice
        if i + n + 1 < len(x_coords):
            # Trougao na osnovu tri tačkice
            triangle = patches.Polygon(
                [(x_coords[i], y_coords[i]),
                 (x_coords[i + 1], y_coords[i + 1]),
                 (x_coords[i + n], y_coords[i + n])],
                closed=True,
                color='orange',
                edgecolor='black'
            )
            ax.add_patch(triangle)

    # Iscrtavanje tačkica
    plt.scatter(x_coords, y_coords, color='blue', s=50)  # s je veličina tačke
    plt.gca().invert_yaxis()  # Invertujemo Y osu da prati "dole" kao u matricama
    plt.axis('equal')  # Jednake proporcije
    plt.axis('off')  # Sakrijemo ose
    plt.show()


# Primer poziva funkcije
drawInitialTable(5)
