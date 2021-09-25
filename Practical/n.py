# 14. Write records of students into result.csv. The fields are as following:

from csv import writer
def pro14():
    #Create Header First
    f = open("results.csv","w",newline='\n')
    dt = writer(f)
    dt.writerow(['Student_ID','StudentName','Score'])
    f.close()
    #Insert Data
    f = open("results.csv","a",newline='\n')
    while True:
        st_id= int(input("Enter Student ID:"))
        st_name = input("Enter Student name:")
        st_score = input("Enter score:")
        dt = writer(f)
        dt.writerow([st_id,st_name,st_score])
        ch=input("Want to insert More records?(y or Y):")
        ch=ch.lower()
        if ch !='y':
           break
    print("Record has been added.")
    f.close()
pro14()