# 7. Write a program to know the cursor position and print the text according to below-given specifications:
  # Print the initial position.
  # Move the cursor to 4th position .
  # Display next 5 characters.
  # Move the cursor to the next 10 characters.
  # Print the current cursor position.
  # Print next 10 characters from the current cursor position.

def program7():
    f = open("intro.txt", "r")
    print("Cusror initial posotion.")
    print(f.tell())
    f.seek(4,0)
    print("Displaying valuse from 5th posotion.")
    print(f.read(5))
    f.seek(10,0)
    print(f.tell())
    print("Print cursor's current posotion")
    print(f.seek(7,0))
    print("Displaying next 10 characters form cursor's current postion.")
    print(f.read(10))
program7()
