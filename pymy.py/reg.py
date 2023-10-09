import  mysql.connector
import tabulate
from tabulate import tabulate

con=mysql.connector.connect(host="localhost",user="root",password="",database="register")

def insert():
    name=input("enter your name : ")
    age=int(input("enter your age : "))
    contact=int(input("enter your number : "))
    email=input("enter your mail : ")

    res=con.cursor()
    sql="insert into data (name,age,contact,email) values (%s,%s,%s,%s)"
    res.execute(sql,(name,age,contact,email))
    con.commit()
    print("\n")
    print("Record Insert sucessfully")

def select():
    res=con.cursor()
    sql="select * from data"
    res.execute(sql)
    result=res.fetchall()
    print("\n")
    print(tabulate(result,headers=["ID","NAME","AGE","CONTACT","MAIL"]))
    #print(tabulate(data, headers=["Name","User ID", "Roll. No."]))
def update():
    print("1.name")
    print("2.age")
    print("3.contact")
    print("4.name")
    print("\n")
    option=int(input("which you field you wantm update ? :"))

    if option==1:
        pid=int(input("enter hyour ID : "))
        name=input("enter your name : ")
        cur=con.cursor()
        sql="update data set name=%s where pid=%s"
        cur.execute(sql,(name,pid))
        con.commit()
        select()
        print("\n")
        print("update sucessfully")
    elif option==2:
        pid=int(input("enter hyour ID : "))
        age=int(input("enter your age : "))
        cur=con.cursor()
        sql="UPDATE data set age=%s where pid=%s"
        cur.execute(sql,(age,pid))
        con.commit()
        select()
        print("\n")
        print("update sucessfully")

    elif option==3:
        pid=int(input("enter hyour ID : "))
        contact=input("enter your contact : ")
        cur=con.cursor()
        sql="update data set contact=%s where pid=%s"
        cur.execute(sql,(contact,pid))
        con.commit()
        select()
        print("\n")
        print("update sucessfully")


    elif option==4:
        pid=int(input("enter hyour ID : "))
        email=input("enter your mail : ")
        cur=con.cursor()
        sql="update data set email=%s where pid=%s"
        cur.execute(sql,(email,pid))
        con.commit()
        select()
        print("\n")

    else:
        print("invalid option ..!!!")

def delete():
    pid=int(input("enter a ID : "))
    res=con.cursor()
    sql="delete from data where pid=%s"
    res.execute(sql,(pid,))
    con.commit()
    print("\n")
    print("delete data successfully")

while True:
    print('\n')
    print("1.Insert Record")
    print("2.Select Record")
    print("3.Update Record")
    print("4.Delete Record")
    print("5.Exit")
    print("\n")

    choice=int(input("enter your choice :"))
    if choice==1:
        insert()
    elif choice==2:
        select()
    elif choice==3:
        update()
    elif choice==4:
        delete()
    elif choice==5:
        quit()
    else:
        print("Invalid option ...!!!!")




