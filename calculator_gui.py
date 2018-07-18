from tkinter import *
window=Tk()
window.resizable(width = False, height = False)

def btnClear():
    global operator
    operator=""
    text_input.set("")

def btnEqual():
    global operator
    sumup=str(eval(operator))
    text_input.set(sumup)
    operator=""

def btnclick(number):
    global operator
    operator=operator+str(number)
    text_input.set(operator)

window.title("                  Calculator")
operator=""
text_input=StringVar()

txtDisplay=Entry(window,font=('arial',20,'bold'),textvariable=text_input,bd=10,insertwidth=3,bg="violet",justify='right').grid(columnspan=4)

b7=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="7",command=lambda:btnclick(7))
b7.grid(row=1,column=0)
b8=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="8",command=lambda:btnclick(8))
b8.grid(row=1,column=1)
b9=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="9",command=lambda:btnclick(9))
b9.grid(row=1,column=2)
bAdd=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="+",command=lambda:btnclick('+'))
bAdd.grid(row=1,column=3)
b4=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="4",command=lambda:btnclick(4))
b4.grid(row=2,column=0)
b5=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="5",command=lambda:btnclick(5))
b5.grid(row=2,column=1)
b6=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="6",command=lambda:btnclick(6))
b6.grid(row=2,column=2)
bSub=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="-",command=lambda:btnclick('-'))
bSub.grid(row=2,column=3)
b1=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="1",command=lambda:btnclick(1))
b1.grid(row=3,column=0)
b2=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="2",command=lambda:btnclick(2))
b2.grid(row=3,column=1)
b3=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="3",command=lambda:btnclick(3))
b3.grid(row=3,column=2)
bMul=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="*",command=lambda:btnclick('*'))
bMul.grid(row=3,column=3)
b0=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="0",command=lambda:btnclick(0))
b0.grid(row=4,column=0)
bC=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="C",command=btnClear)
bC.grid(row=4,column=1)
bDiv=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="/",command=lambda:btnclick('/'))
bDiv.grid(row=4,column=2)
bEqu=Button(window,padx=10,pady=10,bd=8,fg="black",font=('arial',20,'bold'),text="=",command=btnEqual)
bEqu.grid(row=4,column=3)





                                                        

