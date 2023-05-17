def compute_lr0_items(grammar):
    # Augment the grammar with a new start symbol S' -> S
    start = list(grammar.keys())[0]
    grammar['S\''] = [(start,)]

    # Compute the LR(0) items for each augmented production rule
    items = {}
    for A in grammar.keys():
        items[A] = []
        for production in grammar[A]:
            for i in range(len(production) + 1):
                item = (A, tuple(production[:i]), tuple(production[i:]))
                items[A].append(item)

    return items


def compute_lr0_states(grammar):
    # Compute the LR(0) items and the initial state
    items = compute_lr0_items(grammar)
    start = ('S\'',), 0
    state = closure(start, items)

    # Initialize the list of LR(0) states with the initial state
    states = [state]

    # Compute the LR(0) states iteratively until no new states are added
    changed = True
    while changed:
        changed = False
        for state in states:
            for symbol in get_symbols(grammar, state):
                goto_state = goto(state, symbol, items)
                if goto_state and goto_state not in states:
                    states.append(goto_state)
                    changed = True

    return states


def closure(items, all_items):
    # Compute the closure of a set of LR(0) items
    closure = set(items)
    added = True
    while added:
        added = False
        for item in closure.copy():
            A, alpha, beta = item
            if beta and beta[0] in all_items.keys():
                for item in all_items[beta[0]]:
                    new_item = (item[0], (), item[1])
                    if new_item not in closure:
                        closure.add(new_item)
                        added = True

    return closure


def goto(items, symbol, all_items):
    # Compute the goto set of a set of LR(0) items and a symbol
    goto = set()
    for item in items:
        A, alpha, beta = item
        if beta and beta[0] == symbol:
            goto.add((A, alpha + (symbol,), beta[1:]))
    if goto:
        return closure(goto, all_items)
    else:
        return None


def get_symbols(grammar, items):
    # Get the symbols that appear after the dot in the given set of LR(0) items
    symbols = set()
    for item in items:
        A, alpha, beta = item
        if beta:
            symbols.add(beta[0])
    return symbols


grammar = {
    'S': ['E'],
    'E': ['E+T', 'T'],
    'T': ['T*F', 'F'],
    'F': ['(E)', 'id']
}
states = compute_lr0_states(grammar)

# Print the LR(0) states
for i, state in enumerate(states):
    print(f"I{i}:")
    for item in state:
        print(f"\t{item[0]} -> {' '.join(item[1])} . {' '.join(item[2])}")

# Print the transitions between LR(0) states
for i, state in enumerate(states):
    for symbol in get_symbols(grammar, state):
        goto_state = goto(state, symbol, compute_lr0_items(grammar))
        if goto_state:
            j = states.index(goto_state)
            print(f"I{i} --{symbol}--> I{j}")