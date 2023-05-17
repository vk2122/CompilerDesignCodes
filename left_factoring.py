def left_factor(grammar):
    non_terminals = list(grammar.keys())

    for A in non_terminals:
        productions = grammar[A]
        common_prefixes = []

        for production in productions:
            # Find the longest common prefix among the productions
            prefix = production[0]
            for i in range(1, len(production)):
                if production[i] != prefix[i-1]:
                    prefix = prefix[:i-1]
                    break
            common_prefixes.append((prefix, production))

        # Find the longest common prefix among the common prefixes
        max_length = 0
        max_prefix = ''
        for prefix, _ in common_prefixes:
            if len(prefix) > max_length:
                max_length = len(prefix)
                max_prefix = prefix

        # If there is a common prefix, left factor the productions
        if max_length > 0:
            B = A + "'"
            grammar[B] = []
            grammar[A] = []
            for prefix, production in common_prefixes:
                if prefix == max_prefix:
                    grammar[A].append((prefix, B))
                else:
                    grammar[B].append(production[len(prefix):])
            grammar[B].append(('EPSILON',))

    return grammar


grammar = {
    'S': [('a', 'S', 'b', 'c'), ('a', 'S', 'b', 'd'), ('e', 'f')],
    'A': [('a', 'A', 'b'), ('a', 'A', 'c'), ('d',)]
}
left_factored_grammar = left_factor(grammar)
print(left_factored_grammar)
