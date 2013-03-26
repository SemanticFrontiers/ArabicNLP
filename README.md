Arabic NLP
=


Morphological Analyzer
-

```python
from arabicnlp.morpho.stem import ISRIStemmer
stemmer = ISRIStemmer()
stemmer.stem(u'حركات') # u'\u062d\u0631\u0643', حرك
```

**Other Morphological Tools**

It is absolutely crucial to obtain the latest version of SAMA for analysis purposes.
Aramorph and BAMA 2.0 are have outdated and buggy dictionaries (use at your own peril).

* MADA+TOKAN
* Standard Arabic Morphological Analyzer [SAMA 3.1](http://www.ldc.upenn.edu/Catalog/catalogEntry.jsp?catalogId=LDC2010L01)
* Buckwalter's Morphological Analyzer [BAMA 2.0](http://www.ldc.upenn.edu/Catalog/catalogEntry.jsp?catalogId=LDC2004L02).
* AraMorph [Aramorph](http://www.nongnu.org/aramorph/).

Arabic Sentence Structure
-
Arabic Clause Structure: wa wa wa...

This means that you will see a ton of Arabic Parse Trees of the form

`(ROOT (S (CONJ (S)...`
	
PRE+STEM+SUF
Two types of sentences
1. Jumla ismiya
2. Jumla fa3ilya
