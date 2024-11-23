import matplotlib.pyplot as plt
import math
import matplotlib.patches as patches
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
    start_x = 0
    start_y = 0
    spacing = 1

    x_coords = []
    y_coords = []

    current_row_length = n
    x_offset = 0
    y = start_y

    # Crtanje redova sa rastućom dužinom
    for i in range(n):
        x = start_x - x_offset
        for j in range(current_row_length):
            x_coords.append(x)
            y_coords.append(y)
            x += spacing

        current_row_length += 1
        x_offset += spacing / 2
        y -= spacing

    # Crtanje redova sa opadajućom dužinom
    current_row_length = n + n - 1
    for i in range(n - 1):
        x = start_x - x_offset + 1
        for j in range(1, current_row_length):
            x_coords.append(x)
            y_coords.append(y)
            x += spacing
        current_row_length -= 1
        x_offset -= spacing / 2
        y -= spacing

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(x_coords, y_coords, color='blue', s=50)
    ax.invert_yaxis()
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

    def on_click(event):
        # Prag udaljenosti za detekciju tačke
        threshold_distance = 0.2

        if event.xdata is not None and event.ydata is not None:
            distances = [
                ((x - event.xdata)**2 + (y - event.ydata)**2)**0.5
                for x, y in zip(x_coords, y_coords)
            ]
            nearest_index = distances.index(min(distances))
            nearest_point = (x_coords[nearest_index], y_coords[nearest_index])

            # Proveri da li je klik unutar praga
            if distances[nearest_index] <= threshold_distance:
                selected_points.append(nearest_point)
                ax.plot(*nearest_point, 'ro', markersize=5)

                if len(selected_points) == 2:
                    if is_valid_angle(selected_points[0], selected_points[1]):
                        distance = calculate_distance(selected_points[0], selected_points[1])
                        if distance >= 3 and distance <=3.6:  # Proveri da li je dužina linije 4 tacke
                            pair = tuple(sorted(selected_points))
                            if pair not in connected_pairs:
                                connected_pairs.add(pair)
                                connectDots(ax, selected_points[0], selected_points[1])
                                plt.draw()
                            else:
                                print(f"Tačke {pair} su već povezane!")
                        else:
                            print("Dužina linije je manja od 4!")
                    else:
                        print("Nevalidan potez!")

                    for point in selected_points:
                        ax.plot(*point, 'bo', markersize=5)

                    selected_points.clear()

                elif len(selected_points) == 1:
                    ax.plot(*selected_points[0], 'ro', markersize=5)

                plt.draw()
            else:
                print("Klik je van tačke!")  # Poruka za klik van tačke

    fig.canvas.mpl_connect('button_press_event', on_click)

    plt.show()

drawInitialTable(4)
