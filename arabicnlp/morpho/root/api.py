#coding: utf-8

class Rooter(object):
    '''
    An interface for extracting the "root" of an Arabic word.
    '''
    
    def root(self, token):
        '''
        Return the root (الجذر) for an Arabic word.

        :param token: The token that should be rooted.
        :type token: str
        '''
        raise NotImplementedError()

        
if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
    
