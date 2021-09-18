# 3. Write a python program to demonstrate the concept of variable length argument to calculate product and power of the first 10 numbers.

def sum10 (*n):
  total=0
  for i in n:
      total=total+i
  print("Sum of first 10 Numbers:", total)
sum10(1,2,3,4,5,6,7,8,9,10)

def product10(*n):
  pr=1
  for i in n:
    pr=pr*i
  print("Product of first 10 Numbers:", pr)
product10(1,2,3,4,5,6,7,8,9,10)
