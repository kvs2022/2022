# import numpy as np
# from scipy.sparse import csr_matrix
# ar=np.array([[0,0,3,0,4],[0,0,5,7,0],[0,0,0,0,0],[0,2,6,0,0]])
# print(csr_matrix(ar).data)




#single integration
# from scipy.integrate import quad
# #function we want to integrate
# def f(x):
#     # print(x)
#     return 2**x+1
# res=quad(f,-1,1) #here 0 is the lower limit and 1 is upper limit
# print(res)
# #Res gives res and err as output

# import numpy as np
# import scipy.optimize as opt
# f=lambda x:x**2 + 1 #a x to the power T x + 0*x+1
# x=np.linspace(-2,2)
# print(x,f(x))
# sol=opt.minimize_scalar(f)