class DAGNode:
    def __init__(self, op, arg1=None, arg2=None, label=None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.label = label


class DAG:
    def __init__(self):
        self.nodes = []
        self.root = None

    def insert(self, op, arg1=None, arg2=None):
        node = DAGNode(op, arg1, arg2)
        for n in self.nodes:
            if n.op == op and n.arg1 == arg1 and n.arg2 == arg2:
                return n
        self.nodes.append(node)
        return node

    def generate(self, op, arg1=None, arg2=None):
        if op == "lit":
            return self.insert(op, arg1)
        elif op in ["+", "-", "*", "/"]:
            left = arg1 if isinstance(
                arg1, DAGNode) else self.generate("lit", arg1)
            right = arg2 if isinstance(
                arg2, DAGNode) else self.generate("lit", arg2)
            return self.insert(op, left, right)
# Define the DAG class and node class as before


# Get user input for an expression
expression = input("Enter an expression: ")

# Split the expression into operands and operators
operands = []
operators = []
current_operand = ""
for char in expression:
    if char.isdigit():
        current_operand += char
    else:
        operands.append(int(current_operand))
        operators.append(char)
        current_operand = ""
operands.append(int(current_operand))

# Generate the DAG
dag = DAG()
root = None
for i in range(len(operators)):
    op = operators[i]
    arg1 = operands[i] if i == 0 else root
    arg2 = operands[i+1]
    root = dag.generate(op, arg1, arg2)

# Print the DAG
print("DAG nodes:")
for node in dag.nodes:
    print(
        f"Op: {node.op}, Arg1: {node.arg1}, Arg2: {node.arg2}, Label: {node.label}")
print(f"Root: {dag.root}")
