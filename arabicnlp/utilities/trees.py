'''
@author David Lundgren <david.m.lundgren@gmail.com>

A whole bunch of utilities for working with trees. I assume
nltk.tree.Tree representations.
'''

import constants

not_trace = lambda tree: tree.height() == 2 and tree.node != '-NONE-'
has_lemma = lambda tree: tree.lemma

def num_leaves(tree, ignore_traces=True):
    '''
    Returns the # of leaves of a tree (default ignores traces).
    '''
    return len(list(tree.subtrees(not_trace))) if ignore_traces else len(tree.leaves())

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

def lowest_common_ancestor(tree, node1_treepos, node2_treepos):
    ''' Lowest common ancestor between two nodes in a tree.

    >>> import nltk
    >>> s = '(S (NP (PRP They))(VP (VBP expect)(S (NP (PRP him))(VP (TO to)(VP (VB cut)(NP (NNS costs))(PP throughout the organization))))))'
    >>> tree = nltk.tree.Tree(s)
    >>> node1_treepos = (1, 1, 1, 1, 0, 0)
    >>> node2_treepos = (1, 1, 0, 0, 0)
    >>> lowest_common_ancestor(tree, node1_treepos, node2_treepos)
    (1, 1)

    If the tree's root is the lowest common ancestor, return ()
    >>> node1_treepos = ()
    >>> node2_treepos = ()
    >>> lowest_common_ancestor(tree, node1_treepos, node2_treepos)
    ()
    '''

    i = 0
    min_length = min(len(node1_treepos), len(node2_treepos))
    while i < min_length and node1_treepos[i] == node2_treepos[i]:
        i += 1
    return node1_treepos[:i]

def get_path(tree, pred_treepos, constituent_treepos):
    '''Finds a path from pred_treepos treeposition to constituent_treepos treeposition.

    Returns a list of (treeposition, arrow) pairs. The arrow signifies
    the direction of movement in the tree.

    >>> import nltk
    >>> s = '(S (NP (PRP They))(VP (VBP expect)(S (NP (PRP him))(VP (TO to)(VP (VB cut)(NP (NNS costs))(PP throughout the organization))))))'
    >>> tree = nltk.tree.Tree(s)
    >>> pred_treepos = (1, 1, 1, 1, 0, 0)
    >>> constituent_treepos = (1, 1, 0, 0, 0)
    >>> get_path(tree, pred_treepos, constituent_treepos)
    [((1, 1, 1, 1, 0, 0), u'\u2191'), ((1, 1, 1, 1, 0), u'\u2191'), ((1, 1, 1, 1), u'\u2191'), ((1, 1, 1), u'\u2191'), ((1, 1), u'\u2193'), ((1, 1, 0), u'\u2193'), ((1, 1, 0, 0), u'\u2193'), ((1, 1, 0, 0, 0), u'\u2193')]
    '''

    up   = u'\u2191'
    down = u'\u2193'

    a = len(lowest_common_ancestor(tree, pred_treepos, constituent_treepos))
    pred_treepos_path = [(pred_treepos[:x], up) for x in xrange(len(pred_treepos), a, -1)]
    constituent_treepos_path = [(constituent_treepos[:x], down) for x in xrange(a, len(constituent_treepos) + 1)]
    path = pred_treepos_path + constituent_treepos_path

    return path

if __name__ == '__main__':
    import doctest
    doctest.testmod()
