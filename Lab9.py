from tkinter import *
from tkinter import font

def Autorize():
    def StartGame(): #Создаём окно с игровым полем и открываем его
        root.destroy() #Закрываем лишние окна
        start.destroy()
        game = Tk()
        game.title("Игра")
        game.geometry("800x800")
        game.mainloop()
    font1 = font.Font(family= "Verdana", size=11, weight="normal", slant="roman")
    with open("register.txt", "r+") as file: #Открываем файл с данными пользователей
        if not (login.get() or password.get()):
            message = Label(anchor=W, bg="#F8F8FF", text="Заполните все поля!", font=font1)
        else:
            if (login.get() and password.get()) in file.read().split(): #Если введённые данные уже есть
                start = Tk()
                start.title("Начать игру")
                start.geometry("300x100")
                start.configure(background="#F8F8FF")
                message = Label(master=start, anchor=W, bg="#F8F8FF", text="Вы успешно авторизовались!", font=font1)  #Авторизуем пользователя
                message.pack(padx=6, pady=6)
                btn = Button(master=start, text="Начать игру", anchor=W, bg="#6A5ACD", fg="#FFFFFF", font=font1, command=StartGame)
                btn.pack(padx=6, pady=6) 
                start.mainloop()
            else: #Если данные введены впервые
                message = Label(anchor=W, bg="#F8F8FF", text="Неверный логин или пароль!", font=font1) #Сообщение об ошибке входа
                message.pack(padx=6, pady=6)

def Register():
    with open("register.txt", "r+") as file: #Открываем файл с данными пользователей
        if not (login.get() or password.get()):
            message = Label(anchor=W, bg="#F8F8FF", text="Заполните все поля!", font=font1)
        else:
            if login.get() in file.read().split(): #Если введённые данные уже есть
                message = Label(anchor=W, bg="#F8F8FF", text="Такой пользователь уже зарегистрирован!", font=font1)  #Сообщение об ошибке регистрации
                message.pack(padx=6, pady=6)
            else: #Если данные введены впервые
                    file.write(login.get() + " " + password.get() + "\n") #Регистрируем пользователя
                    message = Label(anchor=W, bg="#F8F8FF", text="Вы успешно зарегистрировались!", font=font1) 
                    message.pack(padx=6, pady=6)
     
root = Tk()     # создаем корневой объект - окно
root.title("Лабораторная работа №9")     # устанавливаем заголовок окна
root.geometry("400x300")    # устанавливаем размеры окна
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
btn1 = Button(text="Войти", bg="#6A5ACD", fg="#FFFFFF", font=font1, command=Autorize) #создаём кнопки и устанавливаем внутри окна
btn1.pack(padx=6, pady=6) 
btn2 = Button(text="Зарегистрироваться", bg="#6A5ACD", fg="#FFFFFF", font=font1, command=Register) #создаём кнопки и устанавливаем внутри окна
btn2.pack(padx=6, pady=6) 
root.mainloop()
