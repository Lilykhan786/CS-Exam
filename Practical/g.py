# 7. Write a program to know the cursor position and print the text according to below-given specifications:
  # Print the initial position.
  # Move the cursor to 4th position .
  # Display next 5 characters.
  # Move the cursor to the next 10 characters.
  # Print the current cursor position.
  # Print next 10 characters from the current cursor position.

def program7():
    f = open("intro.txt","r")
    print("Cusror initial position.")
    print(f.tell())
    f.seek(4,0)
    print("Displaying values from 5th position.")
    print(f.read(5))
    f.seek(10,0)
    print(f.tell())
    print("Print cursor's current position")
    print(f.seek(7,0))
    print("Displaying next 10 characters from cursor's current position.")
    print(f.read(10))
program7()