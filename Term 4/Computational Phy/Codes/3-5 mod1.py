#1

# W=-600
# x=-0.01
# k=W/x
# print("The force constant of the spring is",k,"N/m")

# def forceconstant(W,x):
#     return W/x
# W=-600
# x=-0.01
# print("The force constant of the spring is",forceconstant(W,x),"N/m")

# def forceconstant(W,x):
#     return W/x
# W=float(input("Enter the force applied or restoring force"))
# x=float(input("Enter the compression made by the spring"))
# print("The force constant of the spring is",forceconstant(W,x),"N/m")


#2

# from math import pi
# def force(m,t):
#     return (4*(pi**2)*m)/(t**2)
# m=float(input("Enter the mass"))
# t=float(input("Enter the time taken to complete one oscillation"))
# print("Force constant of the spring is ",force(m,t),"N/m")
                                #or
# print("Force constant of the spring is ",round((force(m,t)),2),"N/m")


# from math import pi
# def force(m,k):
#     return 2*pi*math.sqrt(m/k)
# m=float(input("Enter the mass in kg"))
# k=float(input("Enter the value of force constant in N/m"))
# print("time taken to complete one oscillation is ",round((force(m,k)),2),"sec")


#3

# from math import pi
# def force(m,k):
#     return (1/(2*pi))*math.sqrt(k/m)
# m=float(input("Enter the mass in kg"))
# k=float(input("Enter the value of force constant in N/m"))
# print("frequency per second ",round((force(m,k)),2),"Hz")
# a=round((force(m,k)),2)
# print("frequecy per minute",round((a*60),1))


