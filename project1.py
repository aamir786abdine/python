import pymysql
db=pymysql.connect("127.0.0.1","root","1234","employee",3306)

def insert():
    id=int(input("Enter your Id"))
    name=str(input("Enetr your Name"))
    dept=str(input("Enetr your Department"))
    desg=str(input("Enetr your Designation"))
    cursor=db.cursor()
    try:
        sql="insert into erecord values(%d,'%s','%s','%s')"%(id,name,dept,desg)
        cursor.execute(sql)
        db.commit()
        print("record inserted")
    except:
        db.rollback() #if therfe is any error then rollback
        db.close()
        print("try Again not inserted")
        

def delete():
    ids=int(input("Enter the Id which you want to delete"))
    cursor=db.cursor()
    try:
        sql="delete from erecord where id=%d"%(ids)
        cursor.execute(sql)  
        db.commit()
        print("record deleted")
    except:
        db.rollback
        db.close()
        print("Your Record is not deleted try Again!")

def update():
    ids=int(input("Enter your Id"))
    name=str(input("Enetr your Name"))
    dept=str(input("Enetr your Department"))
    desg=str(input("Enetr your Designation"))
    #print(ids,name,dept,desg)
    c=db.cursor()
    sql="update erecord set name='%s',dept='%s',desg='%s' where id=%d"%(name,dept,desg,ids)
    try:
        c.execute(sql)
        db.commit()
        print("record updated")
    except:
        db.rollback()
        db.close()
def view():
    c=db.cursor()
    try:
        c.execute("select * from erecord")
        results=c.fetchall()
        print(results)
        for row in results:
            id=row[0]
            name=row[1]
            dept=row[2]
            desg=row[3]
            print("id = ",id , "name = ", name, "dept = ", dept, "desg =", desg)
    except:
        print("Error:unable to fetch data")
        db.close()

def search():
    ids=int(input("enter the id which you want to search:"))
    c=db.cursor()
    try:
        c.execute("SELECT *FROM erecord WHERE id=%d"%(ids))
        results=c.fetchall()
        print(results)
        for row in results:
            id=row[0]
            name=row[1]
            dept=row[2]
            desg=row[3]
            print("id = ",id , "name = ", name, "dept = ", dept, "desg = ", desg)
        print("Above is your searching result")
    except:
        print("Error:unable to fetch data")          
        db.close()



opt="y"
print("Welcome to database Sysytem")
print("1.insert Employee")
print("2.Delete Employee")
print("3.update Employee")
print("4.view Database")
print("5.search an Employee")
while opt=="y":
    ch=int(input("Enetr your choice:"))
    if(ch==1):
       insert()
    elif(ch==2):
       delete()
    elif(ch==3):
       update()
    elif(ch==4):
       view()
    elif(ch==5):
       search()
    else:
       print("Enetr the correct choice")
    opt=str(input("Do you want to cont."))   
