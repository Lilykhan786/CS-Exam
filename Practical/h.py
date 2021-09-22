# 8. Write a program to store customer data into a binary file cust.dat using a dictionary and print them on screen after reading them. The customer data contains ID as key, and name, city as values.

import pickle
rec={}
def file_create():
    f = open("cline.dat", "wb")
    cno = int(input("Enter Clint ID:"))
    cname = input("Enter Clint Name:")
    address = input("Enter Address:")
    rec={cno:[cname,address]}
    pickle.dump(rec,f)
def read_data():
  f= open("cline.dat", "br")

  print("*"*78)
  print("Data strored in file...")
  rec=pickle.load(f)
  for i in rec :
    print(rec[i])
file_create()