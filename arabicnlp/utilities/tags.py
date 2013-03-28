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

def strip_morphotags(s):
    '''Removes any morphological markings from POS string s.'''

    s = s.split(':')[0]
    plus_split = s.split('+')

    for tag in plus_split:
        if tag in ARABIC_POS_TAGS:
            return tag
        under_split = tag.split('_')
        if len(under_split) > 2:
            underscore_tag = '%s_%s' % (under_split[0], under_split[1])
            if underscore_tag in ARABIC_POS_TAGS:
                return underscore_tag
        else:
            for othertag in under_split:
                if othertag in ARABIC_POS_TAGS:
                    return othertag
    return s

def strip_all(s):
    s = strip_dashtags(s)
    s = strip_morphotags(s)
    return s

def collapse_verb_tag(tag):
    '''Collapses all verbs into "VB" tag.'''

    # hack for english compatibility
    if 'VB' in tag:
        return 'VB'

    return 'VB' if tag in ARABIC_VERB_TAGS else tag

if __name__ == '__main__':
    import doctest
    doctest.testmod()
