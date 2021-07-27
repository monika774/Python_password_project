import random  
from tkinter import*
from functools import partial
top = Tk()
top.geometry("800x600")
top.title("Password generator")
top.configure(bg='pink')


def generate(lwr, upr, nbr, sb):
  lower = "abcdefghijklmnopqrstuvwxyz"
  upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numbers = "1234567890"
  symbol = "!@#$%^&*()"


  all = " "
 
  if lwr.get() == 1:
      all = all + lower
  if upr.get() == 1:
      all = all + upper
  if nbr.get() == 1:
      all = all + numbers
  if sb.get() == 1:
      all = all + symbol

  length = 6
  password ="".join(random.sample(all, length))
  print(password)
  
lwr = IntVar()
upr = IntVar()
nbr = IntVar()
sb  = IntVar()


c1 = Checkbutton(top, text="Lower Characters", variable=lwr, onvalue=1, offvalue=0).place(x=100, y=50)
c2 = Checkbutton(top, text="Upper Characters", variable=upr, onvalue=1, offvalue=0).place(x=100, y=150)
c3 = Checkbutton(top, text="Numbers Characters", variable=nbr, onvalue=1, offvalue=0).place(x=100, y=250)
c4 = Checkbutton(top, text="Symbol Characters", variable=sb, onvalue=1, offvalue=0).place(x=100, y=350)

generate = partial(generate, lwr, upr, nbr, sb)

b1 = Button(top, text ="Generate Password", command= generate,bg='#ffffff', activebackground='#4444ff').place(x=150, y=400)

top.mainloop()

