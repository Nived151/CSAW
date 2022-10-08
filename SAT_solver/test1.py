key=[]
inp=[]
outp=[]
with open("C:\\Users\\sxc210186\\Documents\\GitHub\\CSAW\\SAT_solver\\netlist1.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        part = line.partition('=')
        io=part[0].partition("(")
        gates = part[2].partition("(")
        inp1 = gates[2].partition(",")
        inp2 = inp1[2].partition(")")
        
        # inp, keys, out as list
        if "INPUT" in part[0]:
            if("k" in part[0].split("(")[1].split(")")[0]):
                key.append(part[0].split("(")[1].split(")")[0])
                print(part[0].split("(")[1].split(")")[0],"&")
            else:
                inp.append(part[0].split("(")[1].split(")")[0])
                print(part[0].split("(")[1].split(")")[0],"&")
        if "OUTPUT" in part[0]:
            outp.append(part[0].split("(")[1].split(")")[0])
            print(part[0].split("(")[1].split(")")[0],"&")
        
        #miter circuit
        if " nand" == gates[0]:
            print(part[0], "<=> ~(",inp1[0],"&",inp2[0],")&")
        elif " and" == gates[0]:
            print(part[0], "<=> ~(",inp1[0],"&",inp2[0],")&")
        elif " xnor" == gates[0]:
            print(part[0], "<=> ~(",inp1[0],"+",inp2[0],")&")
        elif " xor" == gates[0]:
            print(part[0], "<=> (",inp1[0],"+",inp2[0],")&")
        elif " nor" == gates[0]:
            print(part[0], "<=> ~(",inp1[0],"|",inp2[0],")&")
        elif " or" == gates[0]:
            print(part[0], "<=> (",inp1[0],"|",inp2[0],")&")
        elif " not" == gates[0]:
            print(part[0], "<=> ~(",inp1[0].partition(")")[0],")&")

        
