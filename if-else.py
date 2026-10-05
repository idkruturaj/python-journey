print("USING if-else")
print("example 1")
age = int(input(" ENTER THE AGE : "))
if age>= 18:
  print(" U CAN ACCESS OUR WEB ")
else:
  print(" SORRY, THIS WEBSITE IS ONLY FOR 18+ USERS")
  
print("--------------------------------")

print("example 2")
num1 = int(input("Enter the numerator number : "))
num2 = int(input("Enter the denomenator number : "))
if num2 == 0:
  print(" Denominator can never be zero ")
else:
    print(f" The division of the numbers is: {num1/num2}")
