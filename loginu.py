from tkinter import *
from tkinter import messagebox

login = ["user0"]

if login[:2] == 'io' and login[2:].isdigit () and len(login)<=10:
    print('Correct')
else:
    print('Incorrect')
root = Tk()
root.title("кнопка")
root.geometry("500x200+600+300")

t1 = Label(text="выберите вид входа",fg='white', bg="blue")
t1.config(font=('Times', 25))
t1.pack()

regist = Button(text="регистрация", background="#555", foreground="#ccc", font="20", pady="10", padx="10")
regist.config(command=state_score)
regist.pack()


log = Button(text="вход", background="#555", foreground="#ccc", padx="15", pady="7", font="13")
log.config(command=far)
log.pack()

root.mainloop()
