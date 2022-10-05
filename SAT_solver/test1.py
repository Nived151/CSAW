import re
with open("C:\\Users\\sxc210186\\Documents\\GitHub\\CSAW\\SAT_solver\\netlist.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        part = line.partition('=')
        io=part[0].partition("(")
        gates = part[2].partition("(")
        inp1 = gates[2].partition(",")
        inp2 = inp1[2].partition(")")
        #inpa = inp1[0]
        #inpb = inp2[0]
        

        if "nand" in gates[0]:
            print(part[0], "<=> ~(",inp1[0],"&",inp2[0],")&")
        elif "xnor" in gates[0]:
            print(part[0], "<=> ~(",inp1[0],"+",inp2[0],")&")
        elif "xor" in gates[0]:
            print(part[0], "<=> (",inp1[0],"+",inp2[0],")&")
        elif "nor" in gates[0]:
            print(part[0], "<=> ~(",inp1[0],"|",inp2[0],")&")
        elif "or" in gates[0]:
            print(part[0], "<=> (",inp1[0],"|",inp2[0],")&")
        #not
        #and


