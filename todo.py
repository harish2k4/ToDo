from tkinter import *
from tkinter import messagebox

def addtask():
    task = myentry.get()
    if task != "":
        lb.insert(END, task)
        myentry.delete(0,"end")
    else:
        messagebox.showwarning("Warning", "Please Enter The Task")

def deltask():
    lb.delete(ANCHOR)

ws = Tk()
ws.geometry('500x450+500+200')  
ws.title('To Do List App')
ws.config(bg='black')
ws.resizable(width=True, height=True)

frame = Frame(ws)
frame.pack(pady=20)

lb = Listbox(
    frame,
    height=8,
    width=40,
    font=('Times', 18),
    bd=0,
    fg='black',
    highlightthickness=10,
    selectbackground='gray',
    activestyle='none', 
)
lb.pack(side=LEFT, fill=BOTH)

tasks = [
    'Finish HW',
    'Drink water',
    'Write software',
    'Take a nap',
    'Learn something',
    'Write code',
]

for item in tasks:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

myentry = Entry(
    ws,
    font=('Times', 14)
)

myentry.pack(pady=20)

btnframe = Frame(ws)
btnframe.pack(pady=20)

addbtn = Button(
    btnframe,
    text='Add Task',
    font=('Times', 14),
    bg='white',
    padx=20,
    pady=10,
    command=addtask
)

addbtn.pack(fill=BOTH, expand=True, side=LEFT)

delbtn = Button(
    btnframe,
    text='Delete Task',
    font=('Times', 14),
    bg='white',
    padx=20,
    pady=10,
    command=deltask
)

delbtn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()
