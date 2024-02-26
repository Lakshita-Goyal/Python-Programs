#S=[i for i in range(0-10) if i%2==0]
#print(S)


#using traditional loop
# square=[]

# for i in range(6):
#     # square.append(i**2)
# print("square(loop):",square)


#using list comprehension
# square_com=[x**2 for x in range(6)]
# print("square(List com):",square_com)

# check the even number using list comprehension

# E=[i for i in range(10) if i%2==0]
# print(E)

#check the square of a number using list comprehension

# S=[x**2 for x in range(10)]
# print(S)

#list [12,15,17,19,23,27] reverse of this without using slicing,indexing,function
List=[12,15,17,19,23,27]
length=len(List)

for  i in range((len(List)-1),-1,-1):
 print(List[i])
 