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
tempoutlist=[]
with open("C:\\Users\\sxc210186\\Documents\\GitHub\\CSAW\\SAT_solver\\netlist.txt", 'r') as f:
    lines = f.readlines()
    for line in lines:
        part = line.split('=')
        
        if "INPUT" in part[0]:
            if("k" in part[0]):
                key.append(part[0].split("(")[1].split(")")[0])
                print(part[0].split("(")[1].split(")")[0],"&")
            else:
                inp.append(part[0].split("(")[1].split(")")[0])
                print(part[0].split("(")[1].split(")")[0],"&")
        elif "OUTPUT" in part[0]:
            outp.append(part[0].split("(")[1].split(")")[0])
            print(part[0].split("(")[1].split(")")[0],"&")
        else:
            gates = part[1].split("(")
            a=part[1].split("(")[1].split(",")[0]
            b=part[1].split("(")[1].split(",")[1].split(")")[0]
            tempout = part[0].split()[0]
            tempoutlist.append(tempout)

        
            def miter_firsthalf():
            # half miter circuit
                if " nand" == gates[0]:
                    print("("+"~("+a+"&"+b+") <=> "+tempout+") &")
                elif " and" == gates[0]:
                    print("("+ "("+a+"&"+b+") <=> "+tempout+") &")
                elif " xnor" == gates[0]:
                    print("("+ "~("+a+"+"+b+") <=> "+tempout+") &")
                elif " xor" == gates[0]:
                    print("("+ "("+a+"+"+b+") <=> "+tempout+") &")
                elif " nor" == gates[0]:
                    print("("+ "~("+a+"|"+b+") <=> "+tempout+") &")
                elif " or" == gates[0]:
                    print("("+ "("+a+"|"+b+") <=> "+tempout+") &")
                elif " not" == gates[0]:
                    print("("+"~("+a.partition(")")[0]+") <=> "+tempout+") &")

            def miter_secondhalf():
                if "INPUT" in part[0]:
                    if("k" in part[0].split("(")[1].split(")")[0]):
                        part[0]=part[0]+"x"
                        key.append(part[0].split("(")[1].split(")")[0])
                        print(part[0].split("(")[1].split(")")[0],"&")
            #other Half miter circuit
                tempoutx = tempout+"x"
                if " nand" == gates[0]:
                    print("("+"~("+a+"&"+b+") <=> "+tempoutx+") &")
                elif " and" == gates[0]:
                    print("("+ "("+a+"&"+b+") <=> "+tempoutx+") &")
                elif " xnor" == gates[0]:
                    print("("+ "~("+a+"+"+b+") <=> "+tempoutx+") &")
                elif " xor" == gates[0]:
                    print("("+ "("+a+"+"+b+") <=> "+tempoutx+") &")
                elif " nor" == gates[0]:
                    print("("+ "~("+a+"|"+b+") <=> "+tempoutx+") &")
                elif " or" == gates[0]:
                    print("("+ "("+a+"|"+b+") <=> "+tempoutx+") &")
                elif " not" == gates[0]:
                    print("("+"~("+a.partition(")")[0]+") <=> "+tempoutx+") &")
            
            #iokeys()
            #miter_firsthalf()
            miter_secondhalf()

        
