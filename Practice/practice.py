# s='hello'
# print(s[1])
# print(s[::-1])
# print(s[-1])
# print(s[4])
# print(2<3>10)

# mylist = [(1,2),(3,4),(5,382)]
# for (a,b) in mylist:
#     print (b,a,sep=',',)

# x=0
# while x<3:
#     print(f'The current value of x is {x}')
#     x=x+1
#     x+=1
# abc="HELLLOOO"
# for i in abc:
#     if i == 'E':
#         break
        # continue
    # print(i)


# count=0
# for i in 'abcdefg':
#     print('at index {} the letter present is {}'.format(count,i))
#     count+=1
#     if count ==3:
#         break
    

# word = 'abcde'
# for i in enumerate(word):
#     print(i)


#zip function will join two or more lists together and return the output in the form of tuple
# l1={1,2,3,5,6}     #won't give the error will go till the shortest list 
# l2=['a','b','r','x','czt']
# zip(l1,l2)
# for i in zip(l2,l1):
#     print(i)

# print(list(zip(l1,l2)))   #will return the output in the form tuple only but in a list 

# in function
#  max,min 
# import random
# from random import shuffle 
# mylist = [1,2,3,4,6,7,9,10]
# print(random.shuffle(mylist))

# from random import randint
# print(randint(1,3))

a="i am a human"
b=[]
for i in a:
    c=b.append(i)
print(c)

# import math
# a=[num**2 for num in range(0,10) if num%2==0]
# print(a)

# celcius=[23,45,34,49]
# fahrenheit= [((9/5)*temp+32) for temp  in celcius]
# print(fahrenheit)


# st='Print only the words that starts with s in this sentence'
# for i in st.split():
#     if i[0].lower()=='s':
#         print (i)
# # else:
#     print("There is no letter that starts with capital S")

# for i in range(10):
#     print (i,sep="-")
    # print ('\n',i,end=",")



# n=int(input("Enter the number of times u want to calculate"))
# for i in range(n):
#     a=eval(input("Enter a number "))
#     b=eval(input("Enter another number "))
#     opr=input("Enter which function u want to opreate among +,/,*,- : ")
#     if opr == '+':
#         print ("The sum of",a,"and", b ,"is ",a+b )
#     elif opr == '-':
#         print ("The difference of",a,"and",b,"is",a-b)
#     elif opr == '*':
#         print("The product of",a,"and",b,"is",a*b)
#     elif opr == '%':
#         print("The division of",a,"and",b,"is",a%b)
#     else:
#         print("Wrong input") 


# a= input("Enter a string")
# for i in len(a):
#     if i=="S":
#         print(i)
#     break




# import pandas as pd
# data = {'Roll No.':['1','2','3'],'Name':['Aman','Rajesh','Vishal'],'Result':['Pass','Pass','Fail']}
# print(pd.DataFrame())
# print(pd.DataFrame(data))
