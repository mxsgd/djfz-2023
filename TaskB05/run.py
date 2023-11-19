# B00 (2021)
#
import sys


class FSA:

    def __init__(self):
        self.initial_state = '0'  # zakładamy dla uproszczenia, że initial state = 0
        self.final_states = set()

        self.transitions = dict()
        self.alphabet = set()

    def add_transition(self, state_from, state_to, symbol):

        if state_from in self.transitions.keys():
            self.transitions[state_from][symbol] = state_to
        else:
            self.transitions[state_from] = dict()
            self.transitions[state_from][symbol] = state_to

    def add_final_state(self, state):
        self.final_states.add(state)

    def get_final_state(self, string):

        current_state = self.initial_state
        for symbol in string:
            current_state = self.transitions[current_state][symbol]
        return current_state

    def accepts(self, string):

        if self.get_final_state(string) in self.final_states:
            return True
        else:
            return False


fsa = FSA()

# def build_fsa(self): #, dfa_desciption
table = open(sys.argv[1])  #  dfa_desciption
for line in table:
    line = line.rstrip('\n')
    if len(line.split('\t')) == 3:
        a, b, c = line.split('\t')
        fsa.add_transition(a, b, c)  #self
        fsa.alphabet.add(c)  #self
    elif len(line.split('\t')) == 1:
        fsa.add_final_state(line)  #self
    else:
        assert False


# def run_dfa(self):  # , input
for line in sys.stdin:  # open(input)
    line = line.rstrip()

    line_n = list(line)

    for i in range(len(line_n)):
        if line_n[i] not in fsa.alphabet:  #self
            line_n[i] = 'x'

    if fsa.accepts(line_n):  #self
        print('YES')
    else:
        print('NO')

    # def run_dfa_and_compare(self, input, expected):
    #
    #     accepts = []
    #
    #     for line in open(input):  # sys.stdin
    #         line = line.rstrip()
    #
    #         line_n = list(line)
    #
    #         for i in range(len(line_n)):
    #             if line_n[i] not in self.alphabet:
    #                 line_n[i] = 'x'
    #
    #         if self.accepts(line_n):
    #             accepts.append('YES')
    #         else:
    #             accepts.append('NO')
    #
    #     i = 0
    #     for line in open(expected):
    #         if line.rstrip() != accepts[i]:
    #             print('Incorrect in line ' + str(i))
    #             return
    #         i = i + 1
    #     print('Correct')
