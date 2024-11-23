import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math

import matplotlib.patches as patches

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import math
def connectDots(ax, point1, point2):
    # Izračunaj dužinu i ugao pravougaonika
    length = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
    angle = math.degrees(math.atan2(point2[1] - point1[1], point2[0] - point1[0]))

    # Dimenzije pravougaonika
    width = 0.2  # Širina pravougaonika
    x1 = point1[0]
    y1=point1[1]
    x2= point2[0]
    y2 = point2[1]

    # Pozicija pravougaonika treba da bude postavljena tako da njegov centar bude u sredini između tačaka
    # Podesimo poziciju donjeg levog ugla
    rect_x = x1
    rect_y = y1

    # Kreiraj pravougaonik sa željenim parametrima
    rectangle = patches.Rectangle(
        (rect_x, rect_y),  # Donji levi ugao pravougaonika
        length,  # Dužina pravougaonika
        width,  # Širina pravougaonika
        angle=angle,  # Ugao rotacije
        linewidth=0.7,
        edgecolor='red',
        facecolor='none')

    # Dodaj pravougaonik na grafikon
    ax.add_patch(rectangle)

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

    valid_angles = [0, 60, 120, 180, 240, 300]
    def is_valid_angle(point1, point2):
        # Izračunaj ugao između tačaka (u stepenima)
        delta_x = point2[0] - point1[0]
        delta_y = point2[1] - point1[1]
        angle = math.degrees(math.atan2(delta_y, delta_x)) % 360  # Ugaoni radijus u stepenima

        # Proveri da li ugao spada u opseg ±7° za bilo koji validan ugao
        tolerance = 7
        for valid_angle in valid_angles:
            if abs(angle - valid_angle) <= tolerance or abs(angle - (valid_angle + 360)) <= tolerance:
                return True

        # Ako nije u opsegu, potez nije validan
        return False

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
            ax.plot(*nearest_point, 'ro', markersize=5)  # Obeleži kliknutu tačku

            # Ako su dve tačke izabrane, nacrtaj liniju
            if len(selected_points) == 2:
                # Provera validnosti poteza
                if is_valid_angle(selected_points[0], selected_points[1]):
                    pair = tuple(sorted(selected_points))  # Sortiraj za doslednost
                    if pair not in connected_pairs:
                        connected_pairs.add(pair)  # Dodaj par u skup
                        connectDots(ax, selected_points[0], selected_points[1])  # Poveži tačke pravougaonikom
                        plt.draw()  # Ažuriraj grafikon
                    else:
                        print(f"Tačke {pair} su već povezane!")  # Obavesti korisnika
                else:
                    print("Nevalidan potez!")  # Obavesti korisnika da potez nije validan

                # Resetuj boje svih selektovanih tačaka
                for point in selected_points:
                    ax.plot(*point, 'bo', markersize=5)  # Vrati na početnu plavu boju

                selected_points.clear()  # Resetuj izbor

            elif len(selected_points) == 1:
                # Označi trenutno selektovanu tačku
                ax.plot(*selected_points[0], 'ro', markersize=5)  # Crvena boja za selektovanu tačku

            plt.draw()  # Ažuriraj prikaz u svakom slučaju

    # Povezivanje događaja klika
    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.show()

drawInitialTable(4)


