reg_desc = {}
addr_desc = {}


def getreg():
    for r in range(8):
        if not reg_desc.get(r):
            reg_desc[r] = True
            return r
    raise Exception("Out of registers!")


def releasereg(r):
    reg_desc[r] = False


def gen_code(x, y, op, z):
    l = addr_desc.get(y, None)
    if l is None or reg_desc.get(l):
        l = getreg()
        print(f"MOV {y}, R{l}")
        addr_desc[y] = l
    r = addr_desc.get(z, None)
    if r is None or reg_desc.get(r):
        r = getreg()
        print(f"MOV {z}, R{r}")
        addr_desc[z] = r
    print(f"{op} R{l}, R{r}")
    addr_desc[x] = l
    releasereg(r)
    if not is_live(y) and y in addr_desc.values():
        releasereg(addr_desc[y])
        del addr_desc[y]
    if not is_live(z) and z in addr_desc.values():
        releasereg(addr_desc[z])
        del addr_desc[z]


def is_live(x):
    return True


gen_code('a', 'b', 'ADD', 'c')
gen_code('d', 'a', 'SUB', 'b')
gen_code('x', 'y', 'MUL', 'z')