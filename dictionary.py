#creating the dictionary
dic1={"name":'Lakshuu',"age":21,"branch":'CSE','id':102}
dic2={"flower":'rose',"place":'jaipur'}
print(dic1)

#adding the key value pair
dic1['occupation']="engineering"
dic2["color"]="pink"
print(dic1)
print(dic2)

#removing the key value pair
keys=dic1.keys()
values=dic1.values()
items=dic1.items()
print(keys)
print(values)
print(items)

#accessing the values
place=dic2['place']
print(place)

#updating the values
dic1['id']=110
dic2['flower']='lotus'
print(dic1)
print(dic2)