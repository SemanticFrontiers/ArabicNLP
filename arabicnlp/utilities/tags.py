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

def get_case_from_atb_tag(tag):
    '''
    Returns the case of an Arabic TreeBank (v3.0) tag if present, otherwise None.
    >>> get_case_from_atb_tag('NOUN+CASE_DEF_GEN')
    CASE_DEF_GEN

    >>> get_case_from_atb_tag('PREP')
    CASE_DEF_GEN
    '''
    has_case = lambda t: 'CASE' in t
    for t in tag.split('+'):
        if has_case(t):
            return t
    return None

if __name__ == '__main__':
    import doctest
    doctest.testmod()
