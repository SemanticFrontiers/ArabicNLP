#coding: utf-8

from arabicnlp.morpho.root.api import Rooter
from arabicnlp.utilities       import constants

class SAMARooter(Rooter):
    '''
    A special rooter that looks up SAMA lemma roots.
    '''

    def root(self, lemma):
        '''
        A special rooter that takes a SAMA-specified lemma and returns its root (الجذر).
        '''
        return constants.SAMA_LEMMA_TO_ROOT.get(lemma, None)

    def get_template(self, lemma):
        pass

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
