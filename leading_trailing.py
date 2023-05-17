def compute_leading_sets(grammar):
    # Initialize leading sets to empty sets
    leading = {A: set() for A in grammar.keys()}

    # Compute leading sets iteratively until they stop changing
    changed = True
    while changed:
        changed = False
        for A in grammar.keys():
            for production in grammar[A]:
                # If the production is of the form A -> B1 B2 ... Bk,
                # add the first(B1) ... first(Bi) to leading(A)
                for i in range(len(production)):
                    B = production[i]
                    if B in grammar.keys():
                        old_size = len(leading[A])
                        leading[A].update(leading[B])
                        leading[A].discard('EPSILON')
                        if 'EPSILON' not in leading[B] or i == len(production)-1:
                            break
                        if len(leading[A]) > old_size:
                            changed = True

    return leading


def compute_trailing_sets(grammar):
    # Initialize trailing sets to empty sets
    trailing = {A: set() for A in grammar.keys()}

    # Compute trailing sets iteratively until they stop changing
    changed = True
    while changed:
        changed = False
        for A in grammar.keys():
            for production in grammar[A]:
                # If the production is of the form A -> B1 B2 ... Bk,
                # add the follow(A) to trailing(Bk)
                for i in range(len(production)-1, -1, -1):
                    B = production[i]
                    if B in grammar.keys():
                        old_size = len(trailing[B])
                        trailing[B].update(trailing[A])
                        trailing[B].discard('EPSILON')
                        if 'EPSILON' not in trailing[A] or i == 0:
                            break
                        if len(trailing[B]) > old_size:
                            changed = True

    return trailing


grammar = {
    'S': [('A', 'b'), ('c',)],
    'A': [('a', 'A'), ('d',)]
}
leading_sets = compute_leading_sets(grammar)
trailing_sets = compute_trailing_sets(grammar)
print(leading_sets)
print(trailing_sets)