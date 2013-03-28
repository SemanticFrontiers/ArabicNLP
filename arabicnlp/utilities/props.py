'''
Utilities for processing propositions (for e.g., Semantic Role Labeling).

As far as I know, there is only one semantic role resource in Arabic, Arabic
PropBank (the latest release is under OntoNotes4. The interface for this
resource is also available in this distribution. All arguments and predicates
are specified by PropBankTreePointers (inherited from nltk).

These are utilities to process such TreePointers and PropBankInstances.
'''

def simplify_pointer(pointer, init_or_final='initial'):
    '''Finds head constitutent for a split, chain, etc. tree pointer

    This is a heuristic for handling split arguments and chain arguments.

    Parameters:

        init_or_final -- specifies whether to search for 
            * initial -- head-initial (right-branching) 
            * final   -- head-final (left-branching)
            * ancestor -- lowest-common dominating ancestor 

    '''
    is_simple = lambda pointer: 'pieces' not in dir(pointer)

    if not is_simple(pointer):
        if init_or_final == 'initial':
            return simplify_pointer(pointer.pieces[0])
        elif init_or_final == 'final':
            return simplify_pointer(pointer.pieces[-1])
        raise ValueError('got to end without finding pointer')

    return pointer
