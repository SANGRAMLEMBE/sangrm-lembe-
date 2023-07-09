from tkinter import *
from tkinter import messagebox

def fun(event):# event parameter is working with only bind not with command
    messagebox.showinfo("My Window","calculation done !!!")
    lbl.configure(text="Calculation Sucsefull")

class MyWindow:
    def __init__(self,win):
        self.lbl1=Label(win,text='First number',fg="red",bg="yellow",font=("bold",12))
        self.lbl2 = Label(win, text='Secound number',fg="red",bg="yellow",font=("bold",12))
        self.lbl3 = Label(win, text='Result',fg="red",bg="yellow",font=("bold",12))

        self.t1=Entry(bd=3)
        self.t2=Entry(bd=3)
        self.t3=Entry(bd=3)
        self.btn1=Button(win,text='ADD')
        self.btn2 = Button(win, text='Substract')
        self.btn3 = Button(win, text='Multiplication')
        self.btn4 = Button(win, text='Division')
        self.lbl1.place(x=100,y=50)
        self.t1.place(x=250,y=50)
        self.lbl2.place(x=100,y=100)
        self.t2.place(x=250,y=100)
        self.b1=Button(win,text='ADD',command=self.add,fg="red",bg="yellow",font=("bold",12))
        #self.b1.bind('<Double-Button-1>', fun)
        self.b2=Button(win,text='substraction',command=self.sub,fg="red",bg="yellow",font=("bold",12))
        #self.b2.bind('<Double-Button-1>', fun)
        self.b3 = Button(win, text='Multiplication', command=self.mul, fg="red", bg="yellow", font=("bold", 12))
        # self.b3.bind('<Double-Button-1>', fun)
        self.b4 = Button(win, text='Division', command=self.div, fg="red", bg="yellow", font=("bold", 12))
        # self.b4.bind('<Double-Button-1>', fun)
        self.b1.place(x=100,y=150)
        self.b2.place(x=200,y=150)
        self.b3.place(x=100,y=200)
        self.b4.place(x=250,y=200)
        self.lbl3.place(x=100,y=250)
        self.t3.place(x=200,y=250)
    def add(self):
        self.t3.delete(0,'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END,str(result))
    def sub(self,event):
        self.t3.delete(0,'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result =num1-num2
        self.t3.insert(END, str(result))
    def mul(self):
        self.t3.delete(0,'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1*num2
        self.t3.insert(END,str(result))
    def div(self):
        self.t3.delete(0,'end')
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1/num2
        self.t3.insert(END,str(result))


window=Tk()
mywin=MyWindow(window)
window.title('Python Calculater')
window.geometry("400x300+10+10")
window.configure(background="aqua")

lbl = Label(window,fg="green",font=("bold",12))
lbl.place(x=150,y=350)

def on_closing():
    if messagebox.askokcancel("Quit","DO YOU WANT TO QUIT?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW",on_closing)

window.mainloop()


