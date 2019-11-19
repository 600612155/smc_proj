#----------------------------------------------------------------------------------------------------------------------------------------
import re
from Type_Code import J_type_GenCode,I_type_GenCode,O_type_GenCode,R_type_GenCode,gen_16twoCom,gen_32twoCom,sign_extend32,labelAddr
from assembler import Assembler
from simulator import simulate

fileName = "multiplication.txt"
filetext = open(fileName,"r")



label_addr = labelAddr(fileName) # create labels - address


line_arr = []
for line in filetext :
    line_arr.append(line) #store each line in array

mem = []
for i in range(0,len(line_arr)):
    mem.append(0)
reg = []
for i in range(0,8):
    reg.append(0)

PC=0
while PC < len(line_arr):
    lineSplit = re.split(r"\s+", line_arr[PC],5) 
    Assembler(lineSplit,mem,PC,label_addr) #convert whole inst to machineCode and store memory
    PC += 1


    
startPC = 0
simulate(startPC,reg,mem)





# def combination( n,  r):
#     if r == 0 or n == r:
#         return 1 
#     else:
#         return combination(n-1,r) + combination(n-1, r-1)

# print(combination(7,3))



