#Создать окно регистрации/авторизации пользователя. Данные пользователя записывать в локальный файл.

from tkinter import *
from tkinter import font

def Register():
        def StartGame(): #Создаём окно с игровым полем и открываем его
            root.destroy() #Закрываем лишние окна
            start.destroy()
            game = Tk()
            game.title("Игра")
            game.geometry("800x800")
            game.mainloop()
        log = login.get()
        pas = password.get()
        start = Tk()
        start.title("Начать игру")
        start.geometry("300x100")
        start.configure(background="#F8F8FF")
        font1 = font.Font(family= "Verdana", size=11, weight="normal", slant="roman")
        with open("register.txt", "r+") as file: #Открываем файл с данными пользователей
            if not (login.get() or password.get()):
                message = Label(anchor=W, bg="#F8F8FF", text="Заполните все поля!", font=font1)
            else:
                if (login.get() and password.get()) in file.read().split(): #Если введённые данные уже есть
                    message = Label(master=start, anchor=W, bg="#F8F8FF", text="Вы успешно авторизовались!", font=font1)  #Авторизуем пользователя
                    message.pack(padx=6, pady=6)
                else: #Если данные введены впервые
                        file.write(log + " " + pas + "\n") #Регистрируем пользователя
                        message = Label(master=start, anchor=W, bg="#F8F8FF", text="Вы успешно зарегистрировались!", font=font1) 
                        message.pack(padx=6, pady=6)
                btn = Button(master=start, text="Начать игру", anchor=W, bg="#6A5ACD", fg="#FFFFFF", font=font1, command=StartGame)
                btn.pack(padx=6, pady=6) 
                start.mainloop()

root = Tk()     # создаем корневой объект - окно
root.title("Лабораторная работа №9")     # устанавливаем заголовок окна
root.geometry("400x200")    # устанавливаем размеры окна
root.configure(background="#F8F8FF")
font1 = font.Font(family= "Verdana", size=11, weight="normal", slant="roman")
llogin = Label(font=font1, anchor=W, background="#F8F8FF", text="Введите Ваш логин") # создаем текстовую метку
llogin.pack(padx=6, pady=6) # размещаем метку в окне
login=Entry(bd=2)
login.pack(padx=6, pady=6)
lpassword = Label(font=font1, anchor=W, background="#F8F8FF", text="Введите Ваш пароль") 
lpassword.pack(padx=6, pady=6)
password=Entry(bd=2)
password.pack(padx=6, pady=6)
btn = Button(text="Зарегистрироваться/Войти", bg="#6A5ACD", fg="#FFFFFF", font=font1, command=Register) #создаём кнопки и устанавливаем внутри окна
btn.pack(padx=6, pady=6) 
root.mainloop()
