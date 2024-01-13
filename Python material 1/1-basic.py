"""
print("Hello")
import val
print(val.a)
print(100)
print(type(100))
print('Hello Friends')
print(type('Hello Friends'))
print(2.10)
print(type(2.10))
print(True)
print(type(True))
name='Riya'
print('Hello',name)
print('Hello','name')
print(name)
name1="Ray"
print(name1)
print("name1")
#Variable as integer
x=2
print(x)
#Add two numbers
a=10
b=20
c=a+b
print(c)
num1=100
num2=23
out=num1+num2
print(out)
#Find the area
width=5
height=5*4
area=width*height
print(area)
x=input(2)
y=input(3)
print(x+y)
print(type(x))
print(x+y)
x=int(input("enter num1"))
y=int(input("enter num2"))
print(type(x))
print(x+y)
print(x/y)
account=1000
name="Ria"
withdraw=200
x=int(input("account"))
y=int(input("withdraw"))
print(x-y)
"""  
"""
#practice
print(type("true"))
print(type(True))
print(True)
name="Ray"
print("Hello",name)
print("hello","name")
x=input(2)
print(type(x)) 
x=input("name1")
print(type(x))
"""
"""
x=float(input("enter a number between 0.0 to 1.0"))
if(x>0.5):
    print("pass")
else:
    print("fail")
no=int(input("enter a number"))
if(no%3==0 and no%5==0):
    print("fizzbuzz")
elif(no%3==0):
    print("fizz")
elif(no%5==0):
    print("buzz")
else:
    print(no)
"""
"""
total_percentage=float(input("enter a number between 0.0 to 1.0: "))
if(total_percentage>1.0 and total_percentage<0.0):
    print("please enter the total percentage")
elif(total_percentage>=0.9):
    print("A") 
elif(total_percentage>=0.8):
    print("B")
elif(total_percentage>=0.7):
    print("C")
elif(total_percentage>=0.6):
    print("D")
elif(total_percentage<0.6):
    print("fail")
elif(total_percentage==6):
    print("please enter between 0.0 to 1.0")
else:
    print("no")
a=False
b=True
print("a and b is", a and b)
print("a and b is",a or b)
print("a and b is",not a)
"""
"""
#floor
minutes=105
print(minutes/60)   
print(minutes//60)
#modulus
x=115
y=5
z=x%y
print(z)
#yeilds the right most digit of x (in base 10)
o=x%10
print(o)
# two digits
p=x%100
print(p)
"""
"""
# conditional execution
x=4
if(x>0 and x%2==0):
    print(x,"is even")
elif(x>0):
    print(x,"is odd")
else:
    print("pass")
#print values
""" 
"""
#Function
def fun_prn(a,z):
    b=a**z
    c=b/4
    return c
#main
x=1
y=2
z=3
a=x*y
c=fun_prn(a,z)
print(c)
"""
'''
#for loop
for i in range(10):
    print(i,"Hi,How are you?")
for i in range(0,10):
    print(i *2)
for i in range(0,10):
    print(2* i)
    print("Hi")
print("\n")
for i in range(10):
    val=2*i
print(val)
for i in range(1,11):
    print("2 x",i,"=",2*i)
for i in range(1,10,2):
    print(i)
for i in range(1,10,2):
    print("2 x",i,"=",2*i)
l="hello"
print(list(l))
for name in list(l):
    print(name)
for num in range(6):
    print(num)
for num in range(6):
    print(num)
print("outside the for loop",num,"\n")
l=[1,2,3,4]
for num in range(len(l)): #for integer range
    print(l[num])
print("hey\n")
#store strings as a list
l=['hey','hi','ola','hello']
for name in l:
    print(name,end=",")
print("out of loop\n")
#for -sum of nummbers
num=0
for i in range(5):
    num=num+i
    print("adding first",i,"numbers gives",num)
'''
"""
num=num+i
0=0+0
1=0+1
3=1+2
6=3+3
10=6+4
"""
'''
#fizz buzz for loop
start=int(input("enter the start number="))
stop=int(input("enter the stop number="))
for no in range(start,stop+1):
    if(no%3==0 and no%5==0):
        print("fizz buzz")
    elif(no%3==0):
        print("fizz")
    elif(no%5==0):
        print("buzz")
    else:
        print(no)
'''
'''
#while syntax
c=0
while(c<9):
    print("count",c)
    c=c+1
print("Thank you")
'''
'''
x=int(input("enter a start count:"))
y=int(input("enter a stop count:"))
while(x<y):
    print("count",x)
    x=x+1
print("Thank you")
'''
'''
c=1
n=1
while(c==1):
    print("student with roll_no ",n,"say come in")
    c=int(input("if c=1 enter/ c=0 exit"))
c=1
n=1
while(c==1):
    print("student with roll_no ",n,"say come in")
    n=n+1
    c=int(input("if c=1 enter/ c=0 exit"))
''' 
'''
c=1
n=1
'''
'''
c=1
while(c==1):
    n=int(input("enter roll_no:"))
    print("student with roll_no ",n,"say come in")
    c=int(input("if c=1 enter/ c=0 exit"))
''' 
'''
c=1
while(c==1):
    n=int(input("enter roll_no:"))
    print("student with roll_no ",n,"say come in")
    n=n+1
    c=int(input("if c=1 enter/ c=0 exit"))
'''
'''
#fizzbuzz
def fizzbuzz_play(no):
    if(no%3==0 and no%5==0):
        print("Fizzbuzz")
        return='fzbz'
    elif(no%3==0):
        print(Fizz)
        return('fz')
    elif(no%s==0):        
        print(Buzz)
        return='bz'
    else:
        print(no)
        return('no')
    
    
ch="y"
fizzbuzz=0
fizz=0
buzz=0
missed=0
print("fizz buzz activity")
while(ch==y):
    num=int(input("enter a number="))
    winloose=fizzbuzz_play(num)
    if winloose=='fz':
        fizz+=1
    elif winloose='bz':
        buzz+=1
    elif winloose=='fzbz':
        fizzbuzz+=1
    else:
        missed+=1
    ch=input('Do you want to continue playing:(y/n')
    if ch=="n":
        print("Congratulations,your score is\n fizzbuzz=%d,fizz=%d,buzz=%d,missed=%d",fizzbuzz,fizz,buzz,missed)    
'''
'''
no=7
1           2
n0%3==0 and n0%5==0  false and false=false
1
no%3==0
2
no%5==0  
''' 
'''
#counting using range
names=['Ray']




'''
'''
#for loop
for i in range(2):
    #print("value of j",i)
    for j in range(10,13):
        #print("value of j",j)
        print("value of i ..j",i,"..",j)
'''
'''
for i 2
    for j 10,13
iteration 1
    i 0
    j 10
        print i,j 0 10
    
    i=0
    j=11
    pr i,j 0,11
    
    i=0
    j=12
    pr 0 12
iter 2
    i 1
    j 10
    pr 1 10
i 1
j 11
pr 1 11
i 1
j12 
pr 1 12
'''
'''
#multiplications of numbers 5 and 6 using nested for loop
for i in range(5,7):
    #print("value of i",i)
    for j in range(1,11):
        #print("value of j",j)
        print("value of i*j=",i,"*",j,"=",i*j)
'''
'''
#multiplication using while   
i=5
while i<=6:
    j=1
    while j<=10:
        print("value of i*j=",i,"*",j,"=",i*j)
        j+=1 #j=j+1
    i+=1
    print("\n")
'''
'''
#Data types
#\n \a \t
#string example
#hello world
#012345678910
#-11-10-9-8-7-6-5-4-3-2-1
String="Hello"
print(String[0])
#methods
variable="Heera is here."
l=len(variable)
print(l)
print(len(variable))
cnt=variable.count("e")
print("count of the string is",cnt)
centre_variable=variable.center(24)               
print("variable center:",centre_variable)
strg="Heera is Here."
capitalized_strg=strg.capitalize()
print(strg)
print(capitalized_strg)
'''
#string operations
#assignment=
strg1="hello"
strg2='hello'
strg3='''hello'''
''' 
print(strg1)
print(strg2)
print(strg3)
#concatenate +
strg1="hello"
strg2="world"
strg1_strg2=strg1+strg2
print(strg1_strg2)
'''
'''
#repetition operator *
strg1="helloworld"
print(strg1*2)
print(strg1*3)
print(strg1*4)
print(strg1*5)
'''
'''
variable="Hello world"
print(variable[0:10])
print(variable[0:10+1])
print(variable[-11:-1])
print(variable[2:5])
print(variable[0:11])
print(variable[-1])
'''
'''
#string comparision operator== !=
strg1="hello"
strg2="hello,world"
strg3="hello,world"
strg4="world"
print(strg1==strg4)
print(strg2==strg3)
print(strg1!=strg4)
print(strg2!=strg3)
#membership operator in not in
strg1="helloworld"
print("w" in strg1)
print("W" in strg1)
print("t" in strg1)
print("t" not in strg1)
print("hello" in strg1)
print("Hello" in strg1)
print("hello" not in strg1)
'''
#presidence operation
#format() function 
'''
num1=20
print(id(num1))#identity of num1
num2=30-10
print(id(num2))
list1=[5,3.5,"hello"]
list1[1]=10
print(list1)
dict1={'fruit':'apple','climate':'cold','price':120}
print(dict1['fruit'])
'''
#* implies import all or every thing
'''
num1=1
result='even' if num1%2==0 else 'odd'
print(result)
'''
'''
names=['ray','rim','stoe','sini']
for i in range(len(names)):
    print(names[i])
string="python is awesome,isn't it"
substring='is'
count=string.count(substring)
print(count) #check for isn't it
import re
txt='the rain in spain'
x=re.search("^the.*spain$",txt)
if x:
    print("yes! we have a match")
else:
    print("no match")
'''
'''
x=int(input("Enter a number:"))
if(x%7==0):
    print("Yay,its Maserati!")
else:
    print("Oh,No!,Better Luck Next Time")
'''
'''
#Error 1: don't give print(cat) statement in main function
def print_twi(cat):
    print(cat)
    print(cat)
def cat_twi(part1,part2):
    cat=part1+part2
    print_twi(cat)
line1='Hello'
line2='enjoy your day'
cat_twi(line1,line2)
#print(cat) name error
def print_twice(brant):
    print(brant)
    print(brant)
print_twice('hello')
def print_twice(brant):
    print(brant)
    print(brant)
print_twice(42)
'''
'''
n=9
for i in range(n,0,-1):
    print(i,end=" ")
    for j in range(i-1,0,-1):
        print(j,end=" ")
    print("")
'''
'''
#02-11-2022
#lists
lst=[1,2,3,4]
print(lst)
lst=["hi","hello"]
print(lst)
lst=[1,'hi',2,'hello']
print(lst)
print(lst[0])
#list slicing
lst=[1,'hi',2,3,'hello',4]
print(lst[2:5])
print(lst[2:5:1])
lst=[1,'hi',2,3,'hello',4]
print(lst[ : :-1])
'''
'''
lst=[1,'hi',2,3,'hello',4]
print(lst[-4:-2])
lst=[1,'hi',2,3,'hello',4]
print(lst[-6:-1])
'''
'''
#list methods
#sort is for ascending order for descending order we have to use reverse one
num=[7,8,9,10,11]
print(num)
print(len(num))
print(max(num))
num.reverse()
print(num)
#if once we reversed the num then it will be in reverse order furhter to conert normal again store it in other variable or print again
num.append(3)
print(num)
print(sum(num))
num=[7,8,9,10,11]
print(num.index(7))
num.insert(3,0)#here we are inserting 0 at 3rd index
print(num)
num.sort()
print(num)
'''
'''
str=['hi','hello','apple','book','good']
print(str)
print(len(str))
print(max(str))
str.reverse()
print(str)
str.append("sara")
print(str)
print(str.index("sara"))
str.insert(3,"hey")
print(str)
str.sort()
print(str)
'''
'''
#Tuples
t='a','b','c','d','e'
print(t)
t=('a','b','c','d','e')
print(t)
#tuple-single element
t1='a',#a comma after the character 
print(type(t1))
t2=("a")
print(type(t2))
t3=tuple("a")
print(type(t3),t3)
t=tuple('hello')
print(t)
t=('a','b','c','d','e')
print(t[0])
#cannot modify tuple
t[0]='A'#o/p typeerror:tuple object does not support item assignment
#but we can replace one tuple with another
t=('A',)+t[1:]
print(t)
#one missed like [:]
'''
'''
addr='rin@stan.org'
unname,domain=addr.split("@")
print("unname=",unname,"\n","domain=",domain)
x,y=(3,4)#x will be bound to 3 and y to 4
print(x,y)
a,b,c='xyz'#a will be bound to x, b to y and c to z
print(a,b,c)
#tiple as return values
t4=divmod(6,3)
print(t4) #o/p (2,0) quotient and remainder
#store quotient and remainder separately
qu,re=divmod(6,3)
print(qu,re)
#function that returns a tuple
def min_max(t):
    return min(t),max(t) #max and min are in built functions
ch=("ron","hey")
print(min_max(ch))
num=(100,12,43.3,19,4)
print(min_max(num))#all functions are not used by both string and integers
#modify
mi,ma=min_max(num)
print("minimum=",mi,"maximum=",ma)
'''
'''
#variable-length argument tuples
def printarg(*args):
    print()
    print(args)
printarg(1,2.0,'3')
t5=(15,3)
print(divmod(*t5))
'''
'''
#03-11-2022
#Dictionary
month=dict()
print(month)
month={'jan':1,'feb':2,'mar':3,'apr':4,'may':5}
print(month)
di=month['apr']-month['jan']
print('apr and jan are',di,'months apart')
month['jun']=6
print(month)
print(month['jun'])
month={1:'jan',2:'feb',3:'mar',4:'apr',5:'may'}
print("the fifth month is"+month[5])#it will give error if month={'jan':1,'feb':2,'mar':3,'apr':4,'may':5}
#dictionaries and loop
month={'jan':1,'feb':2,'mar':3,'apr':4,'may':5}
for key,val in month.items():
    print(key,"=>",val)
'''
'''
#snake and ladder
import random
def snakes_and_laders(x):
    dict_sal={4:16,12:23,18:22,21:3,24:7,26:37,35:9,42:61,49:51,50:11,53:15,55:74,60:23,75:44,82:98,85:95,88:92,89:48,93:25,97:65,99:58}
    print("If the value hits snake or ladder",dict_sal.get(x,x))
    return dict_sal.get(x,x)
def roll_die(x):
    #time.sleep(sleep_between_actions)
    x=random.randint(1,dice_face)
    print("The dice value is",x)
    return x
#sleep_between_actions=1
dice_face=6
p1=0
while True:
    a=roll_die(p1)
    p1=p1+a
    print("After the roll of dice player is at",p1)
    p1=snakes_and_laders(p1)
    print("Player is at",p1)
    if p1>=100:
        print("Player wins!")
        break
'''
'''
#method
month={'jan':1,'feb':2,'mar':3,'apr':4,'may':5}
print(month.keys())
keys=[]
for e in month:
    keys.append(e)
keys.sort()
print(keys)
print("jan" in month)
#set()
mut={10,4,[1,2]}#gives error
num=set([1,2,3])
print(num)
print(num[1:])#gives type error bcoz we don't have index
#if error has to be thrown avoid using discard
#POP
numb={1,2,3,4,5,6,7}
print(numb.pop())#pops small number 
'''
'''
#04-11-2022
#recursion
def countdown(n):
    if n<=0:
        print("Out of function!")
    else:
        print(n)
        countdown(n-1)
countdown(3)
def print_n(s,n):
    if n<=0:
        return 
    print(s)
    print_n(s,n-1)
print_n('hey',3)
#Infinite recursion
def recurse():
    recurse()#no exiting condition
recurse()
#keyboard input
text=input()
print(text)
name=input("What is your name?\n")
print(name)
#Recursive factorial
#factorial of a number using recursion
def recur_factorial(n):
    if n==1:
        return n
    else:
        return n*recur_factorial(n-1)
num=int(input("Enter a number:"))#last in first out
#check if the number is negative
if num<0:
    print("Sorry factorial does not exist for negative numbers")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of",num,"is",recur_factorial(num))
#Recursive binary search
#binary search does not work if the data is not sorted
def binary_search(list1,low,high,n):
    #check base case for the recursive function
    if low<=high:0
        mid=(low+high)//2
    #if element is available at the middle itself then return the its index
        if list1[mid]==n:
            return mid
#if the element is smaller than mid value,then search moves left sublist1
        elif list1[mid]>n:
            return binary_search(list1,low,mid-1,n)
#else the search moves to the right sublist1
        else:
            return binary_search(list1,mid+1,high,n)
    else:
#element is not available in the list1
        return -1
#main
list1=[6,12,17,23,38,45,77,84,90]
n=45
#function call
res=binary_search(list1,0,len(list1)-1,n)
if res!=-1:
    print("Element is pressent at index",res)
else:
    print("Element is not present in list1")
'''
'''
#07-11-2022
#Lambda function
store=lambda x:"Even_no" if x%2==0 else "Odd_no"
print(store(10))
#difference between lambda function and normal or def defined function
def cube_of(num):
    return num*num*num
print("Calling a function:",cube_of(6))
def cube_la(num): return num*num*num
print("Using lambda:",cube_la(6))
#lambda function with list comprehension
find_even=[lambda arg=x:arg*10 for x in range(1,5)]
for item in find_even:
    print(item())
#lambda function with if-else
Max=lambda num1,num2: num1 if(num1>num2) else num2
print(Max(1,2))
#lambda with filter; filter(function,sequence(not dictionary));sequence:list,tuple,string;sets are not sequences
li=[7,1,5,9,21,22,25,44,12]
output=list(filter(lambda x:(x%2!=0),li))
print(output)
li=(1,2,3,4,5)
output=tuple(filter(lambda x:(x%2!=0),li))
print(output)
#lambda() function with map()
#r=map(func,seq)
li=[3,7,9,20,70]
modified=list(map(lambda x:x*2,li))
print(modified)
animals=['rin','ray','roy']
uppered_animals=list(map(lambda animal:animal.upper(),animals))
print(uppered_animals)
#lambda() function with reduce()
#reduce(func,seq)
import functools
op=functools.reduce(lambda x,y:x+y,[47,11,42,13])
print(op)
#cartesian product
#itertools.product()
import itertools
l1=['a','b','c']
l2=['x','y','z']
p=itertools.product(l1,l2)
for v in p:
    print(v)
#or
for v1,v2 in p:
    print(v1,v2)
from itertools import permutations
txt=["".join(i) for i in permutations('SKIN')] 
print(txt)
'''
#09-11-2022
#File handling
#open a file in python
#syntax of the file open function
#file_object=open(file_name[,access_mode][,buffering])
#read
'''
read([n])
readline([n])
readlines()
here n is the no.of bytes
'''
'''
#read the entire file
#a file named "file", will be opened with the reading mode
file=open('file.txt','r')
#print(file.read(2))
#print(file.readline(2))
#print(file.readline())
#print(file.readlines())
'''
'''
line_number=int(input("Enter a number:"))
fo=open("file.txt","r")
currentline=1
for line in fo:
    if(currentline==line_number):
        print(line)
        break
    currentline=currentline+1
    print(currentline)
'''
'''
def find_file(vegetable):
    v_file=open("basic-veg-file.txt")
    vege=v_file.read()
    if vegetable in vege:
        return "veg in list"
    else:
        return "veg not in list"
addr=["Harriata","1378","Atlanta"]
secret_key={"Riya":11,"Sonit":22}
print("complete address of shop")
print(addr)
print("first 2 values stored in address of shop")
print(addr[0],addr[1])
secret_k=int(input("Enter your secret code\t"))
if secret_k in secret_key.values():
    print("Correct secret code\n")
    veg=input("Enter vegetable name without spaces,to check if vegetable exist")
    print(find_file(veg))
else:
    print("Wrong secret code,you are not authorised to login")
'''
'''
#10-11-2022
#The write() file method
#Python code to create a file
file=open('file1.txt','w')
file.write("This is the write command\n")
file.write("It allow us to write in a particular file")
file.close()
with open("file1.txt") as input:
    with open("b(class).txt","w") as output:
        for line in input:
            output.write(line)
def main():
    ##Append-adds at last
    file=open("test.txt","a+")
    for i in range(2):
        file.write("Append line %d\r" %(i+1)) #this %d is for formating
    file.close()
fruits=["Apple\n","Orange\n","Grapes\n","Watermelon"]
##write-overwrites
file=open("test.txt","w")
file.writelines(fruits)
file.write("\n")
file.close()
main()
#functions are objects
def shout(text):
    return text.upper()
print(shout("Hello"))
yell=shout 
print(yell("Hello"))
def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def greet(func):
    #Storing the function in a variable
    greeting=func("""Hi,I am created by a function passed as an argument.""")
    print(greeting)
greet(shout)
greet(whisper)
#functions can return another functions
def create_adder(x):
    def adder(y):
        return x+y
    return adder 
add_15=create_adder(15)
print(add_15(10))
'''
'''
#practice test-2 question
def power(a,b):
    if b == 0:
        return 1
    return a*power(a,b-1)
print(power(2,3))
'''
'''
Name: Chimirala Kowstubha
Application number: JUUG22BTECH56830
Course: AI&DE
Section: A
'''
'''
#Recursive binary search
def binary_search(list1,low,high,n):
    if low<=high:
        mid=(low+high)//2
        if list1[mid]==n:
            return mid
        elif list1[mid]>n:
            return binary_search(list1,low,mid-1,n)
        else:
            return binary_search(list1,mid+1,high,n)
    else:
        return -1
list1=[6,12,17,23,38,45,77,84,90]
n=45
res=binary_search(list1,0,len(list1)-1,n)
if res!=-1:
    print("Element is pressent at index",res)
else:
    print("Element is not present in list1")
'''
'''
Name: Chimirala Kowstubha
Application number: JUUG22BTECH56830
Course: AI&DE
Section: A
'''
'''
#Non-recursive binary search
def non_recursive_binary_search(list1,n):
    low=0
    high=len(list1)-1
    mid=0
    while low<=high:
        mid=(low+high)//2
        if list1[mid]==n:
            return mid
        elif list1[mid]>n:
            high=mid-1
        else:
            low=mid+1
    return -1
list1=[6,12,17,23,38,45,77,84,90]
n=45
res= non_recursive_binary_search(list1,n)
if res!=-1:
    print("Element is pressent at index",res)
else:
    print("Element is not present in list1")
'''
'''
#15-11-2022
#Script,Module,Package and Library
from add import add#not working
output=add(7,8)
print(output)
#Module
from math import pow
val=pow(2,3)
print(val)
#package
import math
print("generates a print")
#Module-time
import time
ticks=time.time()
print("Number of ticks since 12:00am,january1,1970:",ticks)
#import time
localtime=time.localtime(time.time())
print("Local current time:",localtime)#tm_wday=day(Monday=0),isdst:daylightsaving
#Module calender
import calendar
cal=calendar.month(2008,1)
print("Here is the calendar:")
print(cal)
from datetime import *
m=str(input(""))
#2022-11-15 11:00
base=datetime.strptime(m,"%Y-%m-%d %H:%M")
print(base)
n=int(input(""))
for i in range(0,n):#modify (1,n)
    print(timedelta(days=i))
    #0:00:00
    print(base+timedelta(days=i))
#tell() method
text=["Hello\n","Hi\n","Python\n"]
file=open("c.txt","w")#if we use a+ cursor position will be different everytime
file.writelines(text)
print("Where the file cursor is:",file.tell())
file.close()
#seek(),seek(offset)
#0:beginning,1:current,2:end
text=["Hello\n","Hi\n","Python\n"]
file=open("c.txt","w")#if we use a+ cursor position will be different everytime
file.writelines(text)
print(file.seek(0))
file.close()
file=open("c.txt","rb")
#sets reference point to tenth
#position to the left from end
file.seek(-10,2)#seek(reference,offset)
print("Cursor Position:",file.tell())
file.close()
'''
#Numpy
#Matrices
#matrics
#[(0)1(0) 2(1) 3(2)]
#[(1)4    5    6]2x3 matrix(2rows,3 columns)
#Matrix:Multiplication
'''
#3*3 matrix with indices #Axis 0 can be x axis,Axis 1 can be y axis
             axis 1
          (0)  (1) (2)
       (0)0,0 0,1 0,2
axis 0 (1)1,0 1,1 1,2
       (2)2,0 2,1 2,2
'''
'''
#10-11-2022
#NUMPY 1D
import numpy as np
values=np.array([1,2,3,4,5])
print(values)
#Numpy 2D
#import numpy as np
values=np.array([[1,2,3],[4,5,6]])#these have to be of same length
print(values)
#npArray and list
#import numpy as np
my_arr=np.arange(1000000)#arange takes values from 0 to n-1
print(my_arr)
my_list=list(range(1000000))#o/p [0,1,2,3,4,5,6,7,8,9,10,11,.....999999] sometimes it will print all the numbers
print(my_list)
#Numpy for loop
import numpy as np
my_arr=np.arange(10)#1000000(value taken by mam)
for x in range(1):#10(Value taken by mam)
    my_arr2=my_arr*2
print(my_arr2)
#Numpy and list
import numpy as np
from IPython.terminal.embed import InteractiveShellEmbed
ipshell=InteractiveShellEmbed()
ipshell.dummy_mode=True
my_arr=np.arange(1000000)
ipshell.magic("%time for _ in range(10):my_arr2=my_arr*2")
#list
my_list=list(range(100))
for _ in range(10):
    my_list2=my_list*2
print(my_list2)
my_list=list(range(100))
ipshell.magic("%time for _ in range(10):my_list2=[x*2 for x in my_list]")
'''
#practice for mini project
'''
Name: Chimirala Kowstubha
Application number: JUUG22BTECH56830
Course: AI&DE
Section: A
'''
'''
list1=[1,20,3,60,9]
choice=0
while True:
    print("The list 'list1' has the following elements",list1)
    print("\nL I S T  O P E R A T I O N S")
    print("1. Append an element")
    print("2. Insert an element at the desired position")
    print("3. Append a list to a given list")
    print("4. Modify an existing element")
    print("5. Delete an existing elemet element with a given value")
    print("6. Sort the list in ascending order")
    print("7. Sort the list in descending order")
    print("8. Display the list")
    print("9. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        element=int(input("Enter the element to be appended:"))
        list1.append(element)
        print("The element has been appended\n")
    elif choice==2:
        element=int(input("Enter the element to be inserted:"))
        pos=int(input("Enter the position:"))
        list1.insert(pos,element)
        print("The element has been inserted\n")
    elif choice==3:
        list2=eval(input("Enter the elements separated by commas:"))
        list1.extend(list(list2))
        print("The list has been appended\n")
    elif choice==4:
        a=int(input("Enter the position of the element to be modified:"))
        if a<len(list1):
            newelement=int(input("Enter the new element:"))
            oldelement=list1[a]
            list1[a]=newelement
            print("The element",oldelement,"has been modified\n")
        else:
            print("Position of the element is more than the length of list")
    elif choice==5:
        b=int(input("Enter the element to be deleted:"))
        if b in list1:
            list1.remove(b)
            print("The element",b," has been deleted")
        else:
            print("Element",b,"is not present in the list")
    elif choice==6:
        list1.sort()
        print("The list has been sorted in ascending order")
    elif choice==7:
        list1.sort(reverse= True)
        print("The list has been sorted in descending order")   
    elif choice==8:
        print("The list is:",list1)
    elif choice==9:
        print("Exit")
        break
    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue......")
        ch=input("")
'''
#mini project-1
'''
Name: Chimirala Kowstubha
Application number: JUUG22BTECH56830
Course: AI&DE
Section: A
'''
'''
dict1={}
choice=0
while True:
    print("1. Add a phone number")
    print("2. Print a phone number")
    print("3. Delete a phone number")
    print("4. Search a phone number")
    print("5. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        x=int(input("Enter how many phone numbers you want to add:"))
        for i in range(x):
            a=input("Enter name:")
            b=int(input("Enter phone number:"))
            dict2={}
            dict2[a]=b
            dict1.update(dict2)
            print("Phone number of",a," is added to the dictionary")
        print("Dictionary after adding the phone numbers is\n",dict1)
    elif choice==2:
        c=input("Enter the name:")
        if c in dict1:
            print("The phone number of",c,"is",dict1[c])
        else:
            print("The phone number which you are searching is not",end=" ")
            print("there in the dictionay\nEnter valid name")   
    elif choice==3:
        d=input("Enter a name:")
        del dict1[d]
        print("Dictionary after deleting the phone number of",d,"is",dict1)
    elif choice==4:
        e=input("Enter name:")
        print("The phone number which you are searching is",dict1.get(e))
    elif choice==5:
        print("Exit")
        break
    else:
        print("Choice is not valid")
        print("\n\nPress any key to continue......")
        ch=input("")
'''
#Mini project-2
'''
Name: Chimirala Kowstubha
Application number: JUUG22BTECH56830
Course: AI&DE
Section: A
'''
'''
file=open("dict.txt","w")
dict1={}
x=int(input("Enter how many phone numbers you want to add:"))
for i in range(x):
    a=input("Enter name:")
    b=int(input("Enter phone number:"))
    dict1[a]=b
file.write(str(dict1))
file.close()
file= open('dict.txt', 'r')
print(file.read())
choice=0
while True:
    print("1.Adding a phone number")
    print("2.Printing a phone number")
    print("3.Deleting a phone number")
    print("4.Searching a phone number")
    print("5.Exit")
    choice=int(input("Enter your choice between 1-5:"))
    if choice==1:
        file=open("dict.txt","w")
        dict2={}
        a=(input("Enter name:"))
        b=int(input("Enter phone number:"))
        dict1[a]=b
        dict2.update(dict1)
        file.write("The dictionary after appending is: ")
        file.write(str(dict1))
        file.close()
        file= open('dict.txt', 'a+')
    print(file.read())
    if choice==2:
        file=open("dict.txt","w")
        name=input("Enter the key you want to print:")
        file.write("The phone number is printed: ")
        file.write(str(dict1.get(name)))
        file.close()
        file= open('dict.txt', 'a+')
    print(file.read())
    if choice==3:
        file=open("dict.txt","w")
        x=(input("Enter the key you want to delete:"))
        del dict1[x]
        file.write("The dictionary after deleting : ")
        file.write(str(dict1))
        file.close()
        file= open('dict.txt', 'a+')
    print(file.read())
    if choice==4:
        file=open("dict.txt","w")
        y=input("Enter a key you want to search:")
        if y in dict1.keys():
            result="Present in the dictionary" 
        else:
            result="Not Present in the dictionary"
        file.write("The phone number that is searched ")
        file.write(str(dict1.get(y)))
        file.write(" is ")
        file.write(str(result))
        file.close()
        file= open('dict.txt', 'a+')
    print(file.read())
    if choice==5:
        file=open("dict.txt","w")
        file.write("Exit")
        file.close()
        file= open('dict.txt', 'a+')
        break
'''
'''
#17-11-2022
#The NumPy ndarray:A Multidimensional Array Object
import numpy as np
data=np.random.randn(2,3)
print(data)
print(data*10)
print(data)
print(data+data)
print(data.dtype)
#creating ndarrays
import numpy as np
data1=[6,7.5,8,0,1]
arr1=np.array(data1)
print(arr1)
#creating ndarrays
data2=[[1,2,3,4],[5,6,7,8]]#equal length lists
arr2=np.array(data2)
print(arr2)
print(arr2.ndim)#implies 2d array
print(arr2.shape)
print(arr2.dtype)
print(np.zeros(10))#1D
print(np.zeros((3,6)))#2D
#Data types for ndarrays
arr1=np.array([1,2,3], dtype=np.float64)
print(arr1,arr1.dtype)
arr2=np.array([1,2,3], dtype=np.int32)
print(arr2,arr2.dtype)
#convert or cast
import numpy as np
arr=np.array([1,2,3,4,5])
print(arr,arr.dtype)
float_arr=arr.astype(np.float64)
print(float_arr,float_arr.dtype)
numeric_strings= np.array(['1.25','-9.6','42'],dtype=np.string_)
print(numeric_strings.astype(float))
print(numeric_strings.dtype)
#basic indexing and slicing
import numpy as np
arr=np.arange(10)
print(arr)
print(arr[5])
print(arr[5:8])#8 is not included
arr[5:8]=12
print(arr)
arr_slice=arr[5:8]
print(arr_slice)
arr_slice[1]=12345
print(arr_slice)
print(arr)
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d)
print(arr2d[2])#or [2,:]or[2:,:]
print(arr2d[0][2])#or arr2d[0,2]
#2D slicing
arr2d=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr2d[:2])
print(arr2d[:2,1:])
'''
'''
#21-11-2022
#Scipy(library used for Scientific computing)#(Scientific Python)
#Scipy sparce(Sparce means very few numbers)
import numpy as np
from scipy.sparse import csr_matrix
arr=np.array([[0,0,3,0,4],[0,0,5,7,0],[0,0,0,0,0],[0,2,6,0,0]])
print(csr_matrix(arr).data)
#Scipy integrate
#single integration
#f(x)=2^x+1(find the area between limits 0 and 1)
from scipy.integrate import quad
def f(x):
    print(x)#to understand what value x is taking and how many values it is taking
    return 2**x+1
res=quad(f,0,1)#here 0 is lower limit 1 is upper limit#once check with -1 as lower limit
print(res)#Res gives res and err as output(err is error computation)
#Scipy optimize
import numpy as np
import scipy.optimize as opt
f=lambda x:x**2+1 #a x^Tx x+0*x+1
x=np.linspace(-2, 2)
print(x,f(x))
sol=opt.minimize_scalar(f)
#print(sol)#mam didn't say to print sol
'''
'''
#23-11-2022
#Pandas
#1.Series
import pandas as pd
obj=pd.Series([4,7,-5,3])
print(obj)
print(obj.values)
obj2=pd.Series([4,7,-5,3],index=['d','b','a','c'])
print(obj2)
print(obj2.index)
print(obj2['a'])
obj2['d']=6
print(obj2[['c','a','d']])#2 sq brackests because it is like 2d (if it is 3d we have to put 3 sq bracket) here if we use only one bracket it will give error
print(obj2[['a','b','c','d']])
#Using NumPy functions
print(obj2[obj2>0])
print(obj2*2)
import numpy as np
print(np.exp(obj2))
obj3=pd.Series([1,1,2,3])
print(np.exp(obj3))
print('b' in obj2)
print('e' in obj2)
sdata={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
obj4=pd.Series(sdata)
print(obj4)
states=['California','Ohio','Oregon','Texas']
obj4_1=pd.Series(sdata,index=states)
print(obj4_1)
#check for null values
print(pd.isnull(obj4_1))
obj4_1.name='population'
obj4_1.index.name='state'
print(obj4_1)
print(obj)
obj.index=['Bob','Steve','Jeff','Ryan']
print(obj)
#as tuple
obj5=pd.Series((1,1,2,3))
print(obj5)
#Series splitting
print(obj[1])
print(obj[1:3])
#Pandas Data Frame
data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],'year':[2000,2001,2000,2001,2002,2003],'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}#we have to take equal no.of values in state,year,pop
frame=pd.DataFrame(data)
print(frame)
frame=pd.DataFrame(data,columns=['year','state','pop'])
print(frame)
frame2=pd.DataFrame(data,columns=['year','state','pop','debt'])
print(frame2)
#modify index
frame2=pd.DataFrame(data,columns=['year','state','pop','debt'],index=['one','two','three','four','five','six'])
print(frame2)
#display column names
print(frame2.columns)
print(frame2['state'])
print(frame2.year)#note that the returned series have the same index as the DataFrame
print(frame2.loc['three'])
frame2['debt']=16.5
print(frame2)
frame2['debt']=np.arange(6.)
print(frame2)
#Inserting missing values in any location
val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame2['debt']=val
print(frame2)
frame2['eastern']=frame2.state=='Ohio'#'==' which is checking for 'Ohio'
print(frame2)
#removing a column
del frame2['eastern']
print(frame2)
#transpose(not in syllabus)
#Graph
import matplotlib.pyplot as plt
x=[2,6,10,19]
y=[3,6,12,17]
plt.plot(x,y,'c',linewidth=2)#(x,y,color cyan,linewidth)
plt.show()
#bar graph
import matplotlib.pyplot as plt
x=[2,6,10,19]
y=[3,6,12,17]
plt.bar(x,y,align='center',label='sample1',color='green')#(x,y,align center,label,color green)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Bar Graph')
plt.show()
#plt.savefig("graph.png") use it in repel.it
import matplotlib.pyplot as plt
x=[2,6,10,19]
y=[3,6,12,17]
x2=[7,8,9,12,16]
y2=[7,8,13,16,7]
plt.plot(x,y,'b--',label='one',linewidth=2)#(plt.plot(x,y,blue dash,label one,line width)
plt.plot(x2,y2,'kd',label='two')#(plt.plot(x2,y2,black diamond,label)(kd:black diamond(d-diamond,k-black))
plt.title("Chart")
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()#to display labels we use legend
plt.show()
#simple plot
import matplotlib.pyplot as plt
import numpy as np
data=np.arange(10)
print(data)
plt.plot(data)#here we can give color also like(data,black) but default is blue
import matplotlib.pyplot as plt
fig=plt.figure()
ax1 =fig.add_subplot(2,2,1)
ax2 =fig.add_subplot(2,2,2)
ax3 =fig.add_subplot(2,2,3)
ax4 =fig.add_subplot(2,2,4)
'''
'''
#24-11-2022
#Data cleaning
import pandas as pd
import numpy as np
string_data=pd.Series(['aardvark','artichoke',np.nan,'avacado'])
print(string_data)
print(string_data.isnull())
string_data[0]=None
print(string_data)
print(string_data.isnull())
#Filter missing data
from numpy import nan as NA
data=pd.Series([1,NA,3.5,NA,7])
print(data.dropna())
data=pd.DataFrame([[1.,6.5,3],[1.,NA,NA],[NA,NA,NA],[NA,6.5,3.]])
print(data)
cleaned=data.dropna()
print(cleaned)
print(data.dropna(how='all'))#how='all' will only drop rows that are all NA
df=pd.DataFrame(np.random.randn(7,3))
print(df)
df.iloc[:4,1]=NA
df.iloc[:2,2]=NA
print(df)
print(df.dropna())
print(df.dropna(thresh=2))#0 and 1 row
'''
'''
#Group project
import time
from plyer import notification
if __name__ == "__main__":
    while True :
        notification.notify(
            title = "Time to drink water!!" ,
            message = "Drinking water is like washing out your insides and Adequate consumption of water helps regulate blood pressure." ,
            app_icon = "E:\pygp\icon.ico.ico",  
            timeout=10
            
        )
        time.sleep(60*30)
'''
'''
#25-11-2022
#Practice
#variable
#from math import pi
r=float(input("Enter radius:"))
pi=3.14
volume=4/3*pi*r**3
print(volume)
#cost of the book
book=24.95
#discount on the book
discount=(40*book)/100
print("Discount=",discount)
#Shipping for the first copy
shipping1=3
#shipping additional books
shipping_additional=0.75#100 cents=1 dollar
#no.of copies
no=60
total=book*no-no*discount
shipping=shipping_additional*59+shipping1
final_cost=total+shipping
print("Total discount=",no*discount)
print("Amount after discount on books=",total)
print("Total shipping=",shipping)
print("Wholesale for 60 copies with shipping=",final_cost)
def leading_space_str(s):
    print("#"*(70-(len(s))),end="")
    print(s)
x="dora"
leading_space_str(x)
'''
'''
#29-11-2022
# Class practice
m1=[[1,2,3],[1,0,2],[2,5,9]]
m2=[[4,5,6],[1,4,5],[9,4,10]]
s=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(3):
    for j in range(3):
        s[i][j]=m1[i][j]+m2[i][j]
for i in range(3):
    print(s[i])
def sumofN(num):
    if num == 1:
        return 1
    return num+sumofN(num-1)
print(sumofN(3))
'''
'''
#Cousera Practice
def greater_than(x, y):
    """Returns True if x is greater than y, otherwise False."""
    
    if x > y:
        return True
    else:
        return False

#prints general help on the function, including the docstring    
help(greater_than)
#print(greater_than.__doc__)
'''
'''
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print('')
x=input("Enter string:")
for i in range(len(x)):
    if(i%2!=0):
        print(x[i].upper(),end='')
    else:
        print(x[i].lower(),end='')
'''
'''
for i in range(4):
    x=input("")
    file=open('file1v.txt','a+')
    file.write(x)    
file.close()
'''
from sketchpy import library as lib
obj=lib.rdj()
obj.draw()