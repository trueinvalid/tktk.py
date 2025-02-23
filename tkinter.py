import tkinter as tk
from tkinter import messagebox


def open_profile_page(name):
    # Создаем новое окно
    profile_window = tk.Toplevel(window)
    profile_window.title("Профиль")
    profile_window.geometry("300x200")

    # Приветственное сообщение
    label_welcome = tk.Label(profile_window, text=f"Добро пожаловать, {name}!", font=("Arial", 14))
    label_welcome.pack(pady=20)

    # Кнопка выхода
    button_exit = tk.Button(profile_window, text="Выйти", command=profile_window.destroy)
    button_exit.pack(pady=10)
def register():
    name = entry_name.get()
    age = entry_age.get()
    skill = skill_var.get()
    agreement = agreement_var.get()

    # Проверяем корректность данных
    if not name or not age:
        messagebox.showerror("Ошибка", "Пожалуйста, заполните все поля.")
        return

    try:
        age = int(age)
        if age <= 0:
            raise ValueError
    except ValueError:
        messagebox.showerror("Ошибка", "Возраст должен быть положительным числом.")
        return

    if not agreement:
        messagebox.showerror("Ошибка", "Вы должны согласиться с условиями.")
        return

    # Успешная регистрация
    messagebox.showinfo("Успех", f"Регистрация завершена!\n\nИмя: {name}\nВозраст: {age}\nНавык: {skill}")
    open_profile_page(name)

# Создаем окно
window = tk.Tk()
window.title("Регистрация")
window.geometry("400x300")

# Метка и поле дл ввода ФИО
label_name = tk.Label(window, text="ФИО:")
label_name.pack(pady=5)
entry_name = tk.Entry(window, width=30)
entry_name.pack(pady=5)

# Метка и поле для ввода возраста
label_age = tk.Label(window, text="Возраст:")
label_age.pack(pady=5)
entry_age = tk.Entry(window, width=10)
entry_age.pack(pady=5)

# Метка и выпадающий список для навыков
label_skill = tk.Label(window, text="Выберите навык:")
label_skill.pack(pady=5)

skills = ["Программирование", "Дизайн", "Аналитика", "Маркетинг"]
skill_var = tk.StringVar(value=skills[2])
skill_menu = tk.OptionMenu(window, skill_var, *skills)
skill_menu.pack(pady=5)

# Галочка на согласие
agreement_var = tk.BooleanVar()
agreement_checkbox = tk.Checkbutton(window, text="Согласен с условиями", variable=agreement_var)
agreement_checkbox.pack(pady=10)

# Кнопка регистрации
button_register = tk.Button(window, text="Зарегистрироваться", command=register)
button_register.pack(pady=10)

# Запуск главного цикла
window.mainloop()
