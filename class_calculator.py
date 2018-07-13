class calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return self.a/self.b


opt="1"
while opt=="1":
    print("0.Exit")
    print("1.Addition")
    print("2.subtraction")
    print("3.Multiplication")
    print("4.Division")
    choice=int(input("Enter your choice:"))
    a=int(input("Enetr first number:"))
    b=int(input("Enter second number:"))
    obj=calculator(a,b)

    if choice==1:
        print("Result:",obj.add())
    elif choice==2:
        print("Result:",obj.sub())
    elif choice==3:
        print("Result:",obj.mul())
    elif choice==4:
        print("Result:",obj.div())
    elif choice==0:
        print("exiting")
    else:
        print("invalid choice")
    opt=str(input("do you want to continue press<0/1>"))
