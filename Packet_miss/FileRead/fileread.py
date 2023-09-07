import os
import re
import colorama
from colorama import Fore

current_data =0
# gwdaemon.log.0 
InputsearchString ="[2023-01-10T19:00:14.000Z]"
InputEndsearchString ="[2023-01-10T20:00:14.000Z]"
LC = "&1#2 6 1"

# InputFilename = input("enter the file name\n")
# InputsearchString = input("enter the search string in the file \n") 
# file = open(InputFilename,"r") 
# if file == 0:
#     print("The file is empty: " + str(file))
# else:
#     print("The file reading started:")
# for line in file:     
#     if InputsearchString in line:
#         print("debug line no is  ",InputsearchString)
#     else:
#         print("no debug is printed")  

InputFilename = input("enter the file name:-")
# InputsearchString = input("enter the start time that we have to read:-") 
# InputEndsearchString = input("enter the end time that we have to read:-") 
# file = open(InputFilename,"r") 

# with open(InputFilename, 'r') as fp:
#     # read line number 3 to 5
#     # index starts from 0
#     x = fp.readlines()[InputsearchString:InputEndsearchString]
#     print(x)


# if file == 0:
#     print("The file is empty: " + str(file))
# else:
#     print("The file reading started:")
#     for line in file:     
#         if InputsearchString in line:
#             print("debug line no is  ",InputsearchString)
#         else:
#             print("no debug is printed")
result = []
repeatdata =[]
i = 0
flagg = False
with open(InputFilename, "r") as fp:
    # access each line
    for line in fp:
        # check line number
        if InputsearchString in line:
            flagg = True
        if flagg :
            if LC in line :
                # print("LC data is:",LC)
                result.append(line + "\n")
            if  InputEndsearchString in line:
                flagg  = False
                break
for i in result:     
    # split_LCData = i.split(" ")
    # print("split_LCData is:",split_LCData)
    # if split_LCData[8] in result:
    #     print("!!!!!!!!!!!!!!!!!!!!!!!!!!")
    #     repeatdata.append(line) 
    #     print("repeat is:",repeatdata)   
    # else:        
        
    #     pass
     print("Append data is:",i)