import re
from Type_Code import J_type_GenCode, I_type_GenCode, O_type_GenCode, R_type_GenCode, labelAddr, gen_16twoCom, gen_32twoCom, sign_extend32,twoCom_ToInt
from assembler import Assembler
from printState import printState


def simulate(PC, reg, mem):
    count = 1
    
    for i in range(0, 8):
        reg[i] = 0
    startBit = 31
    endBit = 32
    while PC < len(mem):
        
        printState(PC,reg,mem)
        machineCode = gen_32twoCom(int(mem[PC]))
        opcode = gen_32twoCom(int(mem[PC]))[startBit-24:endBit-22]


        A = int(machineCode[startBit-21:endBit-19], 2)
        B = int(machineCode[startBit-18:endBit-16], 2)
        Des = int(machineCode[startBit-2:endBit-0], 2)
        offset = int(twoCom_ToInt(sign_extend32( machineCode[startBit-15:endBit-0])))
        count+=1
        if opcode == '110':
            PC = PC + 1
            count-=1
            break
        elif opcode == '000': #add
            reg[Des] = int(reg[A]) + int(reg[B])
        elif opcode == '001': #nand
            AandB = int(gen_32twoCom(int(reg[A])), 2) & int(gen_32twoCom(int(reg[B])), 2)
            AnandB = int('11111111111111111111111111111111', 2) - AandB
            reg[Des] = AnandB
        elif opcode == "010": #lw
            reg[B] = mem[int(reg[A])+offset]
        elif opcode == '011': #sw
            mem[reg[A]+offset] = int(reg[B])
        elif opcode == '100': #beq
            if reg[A] == reg[B]:
                PC = PC + 1 + offset
                continue
        elif opcode == '101': #jalr
            if A == B:
                reg[B] = PC + 1
                PC = PC + 1
                continue
            else:
                reg[B] = PC + 1
                PC = reg[A]
                continue 
        elif opcode == '111': #noop
            pass
                  


        PC += 1
        

    print("machine halted ")
    print("total of "+str(count)+ " instructions executed")
    print()
    print("final state of machine:")
    print()
    printState(PC,reg,mem)  
    




