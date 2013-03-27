#coding: utf-8

from arabicnlp.morpho.root.api import Rooter
from arabicnlp.utilities       import constants

class SAMARooter(Rooter):
    '''
    A special rooter that looks up SAMA lemma roots.
    '''

    def root(self, lemma):
        '''
        Takes a SAMA-specified lemma and returns its root (الجذر).
        '''
        return constants.SAMA_LEMMA_TO_ROOT.get(lemma, None)

    def pattern(self, lemma, root=None):
        '''
        Takes a SAMA-specified lemma and returns its pattern (الوزن).
        '''

        if not root:
            root = self.root(lemma)
            if not root:
                return None

        # no "real" roots are longer than 4
        if len(root) > 4 or len(root) < 3:
            return None

        lemma = lemma.split('_')[0]
        lemma = lemma.split('-')[0]

        root_placeholders = '123456789'[:len(root)]

        temp = lemma
        i = len(lemma)
        for p, r in reversed(zip(root_placeholders, root)):
            i = temp.rfind(r, 0, i)
            if i < 0:
                return None
            temp = temp[:i] + p + temp[i+1:]
            
        return temp

    def ppattern(self, lemma, root=None):
        '''
        Takes a SAMA-specified lemma and returns its pattern (الوزن) in 3rabizi.
        '''
        p = self.pattern(lemma, root)

        if not p:
            return p

        p = p.replace('1', 'f')
        p = p.replace('3', 'l')
        p = p.replace('2', '3')

        return p


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
