'''
@author David Lundgren <david.m.lundgren@gmail.com>
'''

import constants

not_trace = lambda t: t.height() == 2 and t.node != '-NONE-'

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

if __name__ == '__main__':
    import doctest
    doctest.testmod()
