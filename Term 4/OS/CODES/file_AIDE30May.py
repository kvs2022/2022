# f=open('file_AIDE.text','w')
# data=["This is the first line","This is the second line","This is the third line"]
# for line in data:
#     f.write(line +'\n')
#     print(line,"\n")
# f.close()

# #------------------------------------ OR  ----------------------------------------------------

# with open ('file_AIDE30May.text','w') as f:
#     data=["This is the first line", "This is the second line ", "This is the third line"]
#     for a in data:
#         f.write(a+'\n')
#         print(a)


with open("input.text","r")as f:
    count=0
    for i in f:
        for a in i :
            if i[a]==i[a]:
                count+=1
        print(i,count)
        