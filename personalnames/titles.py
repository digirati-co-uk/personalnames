"""

Titles drawn from https://en.wikipedia.org/wiki/English_honorifics

"""


common_titles = ["master", "mr", "mister", "miss", "mrs", "ms", "mx"]

formal_titles = [
    "sir",
    "mistress",
    "madam",
    "dame",
    "lord",
    "lady",
    "the honourable",
    "hon",
    "the right honourable",
    "the most honourable",
    "rt hon",
]

professional_titles = ["dr", "dr.", "doctor", "professor", "chancellor", "vice-chancellor"]

post_nominals = ["esq", "esq.", "qc", "kc", "r.a.", "a.r.a.", "junior", "jr", "jr.", "senior", "sr", "sr."]

religious_titles = [
    "his holiness",
    "his all holiness",
    "his beatitude",
    "his excellency",
    "his most eminent highness",
    "his eminence",
    "the most reverend",
    "the most rev",
    "the most revd",
    "his grace",
    "his lordship",
    "the right reverend",
    "the rt rev",
    "the most revd",
    "the reverend",
    "the rev",
    "the revd",
    "fr",
    "father",
    "pr",
    "pastor",
    "brother",
    "br",
    "sister",
    "sr",
    "elder",
    "rabbi",
    "imam",
    "imām",
    "shaykh",
    "sheikh",
    "muftī",
    "sharif",
]

prefixes = common_titles + religious_titles + formal_titles + professional_titles
suffixes = post_nominals
