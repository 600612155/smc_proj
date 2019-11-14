import re

label_addr = {}



# with open('test.txt') as f_in:
#     l = list(line for line in (l.strip() for l in f_in) if line)
# print(l[0]) #read file without blank line


            

f2 = open("test.txt", "r")
c = 0
for line in f2:
    test1 = re.split(r"\s+", line,2)
    if test1[0] != '':
        # print(test1[0] +" " + str(c))
        label_addr[test1[0]] = c 
    c+=1
# print(label_addr)       
    # print("line["+str(c)+"]: "+x[0])
    # c+=1





mem = [] # 65536 mem
for i in range(0,10):
    mem.append(0)
reg = [] # 8 reg 0-7
for i in range(0,8):
    reg.append(0)



f3 = open("test.txt", "r")
line1 = f3.readline()
line1 = f3.readline()
# line1 = f3.readline()
# line1 = f3.readline()
# line1 = f3.readline()
# line1 = f3.readline()
# line1 = f3.readline()
# line1 = f3.readline()
PC = 0
print(line1)


line_split = re.split(r"\s+", line1,5)
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



def I_type_GenCode(line_split):
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
        if sym_addr in label_addr:
            bi_offset+=bin(int(str(label_addr[sym_addr])))[2:].zfill(16)
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

with open('test.txt') as f_in:
    l = list(line for line in (l.strip() for l in f_in) if line)



f = open("test.txt", "r")
for line in f:
        test = re.split(r"\s+", line,5)
        print(test)
        if test[1] == 'add' or test[1] == 'nand'  : 
            print(int(R_type_GenCode(test),2))
        elif  test[1] == 'lw' or test[1] == 'sw' or test[1] == 'beq' :
            print(I_type_GenCode(test))
        elif test[1] == 'halt' or test[1] == 'noop' :
            print(int(O_type_GenCode(test),2))
        elif test[1] == 'jalr':
            print(int(J_type_GenCode(test),2))
        elif test[1] == '.fill':
            pass
        else:
            raise ValueError("Invalid instruction")


print(gen_32twoCom(543))