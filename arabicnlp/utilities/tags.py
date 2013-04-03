'''
@author David Lundgren <david.m.lundgren@gmail.com>
'''
import constants
import re

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

def mood(tag):
    pass

def number(tag):
    '''
    Returns number of a tag if it has, otherwise None.
    >>> 'IV3MS+IV+IVSUFF_MOOD:I'
    'S'

    >>> ''
    'D'

    >>> ''
    'P'

    >>> 'DET+NOUN+CASE_DEF_ACC'
    None
    '''
    for subtag in tag.split('+'):
        if subtag


    ['CVSUFF_SUBJ:2FS',
    'CVSUFF_SUBJ:2MP',
    'CVSUFF_SUBJ:2MS',
    'IV1P',
    'IV1S',
    'IV2D',
    'IV2FP',
    'IV2FS',
    'IV2MP',
    'IV2MS',
    'IV3FD',
    'IV3FP',
    'IV3FS',
    'IV3MD',
    'IV3MP',
    'IV3MS',
    'IVSUFF_MOOD:I',
    'IVSUFF_MOOD:J',
    'IVSUFF_MOOD:S',
    'IVSUFF_SUBJ:2FS_MOOD:I',
    'IVSUFF_SUBJ:2FS_MOOD:SJ',
    'IVSUFF_SUBJ:D_MOOD:I',
    'IVSUFF_SUBJ:D_MOOD:SJ',
    'IVSUFF_SUBJ:FP',
    'IVSUFF_SUBJ:MP_MOOD:I',
    'IVSUFF_SUBJ:MP_MOOD:SJ',
    'PVSUFF_3MS',
    'PVSUFF_SUBJ:1P',
    'PVSUFF_SUBJ:1S',
    'PVSUFF_SUBJ:2FS',
    'PVSUFF_SUBJ:2MP',
    'PVSUFF_SUBJ:2MS',
    'PVSUFF_SUBJ:3FD',
    'PVSUFF_SUBJ:3FP',
    'PVSUFF_SUBJ:3FS',
    'PVSUFF_SUBJ:3MD',
    'PVSUFF_SUBJ:3MP',
    'PVSUFF_SUBJ:3MS',]


    # case 1: Verb w/ number
    # case 2: Noun w/ number
    # case 3: Adj  w/ number
    
    return None

def is_passive(tag):
    '''
    Returns true if the given tag is a passive verb. Otherwise, false.
    >>> is_passive('PV_PASS+PVSUFF_SUBJ:3MS')
    True

    >>> is_passive('IV3MS+IV+IVSUFF_MOOD:I')
    False
    '''
    return 'PASS' in tag

if __name__ == '__main__':
    import doctest
    doctest.testmod()
