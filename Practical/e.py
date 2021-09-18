# 5. Write a program to count a total number of lines and count the total number of lines starting with ‘A’, ‘B’, and ‘C’ from the file dfh.txt.

def program5():
  with open("E:\\MyFile.txt","r") as fl:
    data=fl.readlines()
  cnt_lines=0
  cnt_A=0
  cnt_B=0
  cnt_C=0
  for lines in data:
    cnt_lines+=1
    if lines[0]=='A':
      cnt_A+=1
    if lines[0]=='B':
      cnt_B+=1
    if lines[0]=='C':
      cnt_C+=1
    
  print("Total Number of lines are:", cnt_lines)
  print("Total Number of lines strating with A are:", cnt_A)
  print("Total Number of lines strating with B are:", cnt_B)
  print("Total Number of lines strating with C are:", cnt_C)
program5()