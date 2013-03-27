Installation of SAMA
=

The Standard Arabic Morphological Analyzer
([SAMA](http://www.ldc.upenn.edu/Catalog/catalogEntry.jsp?catalogId=LDC2010L01))
enumerates all consistent morphologic analyses of an Arabic word token.  It is
based on a finite-state machine (FSM) that generates consistent analyses using a
lexicon and constraint tables. 

The analyzer comes bundled with three dictionaries that other applications NLP
tools often leverage:

1. `dictStems` - roots, lemmas, and stems
2. `dictPrefixes` - prefixes
3. `dictSuffixes` -  suffixes

It is distributed by the Linguistic Data Consortium ([LDC](http://www.ldc.upenn.edu/)).

Installation 
-

We assume you have obtained the SAMA tarball `LDC2010L01.tgz`, from the LDC's
[website](http://www.ldc.upenn.edu/Catalog/catalogEntry.jsp?catalogId=LDC2010L01).


*Method 1*
```python
>>> import arabicnlp as anlp
>>> anlp.install('SAMA', '/Users/maxlikely/Desktop/LDC2010L01.tgz')
```

*Method 2*
```zsh
$ pwd
/Users/maxlikely/projects/ArabicNLP/lib/SAMA
$ ls
LDC2010L01.tgz README.md
$ tar -xvzf LDC2010L01.tgz
$ ls
LDC2010L01.tgz README.md      sama_3_1
```
