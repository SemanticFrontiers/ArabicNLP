'''

Collapse of Arabic POS tags as they occur with the parsed Arabic Treebank
tokens (taglist.selected) into old Penn English Treebank POS tags.

ALL CAPS is Arabic tag, followed by --> PENNTAG and/or comment (a list of
Arabic tags may be followed by one Penn tag, meaning that the whole list
can go to that one tag).  This list is done alphabetically by the Arabic
POS tags from taglist.selected.

    ARABIC+TAG

        --> its corresponding Penn English Treebank POS tag
            (possible comment)

            1-28-03, Ann Bies bies@ldc.upenn.edu


'''

#==========================================================================
ATB_TO_PENN = {}
ATB_TO_PENN['ABBREV'] = 'NN'
#(Not sure what to say about ABBREV -- most likely NN.  Penn English POS
#had abbreviations tagged as their full word function, but I expect most
#abbreviations in this Arabic corpus to be nouns.)

ATB_TO_PENN['ADJ'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_FEM_DU_ACCGEN'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_FEM_DU_ACCGEN_POSS'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_FEM_DU_NOM'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_FEM_PL'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_FEM_SG'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_MASC_DU_ACCGEN'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_MASC_DU_ACCGEN_POSS'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_MASC_DU_NOM'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_MASC_DU_NOM_POSS'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_MASC_PL_ACCGEN'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_MASC_PL_ACCGEN_POSS'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_MASC_PL_NOM'] = 'JJ'
ATB_TO_PENN['ADJ+NSUFF_MASC_SG_ACC_INDEF'] = 'JJ'
ATB_TO_PENN['ADJ_PROP'] = 'JJ'
ATB_TO_PENN['ADJ_PROP+NSUFF_FEM_SG'] = 'JJ'
ATB_TO_PENN['ADJ_PROP+NSUFF_MASC_PL_NOM'] = 'JJ'
ATB_TO_PENN['ADJ_PROP+NSUFF_MASC_SG_ACC_INDEF'] = 'JJ'

ATB_TO_PENN['ADV'] = 'RB'
ATB_TO_PENN['ADV+NSUFF_FEM_SG'] = 'RB'
ATB_TO_PENN['ADV+NSUFF_MASC_SG_ACC_INDEF'] = 'RB'

ATB_TO_PENN['CONJ'] = 'CC'

ATB_TO_PENN['CONJ+NEG_PART'] = 'CC'
#--> CC cliticized to an RP

ATB_TO_PENN['DEM_PRON_F'] = 'DT'
ATB_TO_PENN['DEM_PRON_FD'] = 'DT'
ATB_TO_PENN['DEM_PRON_FS'] = 'DT'
ATB_TO_PENN['DEM_PRON_MD'] = 'DT'
ATB_TO_PENN['DEM_PRON_MP'] = 'DT'
ATB_TO_PENN['DEM_PRON_MS'] = 'DT'
ATB_TO_PENN['DET'] = 'DT'

ATB_TO_PENN['DET+ADJ'] = 'JJ'
ATB_TO_PENN['DET+ADJ+NSUFF_FEM_DU_ACCGEN'] = 'JJ'
ATB_TO_PENN['DET+ADJ+NSUFF_FEM_DU_NOM'] = 'JJ'
ATB_TO_PENN['DET+ADJ+NSUFF_FEM_PL'] = 'JJ'
ATB_TO_PENN['DET+ADJ+NSUFF_FEM_SG'] = 'JJ'
ATB_TO_PENN['DET+ADJ+NSUFF_MASC_DU_ACCGEN'] = 'JJ'
ATB_TO_PENN['DET+ADJ+NSUFF_MASC_DU_NOM'] = 'JJ'
ATB_TO_PENN['DET+ADJ+NSUFF_MASC_PL_ACCGEN'] = 'JJ'
ATB_TO_PENN['DET+ADJ+NSUFF_MASC_PL_NOM'] = 'JJ'
ATB_TO_PENN['DET+ADJ_PROP'] = 'JJ'
ATB_TO_PENN['DET+ADJ_PROP+NSUFF_FEM_SG'] = 'JJ'
ATB_TO_PENN['DET+ADJ_PROP+NSUFF_MASC_PL_ACCGEN'] = 'JJ'

ATB_TO_PENN['DET+ADV+NSUFF_FEM_SG'] = 'RB'

ATB_TO_PENN['DET+NEG_PART'] = 'DT'
#--> DT cliticized to an RP

ATB_TO_PENN['DET+NOUN'] = 'NN'

ATB_TO_PENN['DET+NOUN+NSUFF_FEM_DU_ACCGEN'] = 'NNS'
ATB_TO_PENN['DET+NOUN+NSUFF_FEM_DU_NOM'] = 'NNS'
ATB_TO_PENN['DET+NOUN+NSUFF_FEM_PL'] = 'NNS'

ATB_TO_PENN['DET+NOUN+NSUFF_FEM_SG'] = 'NN'

ATB_TO_PENN['DET+NOUN+NSUFF_MASC_DU_ACCGEN'] = 'NNS'
ATB_TO_PENN['DET+NOUN+NSUFF_MASC_DU_NOM'] = 'NNS'
ATB_TO_PENN['DET+NOUN+NSUFF_MASC_PL_ACCGEN'] = 'NNS'
ATB_TO_PENN['DET+NOUN+NSUFF_MASC_PL_NOM'] = 'NNS'

ATB_TO_PENN['DET+NOUN_PROP'] = 'NNP'

ATB_TO_PENN['DET+NOUN_PROP+NSUFF_FEM_PL'] = 'NNPS'

ATB_TO_PENN['DET+NOUN_PROP+NSUFF_FEM_SG'] = 'NNP'

ATB_TO_PENN['DET+NOUN_PROP+NSUFF_MASC_DU_ACCGEN'] = 'NNPS'
ATB_TO_PENN['DET+NOUN_PROP+NSUFF_MASC_PL_ACCGEN'] = 'NNPS'
ATB_TO_PENN['DET+NOUN_PROP+NSUFF_MASC_PL_NOM'] = 'NNPS'

ATB_TO_PENN['DET+PREP'] = 'DT'
#--> DT cliticized to an IN

ATB_TO_PENN['EMPHATIC_PARTICLE'] = 'RP'
ATB_TO_PENN['EXCEPT_PART'] = 'RP'

ATB_TO_PENN['FUNC_WORD'] = 'IN'
#(subordinating conjunction, rather than preposition)

ATB_TO_PENN['FUT+IV1P+IV'] = 'VBP'
ATB_TO_PENN['FUT+IV1S+IV'] = 'VBP'
ATB_TO_PENN['FUT+IV2MP+IV+IVSUFF_SUBJ:MP_MOOD:I'] = 'VBP'
ATB_TO_PENN['FUT+IV2MS+IV'] = 'VBP'
ATB_TO_PENN['FUT+IV3FS+IV'] = 'VBP'
#(imperfect verb, using the old present tense verb tag)

ATB_TO_PENN['FUT+IV3FS+VERB_PASSIVE'] = 'VBN'
#(passive verb, using the old past participle tag)

ATB_TO_PENN['FUT+IV3MD+IV+IVSUFF_SUBJ:D_MOOD:I'] = 'VBP'
ATB_TO_PENN['FUT+IV3MP+IV+IVSUFF_SUBJ:MP_MOOD:I'] = 'VBP'
ATB_TO_PENN['FUT+IV3MS+IV'] = 'VBP'
#(imperfect verb, using the old present tense verb tag)

ATB_TO_PENN['FUT+IV3MS+VERB_PASSIVE'] = 'VBN'
#(passive verb, using the old past participle tag)

ATB_TO_PENN['INTERJ'] = 'UH'
ATB_TO_PENN['INTERJ+NSUFF_MASC_SG_ACC_INDEF'] = 'UH'

ATB_TO_PENN['INTERROG_PART'] = 'RP'

ATB_TO_PENN['IV1P+IV'] = 'VBP'
#(imperfect verb, using the old present tense verb tag)

ATB_TO_PENN['IV1P+VERB_PASSIVE'] = 'VBN'
#(passive verb, using the old past participle tag)

ATB_TO_PENN['IV1S+IV'] = 'VBP'
#(imperfect verb, using the old present tense verb tag)

ATB_TO_PENN['IV1S+VERB_PASSIVE'] = 'VBN'
#(passive verb, using the old past participle tag)

ATB_TO_PENN['IV2D+IV+IVSUFF_SUBJ:D_MOOD:I'] = 'VBP'
ATB_TO_PENN['IV2FS+IV+IVSUFF_SUBJ:2FS_MOOD:SJ'] = 'VBP'
ATB_TO_PENN['IV2MP+IV+IVSUFF_SUBJ:MP_MOOD:I'] = 'VBP'
ATB_TO_PENN['IV2MP+IV+IVSUFF_SUBJ:MP_MOOD:SJ'] = 'VBP'
ATB_TO_PENN['IV2MS+IV'] = 'VBP'
#(imperfect verb, using the old present tense verb tag)

ATB_TO_PENN['IV2MS+VERB_PASSIVE'] = 'VBN'
#(passive verb, using the old past participle tag)

ATB_TO_PENN['IV3FD+IV+IVSUFF_SUBJ:D_MOOD:I'] = 'VBP'
ATB_TO_PENN['IV3FD+IV+IVSUFF_SUBJ:D_MOOD:SJ'] = 'VBP'
ATB_TO_PENN['IV3FP+IV+IVSUFF_SUBJ:FP'] = 'VBP'
ATB_TO_PENN['IV3FS+IV'] = 'VBP'
#(imperfect verb, using the old present tense verb tag)

ATB_TO_PENN['IV3FS+VERB_PASSIVE'] = 'VBN'
#(passive verb, using the old past participle tag)

ATB_TO_PENN['IV3MD+IV+IVSUFF_SUBJ:D_MOOD:I'] = 'VBP'
ATB_TO_PENN['IV3MD+IV+IVSUFF_SUBJ:D_MOOD:SJ'] = 'VBP'
ATB_TO_PENN['IV3MP+IV+IVSUFF_SUBJ:MP_MOOD:I'] = 'VBP'
ATB_TO_PENN['IV3MP+IV+IVSUFF_SUBJ:MP_MOOD:SJ'] = 'VBP'
#(imperfect verb, using the old present tense verb tag)

ATB_TO_PENN['IV3MP+VERB_PASSIVE+IVSUFF_SUBJ:MP_MOOD:I'] = 'VBN'
#(passive verb, using the old past participle tag)

ATB_TO_PENN['IV3MS+IV'] = 'VBP'
#(imperfect verb, using the old present tense verb tag)

ATB_TO_PENN['IV3MS+VERB_PASSIVE'] = 'VBN'
#(passive verb, using the old past participle tag)

ATB_TO_PENN['IVSUFF_DO:1P'] = 'PRP'
ATB_TO_PENN['IVSUFF_DO:1S'] = 'PRP'
ATB_TO_PENN['IVSUFF_DO:2MP'] = 'PRP'
ATB_TO_PENN['IVSUFF_DO:2MS'] = 'PRP'
ATB_TO_PENN['IVSUFF_DO:3D'] = 'PRP'
ATB_TO_PENN['IVSUFF_DO:3FS'] = 'PRP'
ATB_TO_PENN['IVSUFF_DO:3MP'] = 'PRP'
ATB_TO_PENN['IVSUFF_DO:3MS'] = 'PRP'

ATB_TO_PENN['NEG_PART'] = 'RP'
ATB_TO_PENN['NEG_PART+PVSUFF_SUBJ:3MS'] = 'RP'

ATB_TO_PENN['NO_FUNC'] = 'NNP'
#--> no POS tag given, but I'd say NNP is probably a good guess for most of
#these, since most though not all unknown words are names.

ATB_TO_PENN['NON_ALPHABETIC'] = 'FW'
ATB_TO_PENN['NON_ARABIC'] = 'FW'
#--> FW or NUM or punctuation
#(non-Arabic characters)

ATB_TO_PENN['NOUN'] = 'NN'

ATB_TO_PENN['NOUN+NSUFF_FEM_DU_ACCGEN'] = 'NNS'
ATB_TO_PENN['NOUN+NSUFF_FEM_DU_ACCGEN_POSS'] = 'NNS'
ATB_TO_PENN['NOUN+NSUFF_FEM_DU_NOM'] = 'NNS'
ATB_TO_PENN['NOUN+NSUFF_FEM_DU_NOM_POSS'] = 'NNS'
ATB_TO_PENN['NOUN+NSUFF_FEM_PL'] = 'NNS'

ATB_TO_PENN['NOUN+NSUFF_FEM_SG'] = 'NN'

ATB_TO_PENN['NOUN+NSUFF_MASC_DU_ACCGEN'] = 'NNS'
ATB_TO_PENN['NOUN+NSUFF_MASC_DU_ACCGEN_POSS'] = 'NNS'
ATB_TO_PENN['NOUN+NSUFF_MASC_DU_NOM'] = 'NNS'
ATB_TO_PENN['NOUN+NSUFF_MASC_DU_NOM_POSS'] = 'NNS'
ATB_TO_PENN['NOUN+NSUFF_MASC_PL_ACCGEN'] = 'NNS'
ATB_TO_PENN['NOUN+NSUFF_MASC_PL_ACCGEN_POSS'] = 'NNS'
ATB_TO_PENN['NOUN+NSUFF_MASC_PL_NOM'] = 'NNS'
ATB_TO_PENN['NOUN+NSUFF_MASC_PL_NOM_POSS'] = 'NNS'

ATB_TO_PENN['NOUN+NSUFF_MASC_SG_ACC_INDEF'] = 'NN'

ATB_TO_PENN['NOUN_PROP'] = 'NNP'

ATB_TO_PENN['NOUN_PROP+NSUFF_FEM_PL'] = 'NNPS'

ATB_TO_PENN['NOUN_PROP+NSUFF_FEM_SG'] = 'NNP'

ATB_TO_PENN['NOUN_PROP+NSUFF_MASC_PL_ACCGEN'] = 'NNPS'

ATB_TO_PENN['NOUN_PROP+NSUFF_MASC_SG_ACC_INDEF'] = 'NNP'

ATB_TO_PENN['NUM'] = 'CD'

ATB_TO_PENN['NUMERIC_COMMA'] = ','
#--> , or decimal point
#(This is an Arabic letter that looks like a comma, and is therefore often
#used in place of a comma for punctuation or for decimal points.)

ATB_TO_PENN['PART'] = 'RP'

ATB_TO_PENN['POSS_PRON_1P'] = 'PRP$'
ATB_TO_PENN['POSS_PRON_1S'] = 'PRP$'
ATB_TO_PENN['POSS_PRON_2FS'] = 'PRP$'
ATB_TO_PENN['POSS_PRON_2MP'] = 'PRP$'
ATB_TO_PENN['POSS_PRON_2MS'] = 'PRP$'
ATB_TO_PENN['POSS_PRON_3D'] = 'PRP$'
ATB_TO_PENN['POSS_PRON_3FP'] = 'PRP$'
ATB_TO_PENN['POSS_PRON_3FS'] = 'PRP$'
ATB_TO_PENN['POSS_PRON_3MP'] = 'PRP$'
ATB_TO_PENN['POSS_PRON_3MS'] = 'PRP$'

ATB_TO_PENN['PREP'] = 'IN'
ATB_TO_PENN['PREP+NSUFF_FEM_SG'] = 'IN'
ATB_TO_PENN['PREP+NSUFF_MASC_SG_ACC_INDEF'] = 'IN'
ATB_TO_PENN['PREP_PROP'] = 'IN'

ATB_TO_PENN['PRON'] = 'PRP'
ATB_TO_PENN['PRON_1P'] = 'PRP'
ATB_TO_PENN['PRON_1S'] = 'PRP'
ATB_TO_PENN['PRON_2FS'] = 'PRP'
ATB_TO_PENN['PRON_2MP'] = 'PRP'
ATB_TO_PENN['PRON_2MS'] = 'PRP'
ATB_TO_PENN['PRON_3D'] = 'PRP'
ATB_TO_PENN['PRON_3FP'] = 'PRP'
ATB_TO_PENN['PRON_3FS'] = 'PRP'
ATB_TO_PENN['PRON_3MP'] = 'PRP'
ATB_TO_PENN['PRON_3MS'] = 'PRP'

ATB_TO_PENN['PUNC'] = '.'
#--> , or . or :
#(We use the PUNC tag for all types of punctuation (period, comma, etc.),
#with the exception of the Arabic character punctuation (which is tagged
#NUMERIC_COMMA).  Actual conversion to Penn English POS tags would require
#looking at the token itself as well as the tag.)

ATB_TO_PENN['PVSUFF_DO:1P'] = 'PRP'
ATB_TO_PENN['PVSUFF_DO:1S'] = 'PRP'
ATB_TO_PENN['PVSUFF_DO:3D'] = 'PRP'
ATB_TO_PENN['PVSUFF_DO:3FS'] = 'PRP'
ATB_TO_PENN['PVSUFF_DO:3MP'] = 'PRP'
ATB_TO_PENN['PVSUFF_DO:3MS'] = 'PRP'
ATB_TO_PENN['PVSUFF_SUBJ:1P'] = 'PRP'
ATB_TO_PENN['PVSUFF_SUBJ:1S'] = 'PRP'
ATB_TO_PENN['PVSUFF_SUBJ:3FS'] = 'PRP'

ATB_TO_PENN['REL_ADV'] = 'WRB'

ATB_TO_PENN['REL_PRON'] = 'WP'

ATB_TO_PENN['REL_PRON+PREP'] = 'WP'
#--> WP cliticized to an IN

ATB_TO_PENN['RESULT_CLAUSE_PARTICLE'] = 'RP'
ATB_TO_PENN['SUBJUNC'] = 'RP'

ATB_TO_PENN['VERB_PASSIVE'] = 'VBN'
ATB_TO_PENN['VERB_PASSIVE+PVSUFF_SUBJ:1S'] = 'VBN'
ATB_TO_PENN['VERB_PASSIVE+PVSUFF_SUBJ:3FS'] = 'VBN'
ATB_TO_PENN['VERB_PASSIVE+PVSUFF_SUBJ:3MD'] = 'VBN'
ATB_TO_PENN['VERB_PASSIVE+PVSUFF_SUBJ:3MP'] = 'VBN'
ATB_TO_PENN['VERB_PASSIVE+PVSUFF_SUBJ:3MS'] = 'VBN'
#(passive verb, using the old past participle tag)

ATB_TO_PENN['VERB_PERFECT'] = 'VBD'
ATB_TO_PENN['VERB_PERFECT+PVSUFF_SUBJ:1P'] = 'VBD'
ATB_TO_PENN['VERB_PERFECT+PVSUFF_SUBJ:1S'] = 'VBD'
ATB_TO_PENN['VERB_PERFECT+PVSUFF_SUBJ:2FS'] = 'VBD'
ATB_TO_PENN['VERB_PERFECT+PVSUFF_SUBJ:2MP'] = 'VBD'
ATB_TO_PENN['VERB_PERFECT+PVSUFF_SUBJ:3FD'] = 'VBD'
ATB_TO_PENN['VERB_PERFECT+PVSUFF_SUBJ:3FP'] = 'VBD'
ATB_TO_PENN['VERB_PERFECT+PVSUFF_SUBJ:3FS'] = 'VBD'
ATB_TO_PENN['VERB_PERFECT+PVSUFF_SUBJ:3MD'] = 'VBD'
ATB_TO_PENN['VERB_PERFECT+PVSUFF_SUBJ:3MP'] = 'VBD'
ATB_TO_PENN['VERB_PERFECT+PVSUFF_SUBJ:3MS'] = 'VBD'
#(perfect verb, using the old past tense verb tag)

ATB_TO_PENN['-NONE-'] = '-NONE-'

#==========================================================================
PENN_POS_TAGS = {
    'CC':	'Coordinating conjunction',
    'CD':	'Cardinal number',
    'DT':	'Determiner',
    'EX':	'Existential there',
    'FW':	'Foreign word',
    'IN':	'Preposition or subordinating conjunction',
    'JJ':	'Adjective',
    'JJR':	'Adjective, comparative',
    'JJS':	'Adjective, superlative',
    'LS':	'List item marker',
    'MD':	'Modal',
    'NN':	'Noun, singular or mass',
    'NNS':	'Noun, plural',
    'NNP':	'Proper noun, singular',
    'NNPS':	'Proper noun, plural',
    'PDT':	'Predeterminer',
    'POS':	'Possessive ending',
    'PRP':	'Personal pronoun',
    'PRP$':	'Possessive pronoun',
    'RB':	'Adverb',
    'RBR':	'Adverb, comparative',
    'RBS':	'Adverb, superlative',
    'RP':	'Particle',
    'SYM':	'Symbol',
    'TO':	'to',
    'UH':	'Interjection',
    'VB':	'Verb, base form',
    'VBD':	'Verb, past tense',
    'VBG':	'Verb, gerund or present participle',
    'VBN':	'Verb, past participle',
    'VBP':	'Verb, non-3rd person singular present',
    'VBZ':	'Verb, 3rd person singular present',
    'WDT':	'Wh-determiner',
    'WP':	'Wh-pronoun',
    'WP$':	'Possessive wh-pronoun',
    'WRB':	'Wh-adverb',
    ',':	'punctuation, token is , (PUNC)',
    '.':	'punctuation, token is . (PUNC)',
    ':':	'punctuation, token is : or other (PUNC)',
    }

ARABIC_POS_TAGS = {
    'ABBREV':'Abbreviation',
    'ACC': 'Accusative',
    'ADJ':'Adjective',
    'ADJ_COMP': 'Comparative Adjective',
    'ADJ_NUM': 'Ordinal number',
    'ADJ.VN': 'Verbal Adjective',
    'ADV': 'Adverb',
    'CASE': 'Case',
    'CONJ': 'Conjunction',
    'CONNEC_PART': 'Connective Particle',
    'CV': ' Command Verb',
    'DEF': ' Definite',
    'DEM_PRON':'Demonstrative Pronoun',
    'DET': 'Determiner',
    'DIALECT': ' Dialect',
    'DO': ' Direct Object',
    'D': 'Dual ',
    'DU': 'Dual',
    'EMPHATIC_PART': 'Emphatic Particle',
    'F':'Feminine',
    'FEM': 'Feminine',
    'FOCUS_PART': 'Focus Particle',
    'FOREIGN':'Foreign Word',
    'FOREIGN_SCRIPT':'Foreign Script',
    'FUT':'Future',
    'FUT_PART': 'Future Particle',
    'GEN':'Genetive',
    'I': 'Indicative',
    'INDEF': ' Indefinite',
    'INTERJ': 'Interjection',
    'INTERROG_ADV': 'Interrogative Adverbs ',
    'INTERROG_PART': 'Interrogative Particle',
    'INTERROG_PRON': 'Interrogative Pronoun',
    'IV':'Imperfect Verb',
    'JUS_PART': 'Jussive Particle',
    'M':'Masculine',
    'MASC':'Masculine',
    'MOOD': 'Mood',
    'NSUFF': 'Noun Suffix',
    'NOM': 'Nominative',
    'NOUN': ' Noun',
    'NOUN_NUM': 'Cardinal Numbers',
    'NOUN_PROP': 'Proper Nouns',
    'NOUN_QUANT': 'Noun Quantifier',
    'NOUN.VN': 'Verbal Noun',
    'NEG_PART': ' Negative Particle',
    'PART': 'Particle',
    'PARTIAL':'Partial Word',
    'PASS': 'Passive',
    'PL':'Plural',
    'POSS': 'Possessive',
    'POSS_PRON': 'Possessive Pronoun',
    'PREP': 'Preposition',
    'PRON': 'Pronoun',
    'PSEUDO_VERB': 'PseudoVerb',
    'PUNC': ' Punctuation  ',
    'PV':'Perfect Verb',
    'RC_PART': ' Response Conditional Particle',
    'RESTRIC_PART': 'Restrictive Particle',
    'REL_ADV': ' Relative Adverb',
    'REL_PRON': ' Relative Pronoun',
    'S': 'Subjunctive',
    'SUBJ': 'Subject',
    'S': 'Singular',
    'SG': 'Singular',
    'SUB_CONJ': ' Subordinating Conjunction',
    'SUFF': 'Suffix',
    'TRANSERR':'Transcription error ',
    'TYPO': ' Typo',
    'VERB':'Verb',
    'VERB_PART': ' Verb Particle',
    'VOC_PART': 'Vocative Particle',
    '-NONE-': 'Empty Constituent',
    'LATIN': 'Latin Script',
    'GRAMMAR_PROBLEM': 'Error in constintuent',}

ARABIC_VERB_TAGS = {
    'CV': ' Command Verb',
    'IV':'Imperfect Verb',
    'PSEUDO_VERB': 'PseudoVerb',
    'PV':'Perfect Verb',
    'VERB':'Verb',
    'VERB_PART': ' Verb Particle',
    }


VERB_INFLECTION_TO_PROPS = {'CVSUFF_SUBJ:2FS',
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
    'PVSUFF_SUBJ:3MS',}
