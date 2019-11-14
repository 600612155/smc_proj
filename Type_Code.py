import re



def labelAddr():
    #label 
    label_addr = {}
    f2 = open("test.txt", "r")
    c = 0
    for line in f2:
        test1 = re.split(r"\s+", line,2)
        if test1[0] != '':
            # print(test1[0] +" " + str(c))
            label_addr[test1[0]] = c 
        c+=1
    return label_addr

#GenCode 
#-------------------------------------------------------------------------------------
def gen_16twoCom(intNumber):
    if intNumber < 0:
        if intNumber >= -32768:
            negNum = intNumber*-1
            top = bin(32767)[2:].zfill(15)
            bi = bin(negNum)[2:].zfill(15)
            negate =  int(top,2) - int(bi,2) + int('1',2)
            result = '1'+bin(negate)[2:].zfill(15)
            return result
        else:
            raise ValueError("Overflow Number")
    else:
        result = bin(intNumber)[2:].zfill(16)
        if intNumber < 32768:
            return result
        else:
            raise ValueError("Overflow Number")

def gen_32twoCom(intNumber):
    if intNumber < 0:
        if intNumber >= -2147483648:
            negNum = intNumber*-1
            top = bin(2147483647)[2:].zfill(31)
            bi = bin(negNum)[2:].zfill(31)
            negate =  int(top,2) - int(bi,2) + int('1',2)
            result = '1'+bin(negate)[2:].zfill(31)
            return result
        else:
            raise ValueError("Overflow Number")
    else:
        result = bin(intNumber)[2:].zfill(32)
        if intNumber < 2147483648:
            return result
        else:
            raise ValueError("Overflow Number")
#--------------------------------------------------------------------------------------

#Type_Code 
def R_type_GenCode(line_split):
    inst = line_split[1]
    regA = line_split[2]
    regB = line_split[3]
    regDes = line_split[4]
    opcode = ''
    bi_regA = bin(int(regA))[2:].zfill(3)
    bi_regB = bin(int(regB))[2:].zfill(3)
    bi_regDes = bin(int(regDes))[2:].zfill(3)
    if inst == 'add':
        opcode+='000'
    elif inst == 'nand':
        opcode+='001'
    machineCodeInst = '0000000'+opcode+bi_regA+bi_regB+'0000000000000'+bi_regDes
    return machineCodeInst

def I_type_GenCode(line_split,PC):
    inst = line_split[1]
    regA = line_split[2]
    regB = line_split[3]
    off = line_split[4]
    opcode = ''
    bi_regA = bin(int(regA))[2:].zfill(3)
    bi_regB = bin(int(regB))[2:].zfill(3)
    bi_offset = ''

    if inst == 'lw':
        opcode+='010'
    elif inst == 'sw':
        opcode+='011'
    elif inst == 'beq':
        opcode+='100'
    else:
        raise ValueError("Invalid instruction")
    if off.lstrip('-').isdigit() :
        bi_offset+=gen_16twoCom(int(off))
    else:
        sym_addr = off
        intOffset = labelAddr()[sym_addr] - (PC+1)
        if sym_addr in labelAddr():
            if inst == 'beq':
                bi_offset+=gen_16twoCom(intOffset)
            else:
                bi_offset+=bin(int(labelAddr()[sym_addr]))[2:].zfill(16)
    I_code = '0000000' + opcode + bi_regA + bi_regB + bi_offset
    
    return I_code


def J_type_GenCode(line_split):
    
    regA = line_split[2]
    regB = line_split[3]
    opcode = '101'
    bi_regA = bin(int(regA))[2:].zfill(3)
    bi_regB = bin(int(regB))[2:].zfill(3)
    return '0000000'+opcode+bi_regA+bi_regB+'0000000000000000'

def O_type_GenCode(line_split):
    opcode = ''
    if line_split[1] == 'halt':
        opcode+='110'
    elif line_split[1] == 'noop':
        opcode+='111'
        
    return '0000000'+opcode+'0000000000000000000000'