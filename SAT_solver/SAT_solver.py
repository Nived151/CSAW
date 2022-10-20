'''convert .bench to .txt file
in txt file ignore inputs and outputs
convert the gates to oracle
add oracle variables to change it into miter circuit
put the miter circuit to logictools , find an api or something to integrate the logic tools
depending on the outputs of logic tools, change the variables in miter circuit
iterate the code unitl no dip
insert the variables when the dip is false to get keys'''


with open("C:\\Users\\sxc210186\\Documents\\GitHub\\CSAW\\SAT_solver\\netlist.txt", 'r') as f:
    lines = f.readlines()
    f='='
    result=[]
    i=0
    t='nand'
    l=len(t)+1
    for line in lines:
        string1=line

        
        part = string1.partition('=')
        result.append(part)
    print(result)
    '''for i in range(0,len(part)):
         if(t in part[i][0:l]):
                   print(line)'''
       



            






