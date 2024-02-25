#creating a set
my_set1={1,2,3,4,5,6,7,8,9,10}
my_set2={'a','b','c','d','e','f','g'}
print(my_set1)
print(my_set2)

#adding the elements in set
my_set2.add("lakshuu")
print(my_set2)

#removing the element from set
my_set2.remove("lakshuu")
print(my_set2)

#union of sets
set_union=my_set1.union({11,12})
print(set_union)

#intersection of element
set_intersection=my_set2.intersection({2,'a'})
print(set_intersection)

#difference of set
set_difference=my_set1.difference()
