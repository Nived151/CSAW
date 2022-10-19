'''convert .bench to .txt file
in txt file ignore inputs and outputs
convert the gates to oracle
add oracle variables to change it into miter circuit
put the miter circuit to logictools , find an api or something to integrate the logic tools
depending on the outputs of logic tools, change the variables in miter circuit
iterate the code unitl no dip
insert the variables when the dip is false to get keys'''

key=[]
inp=[]
outp=[]
with open("C:\\Users\\sxc210186\\Documents\\GitHub\\CSAW\\SAT_solver\\netlist.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        part = line.partition('=')
        io=part[0].partition("(")
        gates = part[2].partition("(")
        inp1 = gates[2].partition(",")
        inp2 = inp1[2].partition(")")
        
        def iokeys():
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
        
        def miter_firsthalf():
        # half miter circuit
            if " nand" == gates[0]:
                print("("+part[0]+ "<=> ~("+inp1[0]+" & "+inp2[0]+"))&")
            elif " and" == gates[0]:
                print("("+part[0]+ "<=> ~("+inp1[0]+" & "+inp2[0]+"))&")
            elif " xnor" == gates[0]:
                print("("+part[0]+ "<=> ~("+inp1[0]+" + "+inp2[0]+"))&")
            elif " xor" == gates[0]:
                print("("+part[0]+ "<=> ("+inp1[0]+" + "+inp2[0]+"))&")
            elif " nor" == gates[0]:
                print("("+part[0]+ "<=> ~("+inp1[0]+" | "+inp2[0]+"))&")
            elif " or" == gates[0]:
                print("("+part[0]+ "<=> ("+inp1[0]," | "+inp2[0]+"))&")
            elif " not" == gates[0]:
                print("("+part[0]+"<=> ~("+inp1[0].partition(")")[0]+"))&")

        def miter_secondhalf():
        #other Half miter circuit
            if " nand" == gates[0]:
                print("("+part[0].split()[0]+"'"+ "<=> ~("+inp1[0]+" & "+inp2[0]+"))&")
            elif " and" == gates[0]:
                print("("+part[0].split()[0]+"'"+ "<=> ~("+inp1[0]+" & "+inp2[0]+"))&")
            elif " xnor" == gates[0]:
                print("("+part[0].split()[0]+"'"+ "<=> ~("+inp1[0]+" + "+inp2[0]+"))&")
            elif " xor" == gates[0]:
                print("("+part[0].split()[0]+"'"+ "<=> ("+inp1[0]+" + "+inp2[0]+"))&")
            elif " nor" == gates[0]:
                print("("+part[0].split()[0]+"'"+ "<=> ~("+inp1[0]+" | "+inp2[0]+"))&")
            elif " or" == gates[0]:
                print("("+part[0].split()[0]+"'"+ "<=> ("+inp1[0]," | "+inp2[0]+"))&")
            elif " not" == gates[0]:
                print("("+part[0].split()[0]+"'"+"<=> ~("+inp1[0].partition(")")[0]+"))&")
            
            if "INPUT" in part[0]:
                if("k" in part[0].split("(")[1].split(")")[0]):
                    key.append(part[0].split("(")[1].split(")")[0])
                    print(part[0].split("(")[1].split(")")[0]+"'","&")

        iokeys()
        miter_firsthalf()
        miter_secondhalf()

        
