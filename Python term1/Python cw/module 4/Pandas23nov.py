                              
                               #SERIES pandas data structue


# import pandas as pd
# obj=pd.Series([4,7,-5,3])
# print(obj)      #Will print index position also


#create a series with an index identifying each data point with a label
# import pandas as pd
# obj2=pd.Series([4,7,-5,3],index=['d','b','a','c'])
# print(obj2)

#only info about index
# print(obj2.index)

# print(obj2['a'])

# obj2['d']=6
# print(obj2)     #or 
# print(obj2[['c','a','d']]) #will print only c,a,d if u write obj2 then it will print whole obj2 list
# print(obj2[['a','b','c','d']])  

#using numpy functions
# print(obj2[obj2>0])
# print(obj2*2)

#pandas don't have exponential function that's why we are using numpy
#pandas can do both numeric and non-numeric data types
#numpy can only work with numeric data types
# import numpy as np
# print(np.exp(obj2))
#exponential funtion is e^x where e is a mathematical constant called Euler's number,appx 2.718282


# import pandas as pd
# import numpy as np
# obj3=pd.Series([1,1,2,3])
# print(np.exp(obj3))
#will take only index values
#print(1 in obj3)   #O/P True
#print(5 in obj3)   #O/P False

#if u hve a data stored in a Python dict,u can create series from it by passing the dict
# import pandas as pd
# sdata={"Ohio":35000,'Texas':71000,'Oregon':16000,'Utah':5000}
# obj4=pd.Series(sdata)
# print(obj4)
# states=['California','Ohio','Oregon','Texas']
# obj4_1=pd.Series(sdata,index=states)
# print(obj4_1)       

#check for null values
#print(pd.isnull(obj4_1))

#Feature of Series is that it automatically aligns by indexlabel
# obj4_1.name='population'
# obj4_1.index.name='state'
# print(obj4_1)


#A Series's index can be altered in-place by assignment
# import pandas as pd
# obj=pd.Series([4,7,-5,3])
# print(obj)
# obj.index=['Bob','Steve','Jeff','Ryan']
# print(obj)

#as tuple
# import pandas as pd
# obj5=pd.Series((1,1,2,3))
# print(obj5)

#like with a numpy array,data can be accessed by the associated index via the familiar Python square-bracket notation
# print(obj[1])
# print(obj[1:3])



                            #DATA FRAMES   pandas data structure


# import pandas as pd
# # data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada','Nevada'],'year':[2000,2001,2002,2001,2002,2003],'pop':[1.5,1.7,3.6,2.4,2.9,3.2]}
# frame=pd.DataFrame(data)
# print(frame)

# # Specify a sequence of columns,the DataFrames's columns will be arranged in that order
# frame=pd.DataFrame(datcolumns=['pop','year','state'])
# print(frame)

# a column that is not in the dict will give missing values(NaN)
# frame2=pd.DataFrame(data,columns=['pop','year','state','debt'])
# print(frame2)

# # modify index
# frame2=pd.DataFrame(data,columns=['pop','year','state'],index=['one','two','three','four','five','six'])
# print(frame2)

# # display column names
# print(frame2.columns)

# #a column in a  Dataframe can be retrieved as a Series
# print(frame2['state'])
#         #or
# print(frame2.year)

# #to find row
# print(frame2.loc['three'])
# # print(frame2.loc[3])        #error as index value is modified to three

# frame2['debt']=16.5
# print(frame2)
# import numpy as np
# frame2['debt']=np.arange(6.)
# print(frame2)

# #inserting missing values in any location
# val=pd.Series([-1.2,-1.5,-1.7],index=['two','four','five'])
# frame2['debt']=val
# print(frame2)

# #add a new column of boolean values where the state column equals 'Ohio'
# #assigning a column that doesn't exist will create a new column
# frame2['eastern']=frame2.state=='Ohio'
# print(frame2)

# #del method can then be used to remove a column
# del frame2['eastern']
# print(frame2)

#transpose (swaping the rows and columns)
# frame2['pop']=frame2.transpose['year']
# print(frame2)
#transpose is not there

# GRAPH
#matplotlib library is used in python to plot graphs
# import matplotlib.pyplot as plt
# x=[2,6,10,19]
# y=[3,6,12,17]

# dotted line with black diamonds
# x2=[7,8,9,12,16]
# y2=[7,8,13,16,7]
# plt.plot(x,y,'b--',label='One',linewidth=2)         #b is for color and -- is for type of the line
# plt.plot(x2,y2,'kd',label='Two')            #k is for black and d is for diamond
# plt.title('Chart')
# plt.ylabel('Y axis')
# plt.xlabel('x axis')
# plt.legend()            #using legend to display labels i.e what type of line and what type of shapes
# plt.show()              #used for showing the graph



#line graph
# plt.plot(x,y,'black',linewidth=2)       #plot(x,y) line plot(x,y,color cyan,linewidth)
# plt.show()


#bar graph
# plt.bar(x,y,align='center',label='Sample1',color='green')
# plt.xlabel("X axis")
# plt.ylabel("Y axis")
# plt.title("Bar Graph")

#simple plot
# import matplotlib.pyplot as plt
# import numpy as np
# data=np.arange(10)
# print(data)
# plt.plot(data)



#figures and subplots
#create a new fig with plt.figure
# import matplotlib.pyplot as plt
# fig=plt.figure()
#this means that the figure should be 2 x 2(so up to four plots in total), and we're selecting the first of four subplots(numbered from 1)
# ax1=fig.add_subplot(2,2,1)  #size is 2 x 2 and 1 is saying that it's the first block
# ax2=fig.add_subplot(2,2,2)  #size is 2 x 2 and 2 is saying that it's the second block
# ax3=fig.add_subplot(2,2,3)  #size is 2 x 2 and 3 is saying that it's the third block
# ax4=fig.add_subplot(2,2,4)  #size is 2 x 2 and 4 is saying that it's the fourth block