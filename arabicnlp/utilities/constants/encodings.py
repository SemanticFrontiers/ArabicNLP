# mapping borrowed from
# https://github.com/andyroberts/buckwalter2unicode/blob/master/buckwalter2unicode.py
BUCKWALTER_TO_UNICODE = {
    "'": u"\u0621", # hamza-on-the-line
    "|": u"\u0622", # madda
    ">": u"\u0623", # hamza-on-'alif
    "&": u"\u0624", # hamza-on-waaw
    "<": u"\u0625", # hamza-under-'alif
    "}": u"\u0626", # hamza-on-yaa'
    "A": u"\u0627", # bare 'alif
    "b": u"\u0628", # baa'
    "p": u"\u0629", # taa' marbuuTa
    "t": u"\u062A", # taa'
    "v": u"\u062B", # thaa'
    "j": u"\u062C", # jiim
    "H": u"\u062D", # Haa'
    "x": u"\u062E", # khaa'
    "d": u"\u062F", # daal
    "*": u"\u0630", # dhaal
    "r": u"\u0631", # raa'
    "z": u"\u0632", # zaay
    "s": u"\u0633", # siin
    "$": u"\u0634", # shiin
    "S": u"\u0635", # Saad
    "D": u"\u0636", # Daad
    "T": u"\u0637", # Taa'
    "Z": u"\u0638", # Zaa' (DHaa')
    "E": u"\u0639", # cayn
    "g": u"\u063A", # ghayn
    "_": u"\u0640", # taTwiil
    "f": u"\u0641", # faa'
    "q": u"\u0642", # qaaf
    "k": u"\u0643", # kaaf
    "l": u"\u0644", # laam
    "m": u"\u0645", # miim
    "n": u"\u0646", # nuun
    "h": u"\u0647", # haa'
    "w": u"\u0648", # waaw
    "Y": u"\u0649", # 'alif maqSuura
    "y": u"\u064A", # yaa'
    "F": u"\u064B", # fatHatayn
    "N": u"\u064C", # Dammatayn
    "K": u"\u064D", # kasratayn
    "a": u"\u064E", # fatHa
    "u": u"\u064F", # Damma
    "i": u"\u0650", # kasra
    "~": u"\u0651", # shaddah
    "o": u"\u0652", # sukuun
    "`": u"\u0670", # dagger 'alif
    "{": u"\u0671", # waSla
}


ARABIZI_TO_UNICODE = {
                "2": u"\u0621", # hamza-on-the-line
                "Aa": u"\u0622", # madda
                "2a": u"\u0623", # hamza-on-'alif
                "2u": u"\u0624", # hamza-on-waaw
                "2i": u"\u0625", # hamza-under-'alif
                "2y": u"\u0626", # hamza-on-yaa'
                "A": u"\u0627", # bare 'alif
                "b": u"\u0628", # baa'
                "ah": u"\u0629", # taa' marbuuTa
                "t": u"\u062A", # taa'
                "th": u"\u062B", # thaa'
                "j": u"\u062C", # jiim
                "7": u"\u062D", # Haa'
                "5": u"\u062E", # khaa'
                "d": u"\u062F", # daal
                "dh": u"\u0630", # dhaal
                "r": u"\u0631", # raa'
                "z": u"\u0632", # zaay
                "s": u"\u0633", # siin
                "sh": u"\u0634", # shiin
                "9": u"\u0635", # Saad
                "9'": u"\u0636", # Daad
                "6": u"\u0637", # Taa'
                "6'": u"\u0638", # Zaa' (DHaa')
                "3": u"\u0639", # cayn
                "3'": u"\u063A", # ghayn
                "t": u"\u0640", # taTwiil
                "f": u"\u0641", # faa'
                "q": u"\u0642", # qaaf
                "k": u"\u0643", # kaaf
                "l": u"\u0644", # laam
                "m": u"\u0645", # miim
                "n": u"\u0646", # nuun
                "h": u"\u0647", # haa'
                "w": u"\u0648", # waaw
                "Y": u"\u0649", # 'alif maqSuura
                "y": u"\u064A", # yaa'
                "F": u"\u064B", # fatHatayn
                "N": u"\u064C", # Dammatayn
                "K": u"\u064D", # kasratayn
                "a": u"\u064E", # fatHa
                "u": u"\u064F", # Damma
                "i": u"\u0650", # kasra
                "~": u"\u0651", # shaddah
                "o": u"\u0652", # sukuun
                "`": u"\u0670", # dagger 'alif
                "{": u"\u0671", # waSla
}

UNICODE_TO_ARABIZI = {v:k for k,v in ARABIZI_TO_UNICODE.iteritems()}
UNICODE_TO_BUCKWALTER = {v:k for k,v in BUCKWALTER_TO_UNICODE.iteritems()}
BUCKWALTER_TO_ARABIZI = {UNICODE_TO_BUCKWALTER[v]:k for k,v in ARABIZI_TO_UNICODE.iteritems()}
