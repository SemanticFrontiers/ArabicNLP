import os

DATA_PATH = os.path.join(os.path.abspath(os.environ['DATA_PATH']), 'ontonotes/raw')

DEBUG = False

root_to_lemmas = {}
lemma_to_stems = {}

# inverted indices
lemma_to_root = {}
stem_to_root  = {}
stem_to_lemma = {}

def dictStems(filename):
    with open(filename) as fin:
        for line in fin:
            yield line.strip()

def parse_line(line, state):

    # root case
    if line.startswith(';--- '):
        if DEBUG:
            print 'root found [%s]' % line

        root = line.split()[1]

        if root in root_to_lemmas:
            if DEBUG:
                print 'DUPLICATE ROOTS! (%s)' % root
            #raise ValueError('duplicate roots! (%s)' % root)
        else:
            root_to_lemmas[root] = []

        state['root'] = root

    # lemma case
    elif line.startswith(';; '):
        if DEBUG:
            print '\tlemma found [%s]' % line

        lemma = line.split()[1]
        state['lemma'] = lemma

        root_to_lemmas[state['root']].append(lemma)

        #if lemma in lemma_to_stems:
        #    raise ValueError('oh no, duplicate lemmas across roots! (%s)' % lemma)

        #lemma_to_stems[lemma] = []


    # catchall
    elif line.startswith(';'):
        # should take care of ; ========= Alif ...
        # should take care of ;
        pass

    # stems case
    else:
        pass
        #print '\t\tstem found [%s]' % line
        #stem = line.split('\t')
        #lemma_to_stems[state['lemma']].append(stem)



def initialize_indices(filename):
    '''
    initiliazes all indices given the dictStems file
    '''

    # regular indices
    state = {}
    for line in dictStems(filename):
        parse_line(line, state)

    # inverted indices
    for root, lemmas in root_to_lemmas.iteritems():
        for lemma in lemmas:
            if lemma in lemma_to_root:
                raise ValueError('lemma-to-MANY-roots (%s --> %s, %s)' % (lemma, lemma_to_root[lemma], root))
            lemma_to_root[lemma] = root

    #for lemma, stems in lemma_to_stems.iteritems():
    #    for stem in stems:
    #        stem = stem[0]
    #        if stem in stem_to_lemma:
    #            raise ValueError('stem-to-MANY-lemmas (%s --> %s, %s)' % (stem, stem_to_lemma[stem], lemma))
    #        stem_to_lemma[stem] = lemma

    #        if stem in stem_to_root:
    #            raise ValueError('stem-to-MANY-roots (%s --> %s, %s)' % (stem, stem_to_root[stem], lemma_to_root[lemma]))
    #        stem_to_root[stem] = lemma_to_root[lemma]


def get_root(lemma):
    if not lemma_to_root:
        filename = os.path.join(DATA_PATH, 'dictStems')
        initialize_indices(filename)
    return lemma_to_root.get(lemma, None)

def get_template(lemma):
    pass

if __name__ == '__main__':
    initialize_indices('/Users/maxlikely/projects/aramorph/src/java/gpl/pierrick/brihaye/aramorph/dictionaries/dictStems')

