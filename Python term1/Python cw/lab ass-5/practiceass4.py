# def sorting(filename):
#     filename=input("Enter file name")
#     infile = open(filename,"r")
#     words = []
#     for line in infile:
#         temp = line.split()
#         for i in temp:
#             words.append(i)
#     infile.close()
#     words.sort()
#     outfile = open("result.txt", "w")
#     for i in words:
#         outfile.writelines(i)
#         outfile.writelines(" ")
#     outfile.close()
# sorting("sample.txt")

# filename=input("Enter file name")
# file=open(filename,"r")
# # a=file.sort()
# file.writelines("Hello")
# # print(a)
# print(file.read())
# file.close()




# import numpy as np
# from numpy.linalg import eig
# a=np.array([[-1,3],[-2,4]])
# w,v=eig(a)
# print("Eigen values",w)
# print("Eigen vectors",v)


# import numpy as np
# arr=np.arange(1000000)
# list=list(range(1000000))
# print(arr)
# print(list)

# for a in range(10):
#     a=a*2
    # print(a)

# data=np.random.randn(2,3)
# print(data)
# data*=data
# print(data)

# data1=[6,4,5,7,8]
# arr=np.array([[1,2,3,4],[6,7,8,9,35]])
# # print(arr)
# print(arr.ndim)
# data=np.random.randn(4,5)
# print(data)

# a=np.arange(10)
# print(a)
# a1=np.array([[1,2]])
# print(a1)
# a2=np.asarray([1,2,3])
# print(a2)
# a3=np.ones,(2,object)
# print(a3)
# a4=np.ones_like()
# print(a4)

# arr1=np.array([1,2,3])#,dtype=np.float64
# print(arr1)
# print(arr1.dtype)

# a=np.array([1,2,3,4,5,6])
# print(a.dtype)
# b=a.astype(np.string_)
# print(b.dtype)

# a1=np.array([1,2,3])
# a2=np.array([4,5,6])
# print(a1<a2)
# print(a)
# print(a*a)
# print(a-a*2)
# print(a+a*2)
# print(a/1.5)

# arr=np.arange(10)
# print(arr[2:4])
# arr[5:8]=12
# print(arr)

# a=np.array([[1,2,3],[4,5,6],[4,567,854]])
# print(a)
# print(a[1,:2])
# print(a[:2,2])
# a[:2,1:]=0
# print(a[1,:2])
# print(a[:,:2])
# print(a[:,:2])
# print(a[:2,1:])

# a=np.array(["BOb","catt","apple","banana"])
# print(np.random.randn(a))
# data=np.random.rand(7,4)
# print(data)
# data[a!="BOb"]=7
# print(data)

# import numpy as np
# import pandas as pd
# from pandas import Series
# obj=pd.Series([4,7,-5,3])
# print(obj)
# obj2=pd.Series([4,7,-5,-3],index=['a','b','c','d'])
# print(obj2)
# print(obj2.index)
# print(obj2['a'])
# print(obj2["d"])
# print(obj2.dtype)

# print(obj2>0)
# print(obj2["c"]>10)
# print(obj2*2)
# print(np.exp(obj2))
# print(4 in obj2)
# dict={'Ohio':35000,'Texas':71000,'Oregon':16000,'Utah':5000}
# obj3=pd.Series(dict)
# print(obj3)
# states=['Ohio','California','Utah','Oregon','Texas']
# obj4=pd.Series(dict,index=states)
# print(obj4)
# print(pd.isnull(obj4['California']))
# print(pd.notnull(obj4['Utah']))
# print(obj3+obj4)
# obj4.name='population'
# obj4.index.name='state'
# print(obj4)

# obj=pd.Series([1,2,3,5])
# names=["Tharani","Maitraiyee","Jash","HK"]
# obj.index=names
# print(obj)

# data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],'year':[2000,2001,2003,2001,2002],'pop':[1.5,1.7,3.6,2.4,2.9]}
# print(pd.DataFrame(data))
# a=pd.DataFrame(data,columns=['pop','state','debt'])
# print(a)

# sparsematrix=[[0,0,3,0,4],[0,0,5,7,0],[0,0,0,0,0],[0,2,6,0,0]]
# size=0
# for i in range(4):
#     for j in range(5):
#         if(sparsematrix[i][j]!=0):
#             size+=1

# rows,cols=(3,size)
# compactMatrix=[[0 for i in range(cols) for j in range(rows)]]

# k=0 
# for i in range(4):
#     for j in range(5):
#         if(sparsematrix[i][j]!=0):
#             compactMatrix[0][k]=i
#             compactMatrix[1][k]=j
#             compactMatrix[2][k]=sparsematrix[i][j]
#             k+=1

# for i in compactMatrix:
#     print(i)

# import numpy as np
# from scipy.sparse import csr_matrix
# arr=np.array([[[0,0,3,0,4],[0,0,5,7,0],[0,0,0,0,0],[0,2,6,0,0]]])
# print(arr)
# print(csr_matrix(arr).data)

# import numpy as np
# from scipy.integrate import quad
# def f(x):
#     return 2**x+1
# res=quad(f,3,4)
# print(res)

# import numpy as np
# from scipy.integrate import quad
# def f(x):
#     return 2**x+1
# res=quad(f,1,2)
# print(res)


# m1=[[1,2,3],[3,4,5]]
# m2=[[2,3,4,],[5,6,7]]
# m3=[[0,0,0],[0,0,0]]
# for i in range(len(m1)):
#     for j in range(len(m2[0])):
#         m3[i][j]=m1[i][j]+m2[i][j]
# for r in m3:
#     print(r)

# char_to_dots = {
#   'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
#   'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
#   'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
#   'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#   'Y': '-.--', 'Z': '--..', ' ': ',', '0': '-----',
#   '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
#   '6': '-....', '7': '--...', '8': '---..', '9': '----.',
#   '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
#   ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
#   '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
# }
# def encode():
#     n=str(input("Enter what do you want to encode: "))
#     v=""
#     for i in n:
#         if i in char_to_dots.keys():
#             v+=char_to_dots[i]+' '
#         elif i.upper() in char_to_dots.keys():
#             v+=char_to_dots[i.upper()]+' '
#         else:
#             v+=i
#     return v
# def decode():
#     n=str(input('Enter what do you want to decode: '))
#     n=n.split()
#     k=""
#     for i in n:
#         if i in char_to_dots.values():
#             v=list(char_to_dots.values()).index(i)
#         else:
#             print("error")
#             break
#         k+=list(char_to_dots.keys())[v]
#     return k

# print(encode())
# print(decode())


# f=open("cricketers.txt","r+")
# f.writelines("Sachin tendulkar")
# f.writelines("Dhoni","\n")
# f.writelines("Rohit Sharma","\n")
# f.writelines("Ronlado","\n")
# f.writelines("Messi","\n")
# print(f.read())   
# d={"k1":123,'k2':[0,1,2],'k3':{"insideKeys":100}}
# print(d['k2'])
# print(d["k3"])
# print(d["k3"]["insideKeys"])
# n=int(input("enter till how many no"))



# n=int(input("Enter the terms"))
# a=0
# b=1
# if a<=0:
#     print(a)
# else:
#     print(a,b,end="")
# for i in range(2,n+1):
# # while i<=n:
#     c=a+b
#     print(c)
#     a=b
#     b=c

# def fibonacci(n):
#     if n<=1:
#         return n
#     else:
#         return(fibonacci(n-1)+fibonacci(n-2))
# n=int(input("Enter no"))
# for i in range(n):
#     print(fibonacci(i))

# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     return result
# n=int(input("enter"))
# print(factorial(n))

def isPalindrome(n):
    #n=n.lower()
    l=len(n)
    if l<2:
        return True
    elif n[0]==n[l-1]:
        return isPalindrome(n[1:l-1])
    else:
        return False
    
n=input("Enter")
ans=isPalindrome(n)
if ans:
    print("Palindrome")
else:
    print("Not a palindrome")