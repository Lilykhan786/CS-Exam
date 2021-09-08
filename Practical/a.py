# 1. Write a python program using a function to print factorial number series from n to m numbers.

def facto():
  n=int(input("Enter the number:"))
  f=1
  for i in range(1,n+1):
    f*=i
    print(f, end=" ")
facto()
