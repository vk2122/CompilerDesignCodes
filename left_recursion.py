def remove_left_recursion(grammar):
    non_terminals = list(grammar.keys())

    for i in range(len(non_terminals)):
        A = non_terminals[i]
        productions = grammar[A]

        # Divide productions into two lists: left-recursive and non-left-recursive
        left_recursive = []
        non_left_recursive = []
        for production in productions:
            if production[0] == A:
                left_recursive.append(production)
            else:
                non_left_recursive.append(production)

        # If there is left recursion, remove it
        if len(left_recursive) > 0:
            B = A + "'"
            grammar[B] = []
            grammar[A] = []
            for production in non_left_recursive:
                grammar[A].append(production + (B,))
            for production in left_recursive:
                grammar[B].append(production[1:] + (B,))
            grammar[B].append(('EPSILON',))

    return grammar


grammar = {
    'S': [('S', 'a'), ('b',)],
    'A': [('A', 'c', 'd'), ('e',)]
}
no_left_recursion_grammar = remove_left_recursion(grammar)
print(no_left_recursion_grammar)
