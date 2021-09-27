# 12. Read a CSV file top5.csv and print the contents in a proper format. The data for top5.csv file are as following:

from csv import reader
def pro1():
    with open("./top5.csv","r") as f:
        d = reader(f)
        data=list(d)
        for i in data:
            print(i)
pro1()