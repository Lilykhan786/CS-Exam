# 9. Write a program to create a binary file sales.dat and write a menu driven program to do the following:

#   Insert record
#   Search Record
#   Update Record
#   Display record
#   Exit

import pickle
import os
def main_menu():
    print("1. Insert a record")
    print("2. Search a record")
    print("3. Update a record")
    print("4. Display a record")
    print("5. Delete a record")
    print("6. Exit")
    ch = int(input("Enter your choice:"))
    if ch==1:
        insert_rec()
    elif ch==2:
        search_rec()
    elif ch==3:
        update_rec()
    elif ch==4:
        display_rec()
    elif ch==5:
        delete_rec()
    elif ch==6:
        print("Have a nice day!")
    else:
        print("Invalid Choice.")

def insert_rec():
    f = open("sales.dat","ab")
    c = 'yes'
    while True:
        sales_id=int(input("Enter ID:"))
        name=input("Enter Name:")
        city=input("Enter City:")
        d = {"SalesId":sales_id,"Name":name,"City":city}
        pickle.dump(d,f)
        print("Record Inserted.")
        print("Want to insert more records, Type yes:")
        c = input()
        c = c.lower()
        if c not in 'yes':
            break
    main_menu()
    f.close()
    
def display_rec():
    f = open("sales.dat","rb")
    try:
        while True:
            d = pickle.load(f)
            print(d)
    except Exception:
       f.close()
    main_menu()

def search_rec():
    f = open("sales.dat","rb")
    s=int(input("Enter id to search:"))
    f1 = 0
    try:
        while True:
            d = pickle.load(f)
            if d["SalesId"]==s:
                f1=1
                print(d)
                break
    except Exception:
        f.close()
    if f1==0:
        print("Record not found...")
    else:
        print("Record found...")
    main_menu()

def update_rec():
    f1 = open("sales.dat","rb")
    f2 = open("temp.dat","wb")
    s=int(input("Enter id to update:"))
    try:
        while True:
            d = pickle.load(f1)
            if d["SalesId"]==s:
                d["Name"]=input("Enter Name:")
                d["City"]=input("Enter City:")
            pickle.dump(d,f2)
    except EOFError:
        print("Record Updated.")
    f1.close()
    f2.close()
    os.remove("sales.dat")
    os.rename("temp.dat","sales.dat")
    main_menu()

def delete_rec():
    f1 = open("sales.dat","rb")
    f2 = open("temp.dat","wb")
    s=int(input("Enter id to delete:"))
    try:
        while True:
            d = pickle.load(f1)
            if d["SalesId"]!=s:
                pickle.dump(d,f2)
    except EOFError:
        print("Record Deleted.")
    f1.close()
    f2.close()
    os.remove("sales.dat")
    os.rename("temp.dat","sales.dat")
    main_menu()
main_menu()