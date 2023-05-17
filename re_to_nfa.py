EPSILON = ''

class State:
    def __init__(self, label):
        self.label = label
        self.transitions = {}
        self.epsilon_transitions = set()
        self.accepting = False

class NFA:
    def __init__(self, start_state, accept_states):
        self.start_state = start_state
        self.accept_states = accept_states

def re_to_nfa(re_string):
    stack = []
    count = 0
    for c in re_string:
        if c == '|':
            # Union
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            new_start_state = State(count)
            new_accept_state = State(count + 1)
            new_start_state.epsilon_transitions.add(nfa1.start_state)
            new_start_state.epsilon_transitions.add(nfa2.start_state)
            nfa1.accept_states[0].epsilon_transitions.add(new_accept_state)
            nfa2.accept_states[0].epsilon_transitions.add(new_accept_state)
            stack.append(NFA(new_start_state, [new_accept_state]))
            count += 2
        elif c == '.':
            # Concatenation
            nfa2 = stack.pop()
            nfa1 = stack.pop()
            for accept_state in nfa1.accept_states:
                accept_state.epsilon_transitions.add(nfa2.start_state)
            stack.append(NFA(nfa1.start_state, nfa2.accept_states))
        elif c == '*':
            # Kleene star
            nfa = stack.pop()
            new_start_state = State(count)
            new_accept_state = State(count + 1)
            new_start_state.epsilon_transitions.add(nfa.start_state)
            nfa.accept_states[0].epsilon_transitions.add(nfa.start_state)
            nfa.accept_states[0].epsilon_transitions.add(new_accept_state)
            new_start_state.epsilon_transitions.add(new_accept_state)
            stack.append(NFA(new_start_state, [new_accept_state]))
            count += 2
        else:
            # Character
            new_start_state = State(count)
            new_accept_state = State(count + 1)
            new_start_state.transitions[c] = [new_accept_state]
            stack.append(NFA(new_start_state, [new_accept_state]))
            count += 2

    nfa = stack.pop()
    nfa.accept_states[0].accepting = True
    return nfa

re_string = input()
nfa = re_to_nfa(re_string)