#lepo se prikazuje sad
from secrets import choice

import customtkinter as ctk
from crtanjeGumica import drawInitialTable
# Иницијализација главног прозора

def MainMenu():

    root = ctk.CTk()
    root.title("Игра Троуглићи")
    root.geometry("400x500")

    # Стилови
    ctk.set_appearance_mode("Dark")  # Модеран тамни режим
    ctk.set_default_color_theme("blue")  # Плави бојни теме

    # Боје и мапирање за позадину
    all_colors = ["Зелена", "Црвена", "Плава", "Жута", "Љубичаста", "Наранџаста"]
    color_map = {
        "Црвена": "#FF4B4B",
        "Плава": "#4B7BFF",
        "Зелена": "#0ffc03",
        "Жута": "#FFD54B",
        "Љубичаста": "#7f03fc",
        "Наранџаста": "#fc7b03"
    }
    selected_colors = {1: "#0ffc03", 2: "#4B7BFF"}
    selected_opponent = 1
    def on_opponent_change():
        selected_opponent = opponent_switch.get()
        if selected_opponent:
            print(f"Изабран противник је рачунар")
        else:
            print(f"Изабран противник је други играч")

    # Функција за промену боје
    def on_color_change(player, choice):
        selected_colors[player] = color_map[choice]
        print(f"Играч {player} је изабрао боју: {choice}")
        if(player==1):
            player1_combobox.configure(fg_color=color_map[choice], text_color="black")
        if(player==2):
            player2_combobox.configure(fg_color=color_map[choice], text_color="black")
        update_comboboxes()

    def update_comboboxes():
        available_colors = []
        for color in all_colors:
            if color_map[color] not in selected_colors.values():
                available_colors.append(color)

        player1_combobox.configure(values=available_colors)
        player2_combobox.configure(values=available_colors)

    # Функције за повећање и смањење вредности
    def increment_value():
        current_value = int(number_entry.get())
        if current_value < 8:
            number_entry.delete(0, "end")
            number_entry.insert(0, str(current_value + 1))


    def decrement_value():
        current_value = int(number_entry.get())
        if current_value > 4:
            number_entry.delete(0, "end")
            number_entry.insert(0, str(current_value - 1))


    # Заглавље
    title_label = ctk.CTkLabel(root, text="ГЛАВНИ МЕНИ", font=("Arial", 20, "bold"))
    title_label.pack(pady=10)  # Смањен падинг


    # Подела за одабир противника
    opponent_frame = ctk.CTkFrame(root, corner_radius=10)
    opponent_frame.pack(pady=10, padx=15, fill="x")  # Смањени размаци

    opponent_label = ctk.CTkLabel(opponent_frame, text="Одабери противника", font=("Arial", 14))
    opponent_label.pack(pady=5)

    opponent_inner_frame = ctk.CTkFrame(opponent_frame, fg_color="transparent")
    opponent_inner_frame.pack()

    opponent_person = ctk.CTkLabel(opponent_inner_frame, text="Други игач", font=("Arial", 12))
    opponent_person.pack(side="left", padx=5)

    opponent_switch = ctk.CTkSwitch(opponent_inner_frame, text="Рачунар", command=on_opponent_change)
    opponent_switch.pack(side="left", padx=5)

#-----------------------------------------------------------------------
    # Подела за одабир боје играча 1
    player1_frame = ctk.CTkFrame(root, corner_radius=10)
    player1_frame.pack(pady=10, padx=15, fill="x")

    player1_label = ctk.CTkLabel(player1_frame, text="Играч 1 - Одабери боју", font=("Arial", 14))
    player1_label.pack(pady=5)

    available_colors = []
    for color in all_colors:
        if color_map[color] not in selected_colors.values():
            available_colors.append(color)

    player1_combobox = ctk.CTkComboBox(
        player1_frame,
        values=available_colors,
        command=lambda choice: on_color_change(1, choice),
        fg_color=color_map["Зелена"],
        text_color="black"
    )
    player1_combobox.pack(pady=5)
    player1_combobox.set("Зелена")  # Постављање текста на почетну вредност

    # Подела за одабир боје играча 2
    player2_frame = ctk.CTkFrame(root, corner_radius=10)
    player2_frame.pack(pady=10, padx=15, fill="x")

    player2_label = ctk.CTkLabel(player2_frame, text="Играч 2 - Одабери боју", font=("Arial", 14))
    player2_label.pack(pady=5)

    player2_combobox = ctk.CTkComboBox(
        player2_frame,
        values=available_colors,
        command=lambda choice: on_color_change(2, choice),
        fg_color = color_map["Плава"],
        text_color="black"
    )
    player2_combobox.pack(pady=5)
    player2_combobox.set("Плава")
    #----------------------------------------------------------------------------
    # Подела за унос броја
    number_frame = ctk.CTkFrame(root, corner_radius=10)
    number_frame.pack(pady=10, padx=15, fill="x")

    number_label = ctk.CTkLabel(number_frame, text="Одабери дужину странице (4-8):", font=("Arial", 14))
    number_label.pack(pady=5)

    # Оквир за центрирање
    controls_frame = ctk.CTkFrame(number_frame, fg_color="transparent")
    controls_frame.pack(pady=5, padx=5, anchor="center")

    # Дугме за смањење
    decrement_button = ctk.CTkButton(controls_frame, text="-", width=30, command=decrement_value)
    decrement_button.pack(side="left", padx=5)

    # Поље за унос броја
    number_entry = ctk.CTkEntry(controls_frame, width=100, justify="center")
    number_entry.insert(0, "4")  # Подразумевана вредност
    number_entry.pack(side="left", padx=5)

    # Дугме за повећање
    increment_button = ctk.CTkButton(controls_frame, text="+", width=30, command=increment_value)
    increment_button.pack(side="left", padx=5)

    # Placeholder функција за почетак игре
    def start_game():
        length = int(number_entry.get())  # Конвертуј у број
        if 4 <= length <= 8:  # Провера да је број у дозвољеном опсегу
            drawInitialTable(length,selected_opponent,selected_colors[1],selected_colors[2])  # Проследи број функцији
            print(f"Игра је започета са дужином странице: {length}")
        else:
            drawInitialTable(4,selected_opponent,selected_colors[1],selected_colors[2])
            print(f"Игра је започета са дужином странице: 4")
        root.withdraw()

    # Дугме за покретање игре
    start_button = ctk.CTkButton(
        root,
        text="Започни игру",
        command=start_game,
        font=("Arial", 14, "bold")
    )
    start_button.pack(pady=15, anchor="center")

    # Покретање главне петље
    root.mainloop()
