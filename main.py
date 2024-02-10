from tkinter import *

print("WELCOME")
print("Enter two numbers you want to perform operations on: ")

num1 = float(input("Firt number"))
num2 = float(input("Second number"))

while True:
  print("1. +")
  print("2. -")
  print("3. ×")
  print("4. ÷")
  print("5.close")

  choice = input ("choose")

  if choice =="1":
    print(num1 + num2)

  elif choice == "2":
    print(num1 - num2)

  elif choice == "3":

      if num1 or num2 == 0:
       print("0")
      else:
        print(num1*num2)


  elif choice == "4":
      if  float(num2) == 0:
        print("number cannot be divided by zero")

      else:
        print(num1/num2)




  elif choice == "5":
      print("close...")
      break

  else:
      print("Invalid choice Please try again.")






