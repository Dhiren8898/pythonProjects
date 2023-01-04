#finding the factorial of number
'''a=int(input("enter a number please= "))
fact=1
for i in range(fact,a+1):
    fact=fact*i
print("factorial of number is =",fact)
'''
#finding the simple intrest
'''
def simple_intrest(p,t,r):
    print("principle is",p)
    print("time-period is", t)
    print("rate of intrest is", r)

    si=(p*t*r)/100
    print("simple intrest is",si)
    return si
simple_intrest(8,6,8)'''
#finding the compound intrest
'''def com_intrest(p,r,t):
    a=p*(pow((1+r/100),t))
    compound_intrest=a-p
    print("the compound intrest is= ",compound_intrest)
com_intrest(10000,10.25,5)'''
#finding the area of circle
'''def circle_1(r):
    pi=3.142
    area=pi*r*r
    print("area of circle=",area)

circle_1(5)'''
'''n=int(input("enter the number ="))
if n>1:
    for i in range(2,int(n/2)+1):
        if(n%i)==0:
            print("{0} is prime".format(n))
        else:
            print(" number is not prime")'''
#lets do problems on functions
'''for i in range(0,10,2):
     print(i)

print("doneeeee")
list=[1,2,3,4,5,6,7,8,9,10]
for i in list[0::3]:
    print(i)
'''
#this function will give the addition of number

#
# def helloworld(a=2,b=5):
#      c=a+b #c is local variable
#      print("i m first proram of pyhton and addition is",c)
# def helloworld1(a,b=3):
#      c=a+b #c is local variable
#      d=a*b
#      print("i m first proram of pyhton and addition is",c)
#      return c,d
#
#
# x,y=helloworld1(3,4) #returned value of function is stored in variable x
# print(f"the addition is {x} and the multiplication is {y}")
# #a=10       #a is gloabal variable

#helloworld(a,b=3)
#helloworld1(4)  #function call #taking one external parameter and one defauly parameter

#helloworld()# for default value

#printing the even numbers in list
# list=[3,4,6,2,99,7,55,45,66]
# for i in list:
#      if i%2==0:
#           print(i)
# list1=[3,-4,6,-9]
# for i in list1:
#      if i<0:
#           print(i)

list1=["mango","ornage","apple","lichi"]
# list2=[3,5,22,44,9] #index starts from 0 and ends on n-1
# list3=[2,"hiii"]
# print(list2[-1])
# print(list2[1:3])
# print(list2[:-1])
# print(f" set={set(list2)}")
# x=set(list2)
# x.remove('5')
# print("",x)

#

# print(list1)
# print(len(list1))
# print(f"the length of {list1} is{len(list1)}")
# for i in list1:
#      print(i)

# list1.append('banana')
# print(f"modified list {list1}")
# print(f"sorted list {list2.sort()} ")
# del list2[0]
# print("after deleting the list",list2)


#tuple
# tuple1=("mango","orange","banana","lichi")
# print(tuple1)
# print(f"the length of tuple is {tuple1} is {len(tuple1)}")
# print("index",tuple1[2])




#dictionary


dict_1={
     'name':"diren",
     'age':24,
     "email":"abc@gmail.com"
}
print(f"the intial dictionary is {dict_1}")
dict_1['name']='sohel'
print(f"the intial dictionary is {dict_1}")
for name,age in dict_1.items():
     print(f"{name} : {age}")
#
# print(dict_1.get('name'),':',dict_1.get('age'))

# dict_4=[{
#      'name':"diren",
#      'age':24,
#      "email":"abc@gmail.com"
#       },
# dict_5={
#      'name':"dooo",
#      'age':24,
#      "email":"abc@gmail.com"
# }
# dict_6={
#      'name':"hiren",
#      'age':24,
#      "email":"abc@gmail.com"
# }
# ]

#string operation

string1='apple'
string1.startswith('la')
string1.find('apple')



















