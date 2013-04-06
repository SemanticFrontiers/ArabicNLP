#coding: utf-8

'''
@author David Lundgren <david.m.lundgren@gmail.com>

A whole bunch of utilities for working with trees. I assume
nltk.tree.Tree representations.
'''

import constants

not_trace = lambda tree: tree.height() == 2 and tree.node != '-NONE-'
has_lemma = lambda tree: tree.lemma
is_clause_node = lambda tree: any([tree.node.startswith(s) for s in ['S', 'SBAR', 'SQ', 'SBARQ', 'FRAG', 'TOP']])
is_simple = lambda tree: 'SPLIT' not in tree.node and 'CHAIN' not in tree.node

def is_sister_or_ancestor(treepos, sis_treepos): 
    if len(sis_treepos) < len(treepos):
        return True
    
    if len(sis_treepos) == len(treepos) and \
            sis_treepos[:-1] == treepos[:-1]:
                return True
    return False

def get_leaves(tree, ignore_traces=True):
    '''
    Returns all leaves of a tree. Default behavior ignores traces. Otherwise
    same as nltk.tree.Tree.leaves().
    '''
    if ignore_traces:
        return [word for word, pos in tree.pos() if pos != '-NONE-']
    return tree.leaves()

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
    [((1, 1, 1, 1, 0, 0), 'UP'), ((1, 1, 1, 1, 0), 'UP'), ((1, 1, 1, 1), 'UP'), ((1, 1, 1), 'UP'), ((1, 1), 'DOWN'), ((1, 1, 0), 'DOWN'), ((1, 1, 0, 0), 'DOWN'), ((1, 1, 0, 0, 0), 'DOWN')]
    '''

    up   = u'\u2191'
    down = u'\u2193'

    up   = 'UP'
    down = 'DOWN'

    a = len(lowest_common_ancestor(tree, pred_treepos, constituent_treepos))
    pred_treepos_path = [(pred_treepos[:x], up) for x in xrange(len(pred_treepos), a, -1)]
    constituent_treepos_path = [(constituent_treepos[:x], down) for x in xrange(a, len(constituent_treepos) + 1)]
    path = pred_treepos_path + constituent_treepos_path

    return path

def get_clause_node(tree, node_treepos):
    '''
    Returns the lowest S, SBAR, etc... node that the given node is a child of.
    '''
    cur_pos = node_treepos
    while not is_clause_node(tree[cur_pos]):
        cur_pos = cur_pos[:-1]
    return tree[cur_pos]

def get_verb_node(tree):
    '''
    Wrapper to handle complex *SPLIT* and *CHAIN* trees. 
    Returns tree with the final verb of one of these splits.
    All splits look something like

    (*SPLIT*
        (PRT (NEG_PART -لا))
        (IV3MS+IV+IVSUFF_MOOD:I يَزالُ))
    '''
    return tree if is_simple(tree) else tree[-1]

if __name__ == '__main__':
    import doctest
    doctest.testmod()
