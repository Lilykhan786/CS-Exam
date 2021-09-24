# 11. Write a function to count records from the binary file marks.dat.

import pickle
def count_records():
    f = open("./Practical/marks.dat","rb")
    cnt=0
    try:
        while True:
            data = pickle.load(f)
            for s in data:
                   cnt+=1
    except Exception:
        f.close()
    print("The file has ", cnt, " records.")
count_records()