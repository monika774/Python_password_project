from  tkinter  import*

from tkinter import messagebox

def showMessage():
     messagebox.showerror("Information title", "This is description")

top = Tk()
top.title('Application form')
top.geometry("800x500")
top.configure(bg='yellow')
l1 = Label(top, text = "Enter Full Name: ").place(x = 30, y = 30)
e1 = Entry(top).place(x =150, y  =30)
l1 = Label(top, text = "Enter Full Surname : ").place(x =30, y = 60)
e1 = Entry(top).place(x =150, y  =60)
l1 = Label(top, text = "Enter Full Email: ").place(x = 30, y = 90)
e1 = Entry(top).place(x =150, y  =90)
l1 = Label(top, text = "Enter Class: ").place(x = 30, y = 120)
e1 = Entry(top).place(x =150, y  =120)



b1 = Button(top , text="OK CLICK ME HERE", command=showMessage).place(x=200, y=200)
top.mainloop()
