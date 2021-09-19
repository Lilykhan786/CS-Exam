# 6. Write a programto replace all spaces from text with – (dash) from the file intro.txt.

def program6():
  cnt = 0
  with open("intro.txt", "r") as f1:
    data = f1.read()
    data = data.replace(' ','-')
  with open("intro.txt", "w") as f1:
    f1.write(data)
  with open("intro.txt", "r") as f1:
    print (f1.read())
program6()