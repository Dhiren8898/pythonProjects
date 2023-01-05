import sys

#program1 reversing the list
list1=[3,5,8,7,2,320,4,99,5]
'''print(list1)
list1.reverse()
print(f"reverse list {list1}")'''
#program2 sum of all the elements in list
'''total=0
for ele in range(0,len(list1)):
    total=total+ele
print(f"the sum of the elements is {total}")'''
#program3 find the smallest & largest number in list
'''list1.sort()
print(f'the smallest number is {list1[0]}')
print(f"the largest number is {list1[-1]}")'''
#program4 printing even and odd numbers from list
'''for i in list1:
    if i%2==0:
        print(i)'''
#program5  finding the duplicate elements from list
'''uniquelist=[]
duplicate_list=[]
for i in list1:
    if i not in uniquelist:
        uniquelist.append(i)
    elif i not in duplicate_list:
        duplicate_list.append(i)
print(duplicate_list)
print(uniquelist)
'''

#tuple
#size of tuple
tuple1=(12,3,22,9)
print(f"size of {tuple1} tuple is {sys.getsizeof(tuple1)} bytes")

#program6 finding the  maximum and minimum element in tuple
#tuple1.sort()
'''print(f"the maximum element of tuple is {tuple1[0]}")
list2=list(tuple1)
print(list2)
list2.sort()
print(f"the maximum value of in tuple is {list2[-1]}")
print(f"the minimum value of in tuple is {list2[0]}")
'''

#
# list1+=tuple1
# print(f"the addition of tuple and list is {list1}")
#
#
#
#
#
# #array creation in python
# import array as arr
# a=arr.array('b',[2,55,4,3])
# print(a)

