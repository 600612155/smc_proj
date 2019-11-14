#----------------------------------------------------------------------------------------------------------------------------------------
import re
from Type_Code import J_type_GenCode,I_type_GenCode,O_type_GenCode,R_type_GenCode,labelAddr


# from Type_O import O_type
# from Type_R import R_type

print(labelAddr()['start'])
    

#import code from text file.
filetext = open("test.txt","r")
#check command in code for each line
PC=0
mem = []
for i in range(0,11):
    mem.append(0)

print(mem)

for line in filetext :
        test = re.split(r"\s+", line,5)

        if test[1] == 'add' or test[1] == 'nand'  : 
            print(R_type_GenCode(test))
            print(int(R_type_GenCode(test),2))
            mem[PC] = int(R_type_GenCode(test),2)
        elif  test[1] == 'lw' or test[1] == 'sw' or test[1] == 'beq' :
            print(I_type_GenCode(test,PC))
            print(int(I_type_GenCode(test,PC),2))
            mem[PC] = int(I_type_GenCode(test,PC),2)
        elif test[1] == 'halt' or test[1] == 'noop' :
            print(O_type_GenCode(test))
            print(int(O_type_GenCode(test),2))
            mem[PC] = int(O_type_GenCode(test),2)
        elif test[1] == 'jalr':
            print(J_type_GenCode(test))
            print(int(J_type_GenCode(test),2))
            mem[PC] = int(J_type_GenCode(test),2)
        elif test[1] == '.fill':
            print(".fill")
            if test[2].lstrip('-').isdigit():
                mem[PC] = test[2]
            else:
                mem[PC] = labelAddr()[test[2]]
        else:
            raise ValueError("Invalid instruction")
        PC+=1

print(mem)
