import re

def labelAddr():
    label_addr = {}
    f2 = open("combination.txt", "r")
    c = 0
    for line in f2:
        test1 = re.split(r"\s+", line,2)
        if test1[0] != '' :
            if test1[0] not in label_addr:
                label_addr[test1[0]] = c 
            else:
                raise ValueError('Duplicate label >> ' + test1[0] )
        c+=1
    return label_addr

label_addr = labelAddr() # create labels - address
print(label_addr)

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
            raise ValueError("Overflow Number OffsetField")
    else:
        result = bin(intNumber)[2:].zfill(16)
        if intNumber < 32768:
            return result
        else:
            raise ValueError("Overflow Number OffsetField")

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
            raise ValueError("Overflow Number OffsetField")
    else:
        result = bin(intNumber)[2:].zfill(32)
        if intNumber < 2147483648 :
            return result
        else:
            raise ValueError("Overflow Number OffsetField")
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
        if intOffset < -32768 or intOffset > 32767:
            print('overflow reference address')
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



def sign_extend32(offset16):
    if int(offset16,2) & (1<<15):
        for n in range(0,16) :
            offset16 = "1" + offset16
    else:
        for n in range(0,16) :
            offset16 = "0" + offset16
    
    offset32 = offset16
    return offset32

def sign_extend(value, bits):
    if len(value) <= bits :
        x = list(value)
        if x[0] == "0":
            for n in range(bits - len(value)) :
                value = "0" + value 
        else:
            for n in range(bits - len(value)) :
                value = "1" + value 
    return value




def twoCom_ToInt(biNumber32):
    if biNumber32[0] == '0':
        return int(biNumber32,2)
    else:
        return int('-'+str(int(bin(4294967296-int(biNumber32,2))[2:].zfill(32),2)))


        

