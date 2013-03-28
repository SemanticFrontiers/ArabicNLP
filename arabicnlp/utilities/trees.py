'''
@author David Lundgren <david.m.lundgren@gmail.com>
'''

import constants

not_trace = lambda tree: tree.height() == 2 and tree.node != '-NONE-'
has_lemma = lambda tree: tree.lemma

def head_leaf(tree):
    '''
    Returns the first (non-empty) leaf in a tree. Can be punctuation.
    Returns None if there is no head leaf.
    '''
    leaves = list(tree.subtrees(not_trace))
    return leaves[0] if leaves else None

def tail_leaf(tree):
    '''
    Returns the last (non-empty) leaf in a tree. Can be punctuation.
    Returns None if there is no tail leaf.
    '''
    leaves = list(tree.subtrees(not_trace))
    return leaves[-1] if leaves else None

def get_lemmas(tree):
    '''
    Returns all lemmas for a tree.
    '''
    return [st.lemma for st in tree.subtrees(has_lemma)]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
