# traditional method

a=int(input("enter the first number"))
b=int(input("enter the second number"))

c=a/b

print(c)
    
# using exception handling
a=int(input("Enter the first number"))
b=int(input("enter the second number"))

try:
    c=a/b
    print("result",c)

except:
    print("cannot divided by zero")

else:
    print("continue")

# index error with list

def get_list_element(my_list,index):
    try:
        element=my_list[index]
        print("Element at index",index,"is:",element)

    except IndexError:
        print("Error: Index out of range")

my_list=[1,2,3,4]
get_list_element=(my_list,2)
get_list_element=(my_list,10)

try:
    print(x)

except NameError:
    print("variable x is not defined")

except:
    print(" something else went wrong")



