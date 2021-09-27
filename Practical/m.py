# 13. Read a CSV file students.csv and print them with tab delimiter. Ignore first row header to print in tabular form.

from csv import reader
def pro3():
    f = open("./students.csv","r")
    dt = reader(f,delimiter=',')
    header_row=next(dt)
    data = list(dt)
    f.close()
    for i in data:
        for j in i:
            print(j,"\t",end=" ")
        print()
pro3() 