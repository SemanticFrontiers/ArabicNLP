#coding: utf-8

import os

# TODO: make this general
DICT_FILE = '/Users/David/data/ontonotes/raw/dictStems'

def dictStems():
    with open(DICT_FILE) as fin:
        for line in fin:
            yield line.strip()

def parse_line(SAMA_ROOT_TO_LEMMAS, line, state):

    # root case
    if line.startswith(';--- '):
        root = line.split()[1]
        SAMA_ROOT_TO_LEMMAS[root] = []
        state['root'] = root

    # lemma case
    elif line.startswith(';; '):
        lemma = line.split()[1]
        state['lemma'] = lemma
        SAMA_ROOT_TO_LEMMAS[state['root']].append(lemma)

    # catchall
    elif line.startswith(';'):
        # should take care of ; ========= Alif ...
        # should take care of ;
        pass

    # stems case
    else:
        pass

def initialize_indices():
    '''
    initiliazes all indices given the dictStems file
    '''

    # regular index
    SAMA_ROOT_TO_LEMMAS = {}
    state = {}
    for line in dictStems():
        parse_line(SAMA_ROOT_TO_LEMMAS, line, state)

    # inverted index
    SAMA_LEMMA_TO_ROOT  = {} 
    for root, lemmas in SAMA_ROOT_TO_LEMMAS.iteritems():
        for lemma in lemmas:
            if lemma in SAMA_LEMMA_TO_ROOT:
                raise ValueError('lemma-to-MANY-roots (%s --> %s, %s)' % (lemma, SAMA_LEMMA_TO_ROOT[lemma], root))
            SAMA_LEMMA_TO_ROOT[lemma] = root

    return SAMA_ROOT_TO_LEMMAS, SAMA_LEMMA_TO_ROOT

SAMA_ROOT_TO_LEMMAS, SAMA_LEMMA_TO_ROOT = initialize_indices()
