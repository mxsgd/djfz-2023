#!/usr/bin/python
#-*- coding: utf-8 -*-
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

table = open(sys.argv[1])
for line in table:
    line = line.rstrip('\n')
    if len(line.split('\t')) == 3:
        a, b, c = line.split('\t')
        fsa.add_transition(a, b, c)
        fsa.alphabet.add(c)
    elif len(line.split('\t')) == 1:
        fsa.add_final_state(line)
    else:
        assert False

for line in sys.stdin:

    line = line.rstrip()
    for symbol in line:
        if symbol not in fsa.alphabet:
            assert False

    if fsa.accepts(line):
        print('YES')
    else:
        print('NO')
