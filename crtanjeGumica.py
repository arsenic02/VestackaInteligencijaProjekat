import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches
from matplotlib.path import Path

point_labels = {}  # Rečnik za čuvanje koordinata i oznaka
point_labels_reversed = {}
obojeni_trouglovi = []

igrac1_score=0 #score predstavlja broj trouglica na tabli
igrac2_score=0

def get_igrac1_score():
    return igrac1_score
def get_igrac2_score():
    return igrac2_score

def set_igrac1_score(value):
    global igrac1_score
    igrac1_score = value

def set_igrac2_score(value):
    global igrac2_score
    igrac2_score = value

prviIgracNaPotezu=True #promenljiva koja oznacava koji je igrac na potezu
    #ako je true -> prvi igrac je na potezu
    # ako je false -> drugi igrac je na potezu

def get_prvi_igrac_na_potezu():
    return prviIgracNaPotezu

# Setter funkcija za 'prviIgracNaPotezu'
def set_prvi_igrac_na_potezu(value):
    global prviIgracNaPotezu
    prviIgracNaPotezu = value

def connectDots(ax, point1, point2):
    # Izračunaj dužinu i ugao pravougaonika
    length = ((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2) ** 0.5
    angle = math.degrees(math.atan2(point2[1] - point1[1], point2[0] - point1[0]))

    # Dimenzije pravougaonika
    width = 0.2  # Širina pravougaonika

    # Pozicija pravougaonika treba da bude postavljena tako da njegov centar bude u sredini između tačaka
    rect_x = point1[0]
    rect_y = point1[1]

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

def krajIgre(n,igrac1_score,igrac2_score):

    suma = n + n - 1  # Početna vrednost sume (n + n - 1)
    ukupna_suma = 0  # Početna vrednost ukupne sume

    # Petlja ide od 0 do n-1 (n puta)
    for i in range(n-1):
        ukupna_suma += suma  # Dodajemo trenutnu vrednost sume
        suma += 2  # Povećavamo sumu za 2 u svakoj iteraciji

    print(f"Konačna suma je: {ukupna_suma}")


    if igrac1_score>=ukupna_suma or igrac2_score>=ukupna_suma:
        return True #kraj igre
    else:
        return False

def drawInitialTable(n):
    if n < 4 or n > 8:
        print("n mora biti između 4 i 8!")
        return

    # Parametri za crtanje
    start_x = 0
    start_y = 0
    spacing = 1

    x_coords = []
    y_coords = []


    labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    label_index = 0  # Indeks za oznake redova

    current_row_length = n
    x_offset = 0
    y = start_y

    # prviIgracNaPotezu=True #promenljiva koja oznacava koji je igrac na potezu
    #ako je true -> prvi igrac je na potezu
    # ako je false -> drugi igrac je na potezu

    # Crtanje redova sa rastućom dužinom
    for i in range(n):
        x = start_x - x_offset
        for j in range(current_row_length):
            x_coords.append(x)
            y_coords.append(y)

            # Generisanje oznake tačke
            point_label = f"{labels[label_index]}{j + 1}"
            point_labels[(x, y)] = point_label  # Dodaj u rečnik
            point_labels_reversed[point_label] = (x, y)  # Ključ je oznaka, vrednost je koordinata

            x += spacing
        current_row_length += 1
        x_offset += spacing / 2
        y += spacing  # Promeni ovde u "y += spacing", da raste od gore ka dole
        label_index += 1

    # Crtanje redova sa opadajućom dužinom
    current_row_length = n + n - 1
    for i in range(n - 1):
        x = start_x - x_offset + 1
        for j in range(1, current_row_length):
            x_coords.append(x)
            y_coords.append(y)

            # Generisanje oznake tačke
            point_label = f"{labels[label_index]}{j}"
            point_labels[(x, y)] = point_label  # Dodaj u rečnik
            point_labels_reversed[point_label] = (x, y)  # Ključ je oznaka, vrednost je koordinata

            x += spacing
        current_row_length -= 1
        x_offset -= spacing / 2
        y += spacing  # Promeni ovde u "y += spacing", da raste od gore ka dole
        label_index += 1

    # Prikazivanje na plotu
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(x_coords, y_coords, color='blue', s=50)
    ax.invert_yaxis()  # Ovo inverzuje y-osa, pa će (0, 0) biti u gornjem levom kutu
    ax.axis('equal')
    ax.axis('off')

    selected_points = []
    connected_pairs = set()

    valid_angles = [0, 60, 120, 180, 240, 300]

    def is_valid_angle(point1, point2):
        delta_x = point2[0] - point1[0]
        delta_y = point2[1] - point1[1]
        angle = math.degrees(math.atan2(delta_y, delta_x)) % 360

        tolerance = 7
        for valid_angle in valid_angles:
            if abs(angle - valid_angle) <= tolerance or abs(angle - (valid_angle + 360)) <= tolerance:
                return True
        return False

    def calculate_distance(point1, point2):
        delta_x = point2[0] - point1[0]
        delta_y = point2[1] - point1[1]
        return math.sqrt(delta_x**2 + delta_y**2)

    def razdvoji(input_str):
        letter = ''.join([char for char in input_str if char.isalpha()])
        number = ''.join([char for char in input_str if char.isdigit()])
        number = int(number)
        return (letter,number)

    def broj_u_slovo(n):
        # Pretvori broj u odgovarajuće slovo
        if 1 <= n <= 26:  # Ova funkcija funkcioniše za brojeve od 1 do 26
            return chr(ord('A') + n - 1)  # 'A' ima ASCII vrednost 65, pa dodajemo n-1
        else:
            return "Nema odgovarajućeg slova"  # Ako broj nije između 1 i 26
    def slovo_u_broj(n):
        return (ord(n)-ord('A') + 1)

    def get_intermediate_points(start, end):

        start_point = razdvoji(point_labels[start])
        end_point =  razdvoji(point_labels[end])
        intermediate = []
        if(start_point[0]>end_point[0]):#Uvek stavlja da onaj gore bude start
            start_point, end_point = end_point, start_point  # Swap vrednosti tuple-ova

        diff = abs(start_point[1]-end_point[1])+1
        if(diff==4 or start_point[1]==end_point[1]): #Da li se nalaze sa iste strane ako da onda je SP-EP+1=4 u suprotnom <4

            if(start_point[1]!=end_point[1] and start_point[0] != end_point[0]):
                znak = 1
                if(start_point[1]>end_point[1]):
                    znak=-1
                intermediate.append(f"{chr(ord(start_point[0]) + 1)}{(start_point[1]+znak)}")
                intermediate.append(f"{chr(ord(start_point[0]) + 2)}{start_point[1]+2*znak}")
            elif(start_point[1]==end_point[1] and start_point[0]!=end_point[0] ):
                intermediate.append(f"{chr(ord(start_point[0]) + 1)}{start_point[1]}")
                intermediate.append(f"{chr(ord(start_point[0]) + 2)}{start_point[1]}")
            elif (start_point[0] == end_point[0]):
                intermediate.append(f"{chr(ord(start_point[0]))}{start_point[1]+1}")
                intermediate.append(f"{chr(ord(start_point[0]))}{start_point[1]+2}")
        else: #Gumica prelazi srednju liniju
            if (start_point[1] > end_point[1]):
                intermediate.append(f"{chr(ord(start_point[0])+1)}{start_point[1]}")
                if slovo_u_broj(chr(ord(start_point[0])+1))==n:
                    intermediate.append(f"{chr(ord(start_point[0])+2)}{start_point[1]-1}")
                else:
                    intermediate.append(f"{chr(ord(start_point[0]) + 2)}{start_point[1]}")
            else:
                if slovo_u_broj(chr(ord(start_point[0]) + 1)) == n:
                    intermediate.append(f"{chr(ord(start_point[0]) + 1)}{start_point[1]+1}")
                    intermediate.append(f"{chr(ord(start_point[0]) + 2)}{start_point[1]+1}")
                else:
                    intermediate.append(f"{chr(ord(start_point[0]) + 1)}{start_point[1]+1}")
                    intermediate.append(f"{chr(ord(start_point[0]) + 2)}{start_point[1]+2}")

        return intermediate

    # Globalna lista za crvene tačke
    red_points = []

    def on_click(event):
        threshold_distance = 0.2

        if event.xdata is not None and event.ydata is not None:
            distances = [
                ((x - event.xdata) ** 2 + (y - event.ydata) ** 2) ** 0.5
                for x, y in zip(x_coords, y_coords)
            ]
            nearest_index = distances.index(min(distances))
            nearest_point = (x_coords[nearest_index], y_coords[nearest_index])

            if distances[nearest_index] <= threshold_distance:
                selected_points.append(nearest_point)
                # Nacrtaj crvenu tačku i dodaj je u red_points
                red_point, = ax.plot(*nearest_point, 'ro', markersize=5)
                red_points.append(red_point)

                if len(selected_points) == 2:
                    start_point = selected_points[0]
                    end_point = selected_points[1]

                    if is_valid_angle(start_point, end_point):
                        distance = calculate_distance(start_point, end_point)
                        if distance >= 3 and distance <= 3.6:  # Proveri da li je dužina linije odgovarajuća
                            pair = tuple(sorted([start_point, end_point]))
                            if pair not in connected_pairs:
                                connected_pairs.add(pair)
                                connectDots(ax, start_point, end_point)

                                # Ispisivanje svih tačaka između startne i krajnje
                                print(f"Startna tačka: {point_labels[start_point]}")
                                print(f"Krajnja tačka: {point_labels[end_point]}")

                                intermediate_points = get_intermediate_points(start_point, end_point)
                                for point in intermediate_points:
                                    print(f"Intermedijarna tačka: {point}")
                            else:
                                print(f"Tačke {pair} su već povezane!")
                        else:
                            print("Dužina linije je manja od 4!")
                            remove_last_two_points()  # Ukloni samo poslednje dve tačke
                    else:
                        print("Nevalidan potez!")
                        remove_last_two_points()  # Ukloni samo poslednje dve tačke

                    # Obrisati selektovane tačke za sledeći odabir
                    selected_points.clear()

                plt.draw()
            else:

                # Pronađi 3 najbliže tačke
                sorted_indices = sorted(range(len(distances)), key=lambda i: distances[i])
                closest_points = [(x_coords[i], y_coords[i]) for i in sorted_indices[:3]]

                triangle_path = Path(closest_points)
                for obojeni_path in obojeni_trouglovi:
                    if obojeni_path.contains_point((event.xdata, event.ydata)):
                        print("Ovaj trougao je već obojen!")
                        return

                if get_prvi_igrac_na_potezu():
                    edgecolor = 'green'
                    facecolor = 'green'
                    set_igrac1_score(get_igrac1_score() + 1)
                    print(f"Score igrac1: {get_igrac1_score()}")
                else:
                    edgecolor = 'orange'
                    facecolor = 'orange'
                    set_igrac2_score(get_igrac2_score() + 1)
                    print(f"Score igrac2: {get_igrac2_score()}")


                # Nacrtaj trougao između tih tačaka i oboji ga zelenom bojom
                triangle = patches.Polygon(
                    closest_points,
                    closed=True,
                    edgecolor=edgecolor,#'green',
                    facecolor=facecolor,#'green',  # Dodaj boju unutrašnjosti
                    alpha=0.5,  # Opcionalno, smanji neprozirnost
                    linewidth=1.5
                )
                ax.add_patch(triangle)

                obojeni_trouglovi.append(triangle_path)
                # Oznake tačaka trougla
                for point in closest_points:
                    ax.plot(*point, 'go', markersize=5)
                    print(f"Tačka trougla: {point_labels[point]}")

                plt.draw()

                #logika da nakon odigranog poteza prvog igraca igra drugi igrac, i obrnuto

                if get_prvi_igrac_na_potezu():
                    set_prvi_igrac_na_potezu(False)
                else:
                    set_prvi_igrac_na_potezu(True)

                    if krajIgre(n,igrac1_score,igrac2_score):
                        if igrac1_score>igrac2_score:
                            print('Kraj igre, igrac1 je pobedio')
                        elif igrac2_score>igrac1_score:
                            print('Kraj igre, igrac2 je pobedio')
                        else:
                            print('Kraj igre, nereseno je')
                        return


    def remove_last_two_points():
        """Ukloni samo poslednje dve crvene tačke sa grafa."""
        for _ in range(2):
            if red_points:
                red_point = red_points.pop()
                red_point.remove()  # Ukloni tačku sa grafa
        plt.draw()

    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.show()

# Testiranje funkcije
# drawInitialTable(4)

