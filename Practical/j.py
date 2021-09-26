# 10. Write a function to write data into binary file marks.dat and display the records of students who scored more than 95 marks.

import pickle
def search_95plus():
    f = open("marks.dat","ab")
    while True:
        rn=int(input("Enter the Rollno:"))
        sname=input("Enter the Name:")
        marks=int(input("Enter the marks:"))
        rec=[]
        data=[rn,sname,marks]
        rec.append(data)
        pickle.dump(rec,f)
        ch=input("Wnat more records?Yes:")
        if ch.lower() not in 'yes':
           break
    f.close()
    f = open("marks.dat","rb")
    cnt=0
    try:
        while True:
            data = pickle.load(f)
            for s in data:
               if s[2]>95:
                   cnt+=1
                   print("Record:",cnt)
                   print("RollNo:",s[0])
                   print("Name:",s[1])
                   print("Marks:",s[2])
    except Exception:
        f.close()
search_95plus()  