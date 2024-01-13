# a=[69,88,96,34]
# n=1
# while True:
#     print("The list has following elements")
#     print("1. Append an element")
#     print("2. Inserting an element")
#     print("3. appending a list to given list")
#     print("4. Modify an existing element")
#     print("5. Delete an existing element with a given value")
#     print("6. Sorting the list in ascending")
#     print("7. Sorting the list in descending order")
#     print("8. Displaying the list")
#     n=int(input("Enter your choice"))

#     if n==1:
#         m=int(input("Enter the element to be appended "))
#         a.append(m)
#         print("Element has been appended",a)
#     elif n==2:
#         m=int(input("Enter the element to be inserted "))
#         pos=int(input("Enter the position of the element"))
#         a.insert(pos,m)
#         print("Element has been inserted at the given position",a)
#     elif n==3:
#         m=eval(input("Enter the elements separated by commas "))
#         a.extend(m)
#         print("List has been appended",a)
#     elif n==4:
#         i=int(input("Enter the position of the element to be modified"))
#         if i<len(a):
#             new_element=int(input("Enter the new element "))
#             old_element=a[i]
#             a[i]=new_element
#             print("The element",old_element,"has been modified",a)
#         else:
#             print("Positon of the element is more than length of the list")
#     elif n==5:
#         i=int(input("Enter position of the element to be deleted"))
#         if i<len(a):
#             m=a.pop(i)
#             print("The element",m,"has been deleted")
#         else:
#             print("no the element is not deleted")
#     elif n==6:
#         a.sort()
#         print("The list is sorted in ascending order",a)
#     elif n==7:
#         a.sort(reverse=True)
#         print("The list has been sorted in descending order",a)
#     elif n==8:
#         print("The list is: ", a)
#     elif n==9:
#         break
#     else:
#         print("Try again")