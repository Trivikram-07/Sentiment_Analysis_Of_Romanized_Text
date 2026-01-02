import re

ASP_MAP = {'dh':'d','th':'t','bh':'b','gh':'g','kh':'k'}

def normalize_sentence(text):
    text = text.lower()
    text = re.sub(r"http\S+|www\.\S+", "", text)
    text = re.sub(r"[^a-z0-9 ]+", " ", text)
    text = re.sub(r"(.)\1{2,}", r"\1\1", text)

    words = []
    for w in text.split():
        for k,v in ASP_MAP.items():
            w = w.replace(k, v)
        w = re.sub(r"(.)\1+", r"\1", w)
        words.append(w)

    return " ".join(words)
