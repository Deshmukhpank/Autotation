import os
import re
import colorama
from colorama import Fore

current_data =0


InputFilename = input("enter the file name\n")
InputsearchString = input("enter the search string in the file \n") 
file = open(InputFilename,"r") 
if file == 0:
    print("The file is empty: " + str(file))
else:
    print("The file reading started:")   
cnt = 1
previous_data = -1
for line in file:     
      if InputsearchString in line: 
        match = re.search(InputsearchString+'([^,]+)', line) 
        current_data = int(match.group(1))    
        if current_data == previous_data + 1:
            pass
        elif current_data == previous_data:
            print("\033[1;32m  repeated packet is  \n",line)
        else:    
            print("\033[2;31m  Missing Packet is   \n",line)
            #print("\033[2;37;40m Missing Packet is \033[0;37;40m \n",line)
        previous_data = current_data
        cnt += 1


   












# &2# 3 1 3 ff 600011 62285326 680 $
# LC2_V60_90322
# LC3_V60_90322
# LC40_V60_90322

  



















































# ADM1 AS-1P-123 1 250 11 2 3 100 10 $v01.00.12 1 com29_lc1_v70_14122 com3_lc_v70_141221
# dir = os.listdir('./')
# for file in dir:
#     if InputFilename == file:
#         print("File Found", file)
#         break