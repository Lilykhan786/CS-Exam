# 4. Create a text file “intro.txt” in python and ask the user to write a single line text by user input.

def program4():
  f = open("intro.txt","w")
  text=input("Enter the text:" )
  f.write(text)
  f.close()
program4()
