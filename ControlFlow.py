#conditional statement if, else
a=5
if (a%2==0):
  print("even")
else:
  print("odd")


#if, else, elif condition
a=int(input("Enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))

if a>=b and a>=c:
  print(f"{a}is the largest number")

elif b>=a and b>=c:
    print(f"{b}is the largest number")

else :
      print(f"{c}is the largest number")


#check if a year is a leap year

year=int(input("enter a year:"))

if(year%4==0 and year%100!=0) or (year%400==0):
  print(f"{year} is a leap year")
else:
  print(f"{year} is not a leap year")


#grading system

score=int(input("enter the student score:"))

if score>=90:
  print(f"{score} then student is pass")

else:
  print(f"{score}then the student is fail")



#grading system

score=int(input("Enter the student score:"))

if score>=90:
  grade='A'

elif 80<=score<90:
    grade='B'

elif 70<=score<80:
   grade='C'

elif 75<=score<70:
   grade='D'

else:
   grade='F'
print(f"The student grade is:{grade}")



#check if a number is positive, negative, or zero

number=int(input("Enter the number:"))

if number>0:
  print(f"{number} is positive")

elif number==0:
  print(f"{number} is zero")

else:
  print(f"{number} is negative")



# simple calculator (addition, substraction, multiplication, division):

num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
operation=input("Enter the operation(+,-,*,/)")

if operation =='+':
   result=num1+num2

elif operation=='-':
  result=num1-num2

elif operation=='*':
   result-num1*num2

elif opeartion=='/':
    if num1!=0:
      result=num1 / num2

    else:
      result="Cannot divided by Zero"
else:
      result="Invalid Operation"
      else:

   print("The result is:")
    


