# print("hi")
# a=input("enter your name").strip().title()
# print("Hello",a,sep=",",end='\n')
# print("hello, 'friend'")
# first,last=a.split(",")
# print(f"hey, {a}")
# print(f"hello, {last}")
# print(a.capitalize())
# print(a.uppercase())

# UDEMY
# def function(name):
#     print ("How are u ?",name)
# function("Harry")
#return keyword allows us to assign the output of the function
#a new variable

# def say_helo(name="hey"):
#     print(f"Hello {name}")
# say_helo("Jerry")

# def even_checklist(no_list):
#     even_numbers=[]
#     for num in no_list:
#         if num % 2 == 0:
#             even_numbers.append(num)
            
#         else:
#             pass
#     return even_numbers
# a=even_checklist([1,2,3,4,5,6])
# print(a)

# def prime_check(no_list):
#     prime_numbers=[]
#     for i in no_list:
#         if i % 1==0 and i % i==0:
#             prime_numbers.append(i)
#         else:
#             pass
#     return prime_numbers
# b=prime_check([6])
# print(b)

# stock_prices=[("Appl",200),("MSFT",400),("Dell",100)]
# for i,j in stock_prices:
#     print(j+0.5*j)


#find the employee of the month 
# work_hours=[('Abby',100),('Billy',900),('Cassie',800)]
# def employee_check(work_hours):
#     current_max=0
#     employee_of_mth=''
#     for employee,hours in work_hours:
#         if hours>current_max:
#             current_max=hours
#             employee_of_mth=employee
#         else:
#             pass
#     return (employee_of_mth,current_max)
# a,b=employee_check(work_hours)
# print(a,"#",b)
# a=employee_check(work_hours)
# print(a)

from random import shuffle
example=[1,23,46,2,5,63]
# a=shuffle(example)
# print(a)

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list 
result = shuffle_list(example)
print(result)

