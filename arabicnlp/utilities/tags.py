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

##############################################################
## Code to reduce POS tags and tree labels to simpler forms ##
##############################################################

def strip_dashtags(s):
    '''Removes dashtags from a string s.'''
    return s if s == '-NONE-' else s.split('-')[0].split('=')[0]

def strip_morphotags(tag):
    '''Removes any morphological markings from POS string s.'''

    tag = tag.split(':')[0]
    plus_split = tag.split('+')

    for sub_tag in plus_split:
        if sub_tag in constants.ARABIC_POS_TAGS:
            return sub_tag
        under_split = sub_tag.split('_')
        if len(under_split) > 2:
            underscore_tag = '%s_%s' % (under_split[0], under_split[1])
            if underscore_tag in constants.ARABIC_POS_TAGS:
                return underscore_tag
        else:
            for othertag in under_split:
                if othertag in constants.ARABIC_POS_TAGS:
                    return othertag
    return tag

def strip_all(tag):
    tag = strip_dashtags(tag)
    tag = strip_morphotags(tag)
    return tag

def simplify_verb_tag(tag):
    '''Collapses all verbs into "VB" tag.'''

    # hack for english compatibility
    if 'VB' in tag:
        return 'VB'

    return 'VB' if strip_all(tag) in constants.ARABIC_VERB_TAGS else tag

def gender(tag):
    '''
    Returns gender of a tag if it has, otherwise None.
    >>> 'IV3MS+IV+IVSUFF_MOOD:I'
    'M'

    >>> ''
    'F'

    >>> 'DET+NOUN+CASE_DEF_ACC'
    None
    '''

    # case 1: Verb w/ gender
    # case 2: Noun w/ gender
    # case 3: Adj  w/ gender
    
    return None
if __name__ == '__main__':
    import doctest
    doctest.testmod()
