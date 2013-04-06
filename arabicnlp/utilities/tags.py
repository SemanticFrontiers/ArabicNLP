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
    'MASC'

    >>> ''
    'FEM'

    >>> 'DET+NOUN+CASE_DEF_ACC'
    None
    '''

    masc = 'MASC'
    fem  = 'FEM'
    # TODO: default case MASC
    # TODO: PRON, REL_PRON, DEM_PRON, POSS_PRON_2MP

    # case 1: Verb w/ gender
    if tag.startswith('IV') and len(tag) >= 3:
        if tag[3] == 'M':
            return masc
        elif tag[3] == 'F':
            return fem
        else:
            return None

    if tag.startswith('CV'):
        if tag[-2] == 'F':
            return fem
        elif tag[-2] == 'M':
            return masc
        else:
            return None

    if tag.startswith('PV'):
        if tag == 'PV+PVSUFF_3MS':
            return masc
        elif ':' in tag and 'M' in tag.split(':')[1]:
            return masc
        elif ':' in tag and 'F' in tag.split(':')[1]:
            return fem
        else:
            return None

    # case 2: Noun, adjective w/ gender
    if 'ADJ' in tag or 'NOUN' in tag:
        if 'FEM' in tag:
            return fem
        else:
            return masc

    # case 3: pronouns 
    if 'PRON' in tag:
        if 'FEM' in tag:
            return fem
        if 'PRON_' in tag:
            if 'F' in tag.split('_')[-1]: # last bit has gender info
                return fem
            else:
                return masc

        return masc

    # catchall
    return None

def mood(tag):
    '''
    Applicable for verbs, this function will return the mood
    of a given verb. 

    Values include:
        'Indicative'
        'Subjunctive'
        'Jussive'
        'Subj/Jussive' (perhaps these are annotation errors?)
        None (if inapplicable)

    >>> mood('IV1P+IV+IVSUFF_MOOD:I')
    'Indicative'
    >>> mood('IV1P+IV+IVSUFF_MOOD:J')
    'Jussive'
    >>> mood('IV1P+IV+IVSUFF_MOOD:S')
    'Subjunctive'
    >>> mood()
    None
    '''

    if 'MOOD' not in tag:
        return None

    # Tags look like this:
    #   IV2D+IV+IVSUFF_SUBJ:D_MOOD:SJ
    # so we split on MOOD and then grab after the colon (:)
    _mood = tag.split('MOOD')[-1][1:]

    return {'I': 'Indicative',
            'J': 'Jussive',
            'S': 'Subjunctive',
            'SJ': 'Subj/Jussive'}.get(_mood, None)

def definiteness(tag):
    '''
    Returns the definiteness status of a nominal.

    Values:
        'Definite'
        'Indefinite'
        None (if non-applicable)

    >>> definiteness('NOUN_PROP+CASE_INDEF_NOM')
    'Indefinite'

    >>> definiteness('DET+NOUN')
    'Definite'

    >>> definiteness('VERB')
    None
    '''
    
    DEF = 'Definite'
    IND = 'Indefinite'
    if 'NOUN' not in tag:
        return None
    elif 'INDEF' in tag:
        return IND
    elif 'NOUN_PROP' in tag:
        return DEF
    elif 'DEF' in tag:
        return DEF
    elif tag.startswith('DET'):
        return DEF
    elif 'POSS' in tag:
        return DEF
    else:
        return IND

def person(tag):
    '''
    Applicable to verbs and pronouns, this will return 1, 2, or 3 depending on
    if the inflected verb is in the 1st person, 2nd, etc.

    Returns `None` if person is not specified.

    >>> person('IV3MD+IV+IVSUFF_SUBJ')
    3

    >>> person('IV')
    None
    '''
    for _person in [1, 2, 3]:
        if str(_person) in tag:
            return _person
    return None

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
        if 'MOOD' in subtag:
            break
    


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

def aspect(tag):
    '''
    Returns the aspect of a verb (past, present, future...) or None.
    >>> aspect('PV+PVSUFF_SUBJ')
    'PV'

    >>> aspect('IV')
    'IV'

    >>> aspect('NOUN_NUM+NSUFF_MASC_PL_GEN')
    None
    '''

    if 'CV' in tag:
        return 'CV'
    elif 'PV' in tag:
        return 'PV'
    elif 'IV' in tag:
        return 'IV'
    else:
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
