#lepo se prikazuje sad
import customtkinter as ctk
from tabla import drawInitialTable
# Иницијализација главног прозора

def MainMenu():

    root = ctk.CTk()
    root.title("Игра Троуглићи")
    root.geometry("400x700")

    # Стилови
    ctk.set_appearance_mode("Dark")  # Модеран тамни режим
    ctk.set_default_color_theme("blue")  # Плави бојни теме

    # Боје и мапирање за позадину
    color_map = {
        "Црвена": "#FF4B4B",
        "Плава": "#4B7BFF",
        "Зелена": "#0ffc03",
        "Жута": "#FFD54B",
        "Љубичаста": "#7f03fc",
        "Наранџаста": "#fc7b03"
    }

    # Функција за промену изабраног режима
    def on_mode_change():
        selected_mode = mode_switch.get()
        if selected_mode:
            print(f"Прво игра противник")
        else:
            print(f"Прво игра први играч (ја)")


    def on_shape_change():
        selected_shape = shape_switch.get()
        if selected_shape:
            print(f"Изабран облик за првог играча је О")
        else:
            print(f"Изабран облик за првог играча је X")


    def on_opponent_change():
        selected_opponent = opponent_switch.get()
        if selected_opponent:
            print(f"Изабран противник је рачунар")
        else:
            print(f"Изабран противник је други играч")


    # Функција за промену боје
    def on_color_change(choice):
        print(f"Изабрана боја: {choice}")
        selected_color = color_map.get(choice, "#FFFFFF")  # Подразумевано бело
        color_combobox.configure(fg_color=selected_color, text_color="black")  # Промена позадине и текста


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

    # Подела за одабир ко почиње игру
    starter_frame = ctk.CTkFrame(root, corner_radius=10)
    starter_frame.pack(pady=10, padx=15, fill="x")

    starter_label = ctk.CTkLabel(starter_frame, text="Одабери ко почиње игру", font=("Arial", 14))
    starter_label.pack(pady=5)

    starter_inner_frame = ctk.CTkFrame(starter_frame, fg_color="transparent")
    starter_inner_frame.pack()

    label_person = ctk.CTkLabel(starter_inner_frame, text="Први играч", font=("Arial", 12))
    label_person.pack(side="left", padx=5)

    mode_switch = ctk.CTkSwitch(starter_inner_frame, text="Противник", command=on_mode_change)
    mode_switch.pack(side="left", padx=5)

    # Подела за одабир облика
    shape_frame = ctk.CTkFrame(root, corner_radius=10)
    shape_frame.pack(pady=10, padx=15, fill="x")

    shape_label = ctk.CTkLabel(shape_frame, text="Одабери који облик желиш да будеш", font=("Arial", 14))
    shape_label.pack(pady=5)

    shape_inner_frame = ctk.CTkFrame(shape_frame, fg_color="transparent")
    # shape_inner_frame.pack()
    shape_inner_frame.pack(pady=5, padx=5, anchor="center")

    label_x = ctk.CTkLabel(shape_inner_frame, text="X", font=("Arial", 12))
    label_x.pack(side="left", padx=5)  # Povećan padding za pomeranje udesno,25

    shape_switch = ctk.CTkSwitch(shape_inner_frame, text="O", command=on_shape_change)
    shape_switch.pack(side="left", padx=5)  # Dodat padding ako je potrebno,10


    # label_x = ctk.CTkLabel(shape_inner_frame, text="X", font=("Arial", 12))
    # label_x.pack(side="left", padx=5)
    #
    # shape_switch = ctk.CTkSwitch(shape_inner_frame, text="O", command=on_shape_change)
    # shape_switch.pack(side="left", padx=5)



    # Подела за одабир боје
    color_frame = ctk.CTkFrame(root, corner_radius=10)
    color_frame.pack(pady=10, padx=15, fill="x")

    color_label = ctk.CTkLabel(color_frame, text="Одабери боју фигурице", font=("Arial", 14))
    color_label.pack(pady=5)

    color_combobox = ctk.CTkComboBox(
        color_frame,
        values=["Зелена", "Црвена", "Плава", "Жута", "Љубичаста", "Наранџаста"],
        command=on_color_change,
        fg_color="#4BFF70",
        text_color="black"  # Постављамо црну боју текста
    )
    color_combobox.pack(pady=5)

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
            drawInitialTable(length)  # Проследи број функцији
            print(f"Игра је започета са дужином странице: {length}")
        else:
            drawInitialTable(4)
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



# #sa skrolom
# import customtkinter as ctk
#
# # Иницијализација главног прозора
# root = ctk.CTk()
# root.title("Игра Троуглићи")
# root.geometry("400x700")
#
# # Стилови
# ctk.set_appearance_mode("Dark")  # Модеран тамни режим
# ctk.set_default_color_theme("blue")  # Плави бојни теме
#
# # Боје и мапирање за позадину
# color_map = {
#     "Црвена": "#FF4B4B",
#     "Плава": "#4B7BFF",
#     "Зелена": "#0ffc03",
#     "Жута": "#FFD54B",
#     "Љубичаста": "#7f03fc",
#     "Наранџаста": "#fc7b03"
# }
#
# # Функције
# def on_mode_change():
#     selected_mode = mode_switch.get()
#     print(f"Прво игра {'противник' if selected_mode else 'први играч (ја)'}")
#
# def on_shape_change():
#     selected_shape = shape_switch.get()
#     print(f"Изабран облик за првог играча је {'О' if selected_shape else 'X'}")
#
# def on_opponent_change():
#     selected_opponent = opponent_switch.get()
#     print(f"Изабран противник је {'рачунар' if selected_opponent else 'други играч'}")
#
# def on_color_change(choice):
#     print(f"Изабрана боја: {choice}")
#     selected_color = color_map.get(choice, "#FFFFFF")
#     color_combobox.configure(fg_color=selected_color, text_color="black")
#
# def increment_value():
#     current_value = int(number_entry.get())
#     if current_value < 8:
#         number_entry.delete(0, "end")
#         number_entry.insert(0, str(current_value + 1))
#
# def decrement_value():
#     current_value = int(number_entry.get())
#     if current_value > 4:
#         number_entry.delete(0, "end")
#         number_entry.insert(0, str(current_value - 1))
#
# def start_game():
#     print("Игра је започета!")
#
# # Скролабилни оквир
# scrollable_frame = ctk.CTkScrollableFrame(root, width=380, height=680, corner_radius=10)
# scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)
#
# # Заглавље
# title_label = ctk.CTkLabel(scrollable_frame, text="ГЛАВНИ МЕНИ", font=("Arial", 20, "bold"))
# title_label.pack(pady=15)
#
# # Подела за одабир противника
# opponent_frame = ctk.CTkFrame(scrollable_frame, corner_radius=10)
# opponent_frame.pack(pady=15, padx=20, fill="x")
#
# opponent_label = ctk.CTkLabel(opponent_frame, text="Одабери противника", font=("Arial", 14))
# opponent_label.pack(pady=10)
#
# opponent_inner_frame = ctk.CTkFrame(opponent_frame, fg_color="transparent")
# opponent_inner_frame.pack()
#
# opponent_person = ctk.CTkLabel(opponent_inner_frame, text="Други играч", font=("Arial", 12))
# opponent_person.pack(side="left", padx=10)
#
# opponent_switch = ctk.CTkSwitch(opponent_inner_frame, text="Рачунар", command=on_opponent_change)
# opponent_switch.pack(side="left", padx=10)
#
# # Подела за одабир ко почиње игру
# starter_frame = ctk.CTkFrame(scrollable_frame, corner_radius=10)
# starter_frame.pack(pady=15, padx=20, fill="x")
#
# starter_label = ctk.CTkLabel(starter_frame, text="Одабери ко почиње игру", font=("Arial", 14))
# starter_label.pack(pady=10)
#
# starter_inner_frame = ctk.CTkFrame(starter_frame, fg_color="transparent")
# starter_inner_frame.pack()
#
# label_person = ctk.CTkLabel(starter_inner_frame, text="Први играч", font=("Arial", 12))
# label_person.pack(side="left", padx=10)
#
# mode_switch = ctk.CTkSwitch(starter_inner_frame, text="Противник", command=on_mode_change)
# mode_switch.pack(side="left", padx=10)
#
# # Подела за одабир облика
# shape_frame = ctk.CTkFrame(scrollable_frame, corner_radius=10)
# shape_frame.pack(pady=15, padx=20, fill="x")
#
# shape_label = ctk.CTkLabel(shape_frame, text="Одабери који облик желиш да будеш", font=("Arial", 14))
# shape_label.pack(pady=10)
#
# shape_inner_frame = ctk.CTkFrame(shape_frame, fg_color="transparent")
# shape_inner_frame.pack()
#
# label_x = ctk.CTkLabel(shape_inner_frame, text="X", font=("Arial", 12))
# label_x.pack(side="left", padx=10)
#
# shape_switch = ctk.CTkSwitch(shape_inner_frame, text="O", command=on_shape_change)
# shape_switch.pack(side="left", padx=10)
#
# # Подела за одабир боје
# color_frame = ctk.CTkFrame(scrollable_frame, corner_radius=10)
# color_frame.pack(pady=15, padx=20, fill="x")
#
# color_label = ctk.CTkLabel(color_frame, text="Одабери боју фигурице", font=("Arial", 14))
# color_label.pack(pady=10)
#
# color_combobox = ctk.CTkComboBox(
#     color_frame,
#     values=["Зелена", "Црвена", "Плава", "Жута", "Љубичаста", "Наранџаста"],
#     command=on_color_change,
#     fg_color="#4BFF70",
#     text_color="black"
# )
# color_combobox.pack(pady=10)
#
# # Подела за унос броја
# number_frame = ctk.CTkFrame(scrollable_frame, corner_radius=10)
# number_frame.pack(pady=15, padx=20, fill="x")
#
# number_label = ctk.CTkLabel(number_frame, text="Одабери дужину странице (4-8):", font=("Arial", 14))
# number_label.pack(pady=10)
#
# controls_frame = ctk.CTkFrame(number_frame, fg_color="transparent")
# controls_frame.pack(pady=10, padx=10, anchor="center")
#
# decrement_button = ctk.CTkButton(controls_frame, text="-", width=30, command=decrement_value)
# decrement_button.pack(side="left", padx=5)
#
# number_entry = ctk.CTkEntry(controls_frame, width=100, justify="center")
# number_entry.insert(0, "4")
# number_entry.pack(side="left", padx=5)
#
# increment_button = ctk.CTkButton(controls_frame, text="+", width=30, command=increment_value)
# increment_button.pack(side="left", padx=5)
#
# # Дугме за покретање игре
# start_button = ctk.CTkButton(
#     scrollable_frame,
#     text="Започни игру",
#     command=start_game,
#     font=("Arial", 14, "bold")
# )
# start_button.pack(pady=20, anchor="center")
#
# # Покретање главне петље
# root.mainloop()
