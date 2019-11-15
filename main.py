#----------------------------------------------------------------------------------------------------------------------------------------
import re
from Type_Code import J_type_GenCode,I_type_GenCode,O_type_GenCode,R_type_GenCode,labelAddr,gen_16twoCom,gen_32twoCom,sign_extend32
from assembler import Assembler
from simulator import simulate


filetext = open("test.txt","r")

line_arr = []
for line in filetext :
    line_arr.append(line) #store each line in array

mem = []
for i in range(0,len(line_arr)):
    mem.append(0)
reg = []
for i in range(0,8):
    reg.append(0)


# print(sign_extend32(gen_16twoCom(7)))

        






PC=0
while PC < len(line_arr):
    lineSplit = re.split(r"\s+", line_arr[PC],5) 
    Assembler(lineSplit,mem,PC) #convert whole inst to machineCode and store memory
    PC += 1


    
PC = 0
simulate(PC,reg,mem)




