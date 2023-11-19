import sys


class FSA:

    def __init__(self,):
        self.initial_state = '0'
        self.final_states = set()

        self.transitions = dict()
        self.alphabet = set()

    def add_transition(self, state_from, state_to, symbol):

        if state_from in self.transitions.keys():
            if symbol not in self.transitions[state_from].keys():
                self.transitions[state_from][symbol] = {state_to}
            else:
                self.transitions[state_from][symbol] |= {state_to}
        else:
            self.transitions[state_from] = dict()
            self.transitions[state_from][symbol] = {state_to}

    def add_final_state(self, state):
        self.final_states.add(state)


fsa = FSA()

table = open(sys.argv[1])
for line in table:
    line = line.rstrip()

    if len(line.split('\t')) == 3:
        a, b, c = line.split('\t')
        fsa.add_transition(a, b, c)
        fsa.alphabet.add(c)
    else:
        fsa.add_final_state(line)


for line in sys.stdin:
    line = line.rstrip()

    if fsa.accepts(line):
        print('YES')
    else:
        print('NO')
