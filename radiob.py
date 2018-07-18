from tkinter import *
window=Tk()
c=StringVar()
list1=['canada','new york','usa','Nepal','Uk','turkey']
d=OptionMenu(window,c,*list1)
d.configure(width=25)
c.set('select your country')
d.place(x=235,y=250)
