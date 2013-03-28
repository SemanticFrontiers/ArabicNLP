def strip_diacritics(word):
    '''
    Removes diacritics of a Buckwalter encoded word.

    hamza
        hamza on alif: >
        hamza below alif: <
    alif
        madda on alif: |
        alif al-wasla: {
        dagger alif: `
    harakat
        fatha: a
        damma: u
        kasra: i
        fathatayn: F
        dammatayn: N
        kasratayn K
        shadda: ~
        sukun: o
    
    >>> strip_diacritics('tadAras')
    'tdArs'
    '''

    markers = [('>', 'A'),
               ('<', 'A'),
               ('|', 'A'),
               ('{', 'A'),
               ('a', ''),
               ('u', ''),
               ('i', ''),
               ('~', ''),
               ('o', ''),
               ('F', ''),
               ('N', ''),
               ('K', ''),
               ('`', '')]

    for marker, replacement in markers:
        word = word.replace(marker, replacement)

    return word
