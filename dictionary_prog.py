#dictionay programming
#
# dict1={
#     "name":22,
#     'age':23,
#     'address':88,
#     'percentage':93
# }
# print(dict1)
# print(dict1['name'])
#creatig a empty dictionary and adding element

# dict2={}
# dict2['name']='name '
# dict2['surname']='vishwakarma'
# dict2['age']=3
# print(f"the dictionary is {dict2}")


#accessing elemnts of dictionary
# print(f"the first element of dictionary is {dict1['name']}")
# print(f"the second element of dictionary is {dict1['age']}")

#dictionary methods
# dict1.clear()
# print(dict1)
# dict2=dict1.copy()
# print(dict2)
# print(dict2.get('name'))
# print(dict2.items())
# print(dict2.pop())


#find the sum of all items in dictionary
# def returnsum(d):
#     list=[]
#     for i in dict1:
#         list.append(dict1[i])
#     final=sum(list)
#     return final
#
# dict1={
#     "name":22,
#     'age':23,
#     'address':88,
#     'percentage':93
# }
#lambda function usage
# print(returnsum(dict1))
# list1=[
#     {"age":22},
#     {'age':23},
#     {'age':18},
#     {'age':93}
# ]
# print(sorted(list1,key=lambda i:i['age']))
#coverting list of tuple into dictionary

#merging a dictionary
# def merge(dict1,dict2):
#     return(dict2.update(dict1))
# dict1={
#     'a':10, 'b':8
# }
# dict2={
#     'c':10, 'd':8
# }
# print(dict2.update(dict1)) #update function is used for merging the dictionary
# print(dict2)

#ocverting list of tuple into dictionary
list_tuple=[("dhiren",10),("viren",4),("sumit",19)]
di=dict(list_tuple)
print(di)

di1=tuple(list_tuple)
print(di1)
di1 = list(list_tuple)
print(di1)





