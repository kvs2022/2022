
                                #Data Cleaning:  #find missing data
# import pandas as pd
# import numpy as np
# string_data=pd.Series(['aardvark','artichoke',np.nan,'avocado'])
# print(string_data)
# print(string_data.isnull())

#replacing the data stored at positon 0 
# string_data[0]=None
# print(string_data)
# print(string_data.isnull())

# filtering missing data
# import pandas as pd
# from numpy import nan as NA
# data=pd.Series([1,NA,3.5,NA,7])
# print(data.dropna())

# from numpy import nan as NA
# import pandas as pd
# data=pd.DataFrame([[1,6.5,3.],[1.,NA,NA],[NA,NA,NA],[NA,6.5,3.]])
# print(data)

# dropna drops row that contains missing value
# cleaned=data.dropna()
# print(cleaned)

#how='all' will only drop rows that are all NA:
# print(data.dropna(how='all'))

# import pandas as pd
# import numpy as np
# df=pd.DataFrame(np.random.randn(7,3))
# print(df)

#slicing
# from numpy import nan as NA
# df.iloc[:4,1]=NA
# df.iloc[:2,2]=NA
# print(df)
# print(df.dropna())
# print(df.dropna(thresh=2))      #0 and 1 row


                                    #FIGURES AND SUBPLOTS
# from matplotlib import Figure as plt
# import numpy as  np
# fig=plt.figure()
# ax2=fig.add_subplot(2,2,2)
# ax2.scatter(np.arange(30),np.arange(30)+3*np.random.randn(30))
# plt.savefig("graph4.png")


