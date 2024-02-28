# traditional apporach without the walrus operator
n=10
squares=[]

while n>0:
    square=n**2
    squares.append(square)
    n-=1
print("squares(Traditonal):",squares)


#using walrus operator
n=5
squares=[]
while(square:=n**2)>0:
    squares.append(square)
    n-=1
print("squares(Walrus Operator):",squares)


# import calendar
# print(calendar.month(2023,2))

#using modules in python
def cal(a,b):
    return a*b,a+b,a-b,a//b

cal(12,3)
print(cal(12,3))