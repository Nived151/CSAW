'''convert .bench to .txt file
in txt file ignore inputs and outputs
convert the gates to oracle
add oracle variables to change it into miter circuit
put the miter circuit to logictools , find an api or something to integrate the logic tools
depending on the outputs of logic tools, change the variables in miter circuit
iterate the code unitl no dip
insert the variables when the dip is false to get keys'''

with open('netlist.txt', 'w') as f:
    f.write('readme')