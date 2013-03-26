'''
@author David Lundgren <david.m.lundgren@gmail.com>
'''
import constants

def atb_tag_to_penn(tag):
    '''Arabic POS tag to English POS tag.

    Converts a Penn Arabic TreeBank part-of-speech tag into the corresponding
    Penn English TreeBank part-of-speech tag.

    >>> atb_tag_to_penn('NOUN') 
    'NN'

    >>> atb_tag_to_penn('PVSUFF_DO:3MS') 
    'PRP'
    '''

    return constants.ATB_TO_PENN.get(tag, None)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
