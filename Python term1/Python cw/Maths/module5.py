# from sympy import Symbol,Function,Derivative,Eq,dsolve
# x=Symbol('x')
# y=Function('y')(x)
# deq=Eq(Derivative(y,x,x)+Derivative(y,x)-2*y,0)
# solution=dsolve(deq)
# print(solution)

# from sympy import Symbol,Function,Derivative,Eq,dsolve,solve
# from sympy.plotting import plot
# x=Symbol('x')
# y=Function('y')(x)
# deq=Eq(Derivative(y,x,x)-2*Derivative(y,x)+6*y,0)
# s=solve(deq)
# eqn1=s.rhs.subs(x,0)-1
# eqn2=s.rhs.diff(x).subs(x,0)+1
# constants=solve([eqn1,eqn2])
# solution=s.subs(constants)
# plot(solution.rhs)


# from sympy import Symbol,Function,Derivative,Eq,dsolve,solve
# from sympy.plotting import plot
# x=Symbol('x')
# y=Function('y')(x)
# deq=Eq(Derivative(y,x,x,x)-3*Derivative(y,x,x)+3*Derivative(y,x)-y,0)
# s=dsolve(deq)
# print(s)

# from sympy import Symbol,Function,Dermivative,Eq,dsolve,solve
# from sympy.plotting import plot
# x=Symbol('x')
# y=Function('y')(x)
# deq=Eq(Derivative(y,x,x,x,x)-2*Derivative(y,x,x,x)+2*Derivative(y,x,x)-2*Derivative(y,x)+y,0)
# s=dsolve(deq)
# print(s)

