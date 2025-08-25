import matplotlib.pyplot as plt
import matplotlib.patches as patches

def drawInitialTable(n):
    if n < 4 or n > 8:
        print("n mora biti izmedju 4 i 8!")
        return

    start_x = 0
    start_y = 0
    spacing = 1

    x_coords = []
    y_coords = []

    current_row_length = n
    x_offset = 0
    y = start_y

    for i in range(n):
        x = start_x - x_offset
        for j in range(current_row_length):
            x_coords.append(x)
            y_coords.append(y)
            x += spacing

        current_row_length += 1
        x_offset += spacing / 2
        y -= spacing


    current_row_length = n + n - 1
    for i in range(n - 1):
        x = start_x - x_offset + 1
        for j in range(current_row_length):
            x_coords.append(x)
            y_coords.append(y)
            x += spacing
        current_row_length -= 1
        x_offset -= spacing / 2
        y -= spacing

    plt.figure(figsize=(6, 6))
    ax = plt.gca()

    # Dodavanje trouglova izmedju tackica
    for i in range(len(x_coords) - n):
        if i + n + 1 < len(x_coords):
            triangle = patches.Polygon(
                [(x_coords[i], y_coords[i]),
                 (x_coords[i + 1], y_coords[i + 1]),
                 (x_coords[i + n], y_coords[i + n])],
                closed=True,
                color='orange',
                edgecolor='black'
            )
            ax.add_patch(triangle)

    plt.scatter(x_coords, y_coords, color='blue', s=50)
    plt.gca().invert_yaxis()
    plt.axis('equal')
    plt.axis('off')
    plt.show()

