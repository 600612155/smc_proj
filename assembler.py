

from Type_Code import J_type_GenCode,I_type_GenCode,O_type_GenCode,R_type_GenCode,labelAddr



def Assembler(lineSplit,mem,PC):
        if lineSplit[1] == 'add' or lineSplit[1] == 'nand'  : 
            mem[PC] = int(R_type_GenCode(lineSplit),2)
        elif  lineSplit[1] == 'lw' or lineSplit[1] == 'sw' or lineSplit[1] == 'beq' :
            mem[PC] = int(I_type_GenCode(lineSplit,PC),2)
        elif lineSplit[1] == 'halt' or lineSplit[1] == 'noop' :
            mem[PC] = int(O_type_GenCode(lineSplit),2)
        elif lineSplit[1] == 'jalr':
            mem[PC] = int(J_type_GenCode(lineSplit),2)
        elif lineSplit[1] == '.fill':
            if lineSplit[2].lstrip('-').isdigit():
                mem[PC] = lineSplit[2]
            else:
                mem[PC] = labelAddr()[lineSplit[2]]
        else:
            raise ValueError("Invalid instruction")
