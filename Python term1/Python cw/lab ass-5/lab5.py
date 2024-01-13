# f=open("nfl1978-2013.csv","r")
# a=input("Enter full name")
# b=input("Enter full name")
# c=a in f.read() and b in f.read()
# if c==True:
#     print(f.read())

# f = open("nfl1978-2013.csv","r")
# u1=input("Enter team 1 (Full name is required): ")
# u2=input("Enter team 2 (Full name is required): ")

# z = u1 in f.read() and u2 in f.read()
# if z == True:
#     print(f.read())


#tharani, #juug22btech56651, #aide
# lines = [line.strip() for line in open('nfl1978-2013.csv')]
# t1 = input('Enter team 1 (full name required): ')
# t2 = input('Enter team 2 (full name required): ')
# for line in lines[1:]:
#     date, team1, score1, team2, score2 = line.split(',')
    
#     if ((team1 == t1 and team2 == t2) or (team2 == t1 and team1 == t2)) and (int(score1) == 0 or int(score2)) == 0:
#         print(line)    



# from random import shuffle

# f = open("multiple_choice.txt","r")
# f1 = open("new.txt","w")
# l1 = list()
# for line in f:
#     l1.append(line)
# L2=shuffle(l1)
# for i in L2:                                                                            
#     f1.write(i)
# f1=open("new.txt","r")
# print(f1.read())


# from random import shuffle

# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# output_file = open('new_multiple_choice.txt', 'w')
# lines = [line.strip() for line in open('multiple_choice.txt')]
# for line in lines:
#     if len(line) > 0 and line[0].isdigit():
#         print(line, file=output_file)
#         choices = []
#     elif len(line) > 0 and line[0] == '(':
#         choices.append(line[4:]) # only include answer, not letter
#     else: # blank line signals question is done
#         shuffle(choices)
#         for i in range(len(choices)):
#             print('(' + alphabet[i] + ')', choices[i], file=output_file)
#         print(file=output_file) # blank line
# # These three lines are for the last question, since there won't be a blank line at the end of the file to signal that a question is done.
# shuffle(choices)
# for i in range(len(choices)):
#     print('(' + alphabet[i] + ')', choices[i], file=output_file)
# output_file.close()

#tharani, #juug22btech56651, #aide
# lines = [line.strip() for line in open("high_temperatures.txt")]
# largest = 0
# values = []
# for i in range(len(lines)):
#     date,temp = lines[i].split(' ')
#     date30,temp30 = lines[(i-30)%365].split(' ')
#     print(lines)
#     diff = int(temp) - int(temp30)
#     if  diff > largest:
#         largest = diff
#         values = [date30 + ' to ' + date + '   ' + temp30 + '-' + temp]
#     elif diff == largest:
#         values.append(date30 + ' to ' + date + '   ' + temp30 + '-' + temp)
# for x in values:
#     print(x)


# #tharani, #juug22btech56651, #aide
# f=open("a.txt","r")
# f1=open("b.txt","w")
# for line in f:
#     f1.write(line)
# f1=open("b.txt","r")
# print(f1.read())