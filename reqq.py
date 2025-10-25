from tkinter import *
from tkinter import ttk
import tkinter as tk
import mysql.connector
import threading

    

#Работа с Tkinter

results = list()
#Работа в mysql.connector
def mysql_q():
    global results
    try:
        conn = mysql.connector.connect(
        host = "jdkw23rd.duckdns.org",
        user = "bot_user",
        database = "first",
        password = "Qwerty2008.",
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * from tele2 where PHONE = %s", (user_input,))
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        root.after(0, aft)
    except mysql.connector.Error as e:
        labell.config(text=f"Ошибка БД: {e}", font=("Arial", 7, "bold"))
        progress.stop()
        progress.pack_forget()
        butt.config(state=tk.NORMAL)
    except Exception as e:
        labell.config(text=f"Ошибка: {e}", font=("Arial", 7, "bold"))
        progress.stop()
        progress.pack_forget()
        butt.config(state=tk.NORMAL)

def aft():
    progress.stop()
    progress.pack_forget()
    if len(results) == 0:
        labell.config(text="Данные не найдены")
    else:
        labell.config(text="Данные найдены")
        labelll.config(text=results)
def button_clicked():
    global user_input
    user_input = entry_field.get()
    if "7" in user_input:
        global results
        butt.config(state=tk.DISABLED)
        labell.config(text=f"{user_input}\nЗапрос принят ожидайте получения данных", font=("Arial", 16, "bold"))
        thread = threading.Thread(target=mysql_q)
        progress.pack(pady=10, anchor='w')
        progress.start(10)
        thread.start()
        progress.pack(pady=10, anchor='w')
        progress.start(10)
    else:
        labell.config(text="Введите корректные данные")

root = Tk()
root.title('reqq')
root.configure(bg = "lightblue")
label = Label(root, text='Впишите номер телефона для поиска в формате 79867563434', font=("Arial", 16, "bold"), bg="lightblue")
label.pack(anchor='w')

entry_field = Entry(root, width=30)
entry_field.pack(anchor='w')

butt = Button(root, text='Запрос', command = button_clicked, anchor='e', font=("Arial", 16, "bold"), bg="lightblue")
butt.pack(anchor='w', pady='40')
labell=Label(root, text='', font=("Arial", 16, "bold"), bg="lightblue")
labell.pack(anchor='w', pady='40')
labelll=Label(root, text=results, font=("Arial", 16, "bold"), bg="lightblue")
labelll.pack()
progress = ttk.Progressbar(root, mode='indeterminate', length=200)
root.mainloop()
