# Quadruple data structure
class Quadruple:
    def __init__(self, op, arg1, arg2, result):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

# Triple data structure


class Triple:
    def __init__(self, op, arg1, arg2):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

# Indirect triple data structure


class IndirectTriple:
    def __init__(self, op, arg1, arg2):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2

# Triple indirect data structure


class TripleIndirect:
    def __init__(self, op, arg1, arg2):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2


# Example usage
q = Quadruple("+", "1", "2", "t1")
t = Triple("*", "t1", "3")
it = IndirectTriple("=", "t1", "x")
tit = TripleIndirect("=", "x", "y")
