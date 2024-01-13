# a=[31,34,56,7,8,9]
# n=0
# print("The operations performed here are")
# print("1. Appending the element")
# print("2. Inserting an element")
# n=int(input("Enter your choice between 1 or 2 "))
# if n==1:
#      elements=int(input("Enter the elements you want to append "))
#      a.append(elements)
#      print("The appended list is:",a)
#  elif n==2:
#      elements=int(input("Elements to be inserted "))
#      pos=int(input("Enter the position "))
#      a.insert(elements,pos)
#      print("The new list ",a)
#  else:
#      print("Try again ")


# create an empty dictionary

# #tharani, #juug22btech56651, #aide
#code has error
dict={}
no=0
a=input("Enter Yes to continue otheriwse enter no: ")
while a=="yes":
    print("The dictionary is",dict)
    print("1. Adding an phone number")
    print("2. Printing a phone number")
    print("3.Deleting a phone number")
    print("4. Search a phone number")
    no=int(input("Enter your choice "))

    if no==1:
        a=input("Enter the name of the person ")
        b=int(input("Enter a phone number "))
        dict[a]=b
        print(a)
    elif no==2:
        print(dict)
    elif no==3:
        a=input("Enter a name")
        del dict[a]
    elif no==4:
        x=int(input("Enter the no of the person "))
        if x in dict.values:
            print("The name of the person is",dict.value(x))
        else:
            print("nope enter proper details")
    else:
        print("You are not authorised")
  


"""
#tharani, #juug22btech56651, #aide
a=[69,88,96,34]
n=1
while True:
    print("The list has following elements")
    print("1. Append an element")
    print("2. Inserting an element")
    print("3. appending a list to given list")
    print("4. Modify an existing element")
    print("5. Delete an existing element with a given value")
    print("6. Sorting the list in ascending")
    print("7. Sorting the list in descending order")
    print("8. Displaying the list")
    n=int(input("Enter your choice"))

    if n==1:
        m=int(input("Enter the element to be appended "))
        a.append(m)
        print("Element has been appended",a)
    elif n==2:
        m=int(input("Enter the element to be inserted "))
        pos=int(input("Enter the position of the element"))
        a.insert(pos,m)
        print("Element has been inserted at the given position",a)
    elif n==3:
        m=eval(input("Enter the elements separated by commas "))
        a.extend(m)
        print("List has been appended",a)
    elif n==4:
        i=int(input("Enter the position of the element to be modified"))
        if i<len(a):
            new_element=int(input("Enter the new element "))
            old_element=a[i]
            a[i]=new_element
            print("The element",old_element,"has been modified",a)
        else:
            print("Positon of the element is more than length of the list")
    elif n==5:
        i=int(input("Enter position of the element to be deleted"))
        if i<len(a):
            m=a.pop(i)
            print("The element",m,"has been deleted")
        else:
            print("no the element is not deleted")
    elif n==6:
        a.sort()
        print("The list is sorted in ascending order",a)
    elif n==7:
        a.sort(reverse=True)
        print("The list has been sorted in descending order",a)
    elif n==8:
        print("The list is: ", a)
    elif n==9:
        break
    else:
        print("Try again")
"""