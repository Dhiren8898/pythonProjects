#python basics
'''a = 20 #integer
b = 30.69 #decimals
c='hello world'

e="helo world"
f=c+d
g=a%b
print(g)
print(f)
print(type(a))
print(type(b))
print('d is of type',type(d))
age=20
name="Dhiren"
print('{1} is {0} years old'.format(age,name))


#How to

#< > >= <= !=

if a>b:
    print("a is bigger")
else:
    print("b is greater")

#+ (plus)
#-(minus)
#*(multiply)
#**(powrer)
#print(2**3)  (2*2*2)
#/ (Divide)
p=4/3
print("divide=",p)
p=4%3
print("mod=",p)
p=7//3
print("quitiont=",p)

#bitwise operator
#&(bit-wise AND)
#|(bit-wise OR)
#^(bit-wise XOR)
#~(bit-wise invert)
#finding the area and perimeter of rectagle
length=50
breadth=20
area=length*breadth
perimeter=2*(length+breadth)
print("area of reactangle= ",area)
print("perimeter of reactangle= ",perimeter)

#finding the even and odd between 1 to 100
a=100
for i in range(0,a+1):
    if i%2==0:
        print("even number=",i)
    else:
        print("odd number=",i)'''
#use of if condition
'''a=20
if a>0:
    print("a is positive")
elif a<0:
    print("a is negative")
else:
    print("a is zero")'''
#while loop
'''a=5
while a<10:
    a+=1
    print("using while loop assingment operator",a)

#one more example for while loop
a=20
running= True
while running:
    #print("@@",a)
    get_input_value=int(input('enter a number'))
    if get_input_value>20:
        running=False
    else:
        print("the numner entered is",get_input_value)

print("done")'''
#print('dhiren'>'latin')
#for loop

'''for i in(1,10):
    if i<5:
        print("this is inside if")
    else:
        print(i)'''

'''list1=[3,4,7,8,9]
print(list)
k=' '
for i in  list1:
    print(i)
    k+=','+str(i)
print(k)

#break statement
for i in list1:
    if i==1:
        continue
    print(i)'''

#sum of all numbers in list
list1=[2,5,8,33]
total=0
for i in range(0,len(list1)):
    total=total+list1[i]
print("sum=",total)

#finding the smallest element in list
list2=[3,5,7,1,44,6,2]
list2.sort()
print("smalllest value is ", list2[0])

#finding the biggest number in list
list2=[3,5,7,1,44,6,2]
list2.sort()
print("smalllest value is ", list2[-1])

