# # nije los kod, ali nema provere da li je gumica sirine 3, odnosno 4 stubica
# import matplotlib.pyplot as plt
#
# def drawInitialTable(n):
#     if n < 4 or n > 8:
#         print("n mora biti između 4 i 8!")
#         return
#
#     # Parametri za crtanje
#     start_x = 0  # Početna x koordinata
#     start_y = 0  # Početna y koordinata
#     spacing = 1  # Razmak između tačkica
#
#     x_coords = []  # X koordinate tačkica
#     y_coords = []  # Y koordinate tačkica
#
#     current_row_length = n  # Broj tačkica u trenutnom redu
#     x_offset = 0  # Pomak za levi početak svakog reda
#     y = start_y  # Y koordinata trenutnog reda
#
#     # Crtanje redova sa rastućom dužinom
#     for i in range(n):
#         x = start_x - x_offset
#         for j in range(current_row_length):
#             x_coords.append(x)
#             y_coords.append(y)
#             x += spacing
#
#         current_row_length += 1  # Povećaj dužinu reda
#         x_offset += spacing / 2  # Pomeri početak sledećeg reda ulevo
#         y -= spacing  # Pređi na sledeći red (idemo dole po grafiku)
#
#     # Crtanje redova sa opadajućom dužinom
#     current_row_length = n + n - 1  # Početna dužina za opadajuće redove
#     for i in range(n - 1):
#         x = start_x - x_offset + 1
#         for j in range(1, current_row_length):
#             x_coords.append(x)
#             y_coords.append(y)
#             x += spacing
#         current_row_length -= 1  # Smanji dužinu reda
#         x_offset -= spacing / 2  # Pomeri početak sledećeg reda udesno
#         y -= spacing  # Pređi na sledeći red (idemo dole po grafiku)
#
#     # Interaktivno povezivanje tačaka
#     fig, ax = plt.subplots(figsize=(6, 6))
#     ax.scatter(x_coords, y_coords, color='blue', s=50)  # Crtanje tačkica
#     ax.invert_yaxis()  # Invertovanje Y ose
#     ax.axis('equal')  # Jednake proporcije
#     ax.axis('off')  # Sakrivanje osa
#
#     selected_points = []  # Lista za čuvanje kliknutih tačaka
#
#     def on_click(event):
#         # Traženje najbliže tačke na osnovu kliknute pozicije
#         if event.xdata is not None and event.ydata is not None:
#             distances = [
#                 ((x - event.xdata)**2 + (y - event.ydata)**2)**0.5
#                 for x, y in zip(x_coords, y_coords)
#             ]
#             nearest_index = distances.index(min(distances))
#             nearest_point = (x_coords[nearest_index], y_coords[nearest_index])
#
#             # Dodavanje kliknute tačke u listu
#             selected_points.append(nearest_point)
#             ax.plot(*nearest_point, 'ro', markersize=10)  # Obeleži kliknutu tačku
#
#             # Ako su dve tačke izabrane, nacrtaj liniju
#             if len(selected_points) == 2:
#                 x_line, y_line = zip(*selected_points)
#                 ax.plot(x_line, y_line, 'red', linewidth=2)  # Poveži tačke linijom
#                 selected_points.clear()  # Resetuj izbor
#
#             plt.draw()  # Ažuriraj grafikon
#
#     # Povezivanje događaja klika
#     fig.canvas.mpl_connect('button_press_event', on_click)
#
#     plt.show()
#
#
# # Primer poziva funkcije
# drawInitialTable(4)


#kod koji bi trebalo da ispita uslov da se ne crtaju linije 2 puta izmedju istih tackica(stubica)
import matplotlib.pyplot as plt

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
        for j in range(1, current_row_length):
            x_coords.append(x)
            y_coords.append(y)
            x += spacing
        current_row_length -= 1  # Smanji dužinu reda
        x_offset -= spacing / 2  # Pomeri početak sledećeg reda udesno
        y -= spacing  # Pređi na sledeći red (idemo dole po grafiku)

    # Interaktivno povezivanje tačaka
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(x_coords, y_coords, color='blue', s=50)  # Crtanje tačkica
    ax.invert_yaxis()  # Invertovanje Y ose
    ax.axis('equal')  # Jednake proporcije
    ax.axis('off')  # Sakrivanje osa

    selected_points = []  # Lista za čuvanje kliknutih tačaka
    connected_pairs = set()  # Skup za čuvanje povezanih parova

    def on_click(event):
        # Traženje najbliže tačke na osnovu kliknute pozicije
        if event.xdata is not None and event.ydata is not None:
            distances = [
                ((x - event.xdata)**2 + (y - event.ydata)**2)**0.5
                for x, y in zip(x_coords, y_coords)
            ]
            nearest_index = distances.index(min(distances))
            nearest_point = (x_coords[nearest_index], y_coords[nearest_index])

            # Dodavanje kliknute tačke u listu
            selected_points.append(nearest_point)
            ax.plot(*nearest_point, 'ro', markersize=10)  # Obeleži kliknutu tačku

            # Ako su dve tačke izabrane, nacrtaj liniju
            if len(selected_points) == 2:
                pair = tuple(sorted(selected_points))  # Sortiraj za doslednost
                if pair not in connected_pairs:
                    connected_pairs.add(pair)  # Dodaj par u skup
                    x_line, y_line = zip(*selected_points)
                    ax.plot(x_line, y_line, 'red', linewidth=2)  # Poveži tačke linijom
                else:
                    print(f"Tačke {pair} su već povezane!")  # Obavesti korisnika
                selected_points.clear()  # Resetuj izbor

            plt.draw()  # Ažuriraj grafikon

    # Povezivanje događaja klika
    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.show()






