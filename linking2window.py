from tkinter import *

class Welcome():
    def __init__(self,master):
        self.master=master
        master.geometry("500x400+400+200")
        master.title("Welcome")
        Label(master,text="Welcome to wages Calculator GUI",fg="violet",font=('bold',20),anchor='w').grid(row=0,column=0)
        Button(master,text="OK",padx=8,pady=8,bg="green",fg="white",command=self.gotowages).place(x=200,y=50)
        Button(master,text="QUIT",padx=8,pady=8,bg="red",fg="white",command=self.finish).place(x=300,y=50)
    def finish(self):
        self.master.destroy()
        
    def gotowages(self):
        root2=Toplevel(self.master)
        MyGUI=Wages(root2)
        
class Wages():
    def __init__(self,master):
        self.master=master
        self.nhours=DoubleVar()
        self.salaryh=DoubleVar()

        self.master.geometry("500x200+100+200")
        self.master.title("Wages Calculator")
        Label(master,text="Welcome to wages Calculator GUI",fg="violet",font=('bold',15),anchor='w').grid(row=0,column=0)
        Label(master,text="Enter your salary per hour",fg="red",font=('bold',10),anchor='w').grid(row=3,column=0)
        Label(master,text="Enter the no. of hours worked",fg="red",font=('bold',10),anchor='w').grid(row=4,column=0)
        self.mysalary=Entry(self.master,textvariable=self.salaryh).grid(row=3,column=1)
        self.myhours=Entry(self.master,textvariable=self.nhours).grid(row=4,column=1)
        Button(master,text="calculate salary",bg="red",fg="white",command=self.calcsal).place(x=300,y=120)
        Button(master,text="Back",bg="red",fg="white",command=self.myquit).place(x=330,y=150)
    def myquit(self):
        self.master.destroy()
    def calcsal(self):
        hours=self.nhours.get()
        print("No.of hours worked:",hours)
        hsal=self.salaryh.get()
        print("Salary per hour",hsal)
        salary=hours*hsal
        print("Total Earning",salary)
        Label(self.master,text="your salary is Rs %.2f ."%salary).place(x=230,y=90)
        
        
    
def main():
    croot=Tk()
    myGUIWelcome=Welcome(croot)
    croot.mainloop()
if __name__=='__main__':
    main()
    
