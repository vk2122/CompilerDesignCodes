gram = {
	"E":["E*E","E+E","i"]
}
starting_terminal = "E"

inp = input("Enter the string \n")
inp=inp+"$"

stack = "$"
print(f'{"Stack": <15}'+"|"+f'{"Input Buffer": <15}'+"|"+f'Parsing Action')
print(f'{"-":-<50}')

while True:
	action = True
	i = 0
	while i<len(gram[starting_terminal]):
		if gram[starting_terminal][i] in stack:
			stack = stack.replace(gram[starting_terminal][i],starting_terminal)
			print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Reduce S->{gram[starting_terminal][i]}')
			i=-1
			action = False
		i+=1
	if len(inp)>1:
		stack+=inp[0]
		inp=inp[1:]
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Shift')
		action = False

	if inp == "$" and stack == ("$"+starting_terminal):
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Accepted')
		break

	if action:
		print(f'{stack: <15}'+"|"+f'{inp: <15}'+"|"+f'Rejected')
		break

# Sample input / Output:

# Enter the string 
# i+i*i
# Stack          |Input Buffer   |Parsing Action
# --------------------------------------------------
# $i             |+i*i$          |Shift
# $E             |+i*i$          |Reduce S->i
# $E+            |i*i$           |Shift
# $E+i           |*i$            |Shift
# $E+E           |*i$            |Reduce S->i
# $E             |*i$            |Reduce S->E+E
# $E*            |i$             |Shift
# $E*i           |$              |Shift
# $E*E           |$              |Reduce S->i
# $E             |$              |Reduce S->E*E
# $E             |$              |Accepted