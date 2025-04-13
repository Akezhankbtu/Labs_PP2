import psycopg2
import csv


conn=psycopg2.connect(
    dbname='phonebook',
    user='akezhanamanzhol',
    password='4167',
    host='localhost',
    port='5432'

)

conn.autocommit=True
command_insert="INSERT INTO phonebook (username, phone) VALUES (%s, %s)"
cur=conn.cursor()

def csvv():
    with open('Straw_hat.csv','r') as file:
        reader=csv.DictReader(file)
        for row in reader:
            cur.execute("INSERT INTO phonebook (username,phone) VALUES (%s,%s)",
                        (row['username'],row['phone']))
        
def insert_db():
    username=input("Name:")
    phone=input("Phone:")

    cur.execute(command_insert,(username,phone))



def change_name():
    id=int(input("ID:"))

    new_name=input("New name:")
    cur.execute("UPDATE phonebook SET username=%s WHERE id=%s",(new_name,id))
    print("Name updated")



def change_phone():
    new_phone=input("Phone:")
    id=int(input("ID"))
    cur.execute("UPDATE phonebook SET phone=%s WHERE id=%s",(new_phone,id))
    print("Phone updated")

def query_data():
    filter_text = input("Enter search filter (part of name or phone): ")

    cur.execute("SELECT*FROM phonebook where username ILIKE %s OR phone ILIKE %s",
                ('%'+ filter_text+'%','%'+filter_text+'%'))
    results=cur.fetchall()
    for r in results:
        print(r)
def delete_user():
    value=input("Enter name or phone to Delete:")
    cur.execute("DELETE from phonebook WHERE username=%s OR phone=%s ",(value,value))
    print("User deleted if existed.")
while True:
    print("1 - Insert from input")
    print("2 - Change name")
    print("3 - Change phone")
    print("4 - Query data")
    print("5 - Delete")
    print("6-CSV file")
    print("0 - Exit")
    
    choice = input("Choose option: ")
    
    if choice == "1":
        insert_db()
    elif choice == "2":
        change_name()
    elif choice == "3":
        change_phone()
    elif choice == "4":
        query_data()
    elif choice == "5":
        delete_user()
    elif choice=="6":
        csvv()
    elif choice == "0":
        break
    else:
        print("Invalid option.")
cur.close()
conn.close()