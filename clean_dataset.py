# import pandas as pd
# from collections import Counter
# import json
# import re
# from telugu_normalizer import normalize_sentence, cluster_variants

# DATA_PATH = "data.csv"
# OUTPUT_PATH = "cleaned_corpus.txt"

# # ---------- precompiled regex (speed) ----------
# RE_ALPHA = re.compile(r"^[a-z]+$")
# RE_STOP = re.compile(
#     r"^(the|and|you|are|for|but|not|this|that|was|with|have|all|just|will|what|why|who|they|from|been|very|more|less|than|when|then|where|their|there|here)$"
# )
# RE_SUFFIX = re.compile(r"(tion|ing|ment|ness|able|ible|ful|est|ist|ism|ify|ive)$")
# RE_VOWEL_ONLY = re.compile(r"^[aeiou]+$")

# EN_COMMON = {
#     "movie","super","nice","love","waste","happy","sad","good","bad",
#     "bro","anna","fan","song","scene","matter","idea","point","final"
# }
# TEL_PHON = ("aa","ee","oo","uu","th","dh","ch","sh","bh","kh","ph",
#             "ll","rr","nd","nt","ng","tt","pp","kk","mm","nn")
# EN_CLUST = ("st","sp","fr","cl","cr","pl","tr","br","pr","gr")

# def looks_telugu(word):
#     if not RE_ALPHA.match(word): return False
#     if len(word) < 4 or len(word) > 12: return False
#     if RE_STOP.match(word): return False
#     if word in EN_COMMON: return False
#     if RE_SUFFIX.search(word): return False
#     if RE_VOWEL_ONLY.match(word): return False
#     if not any(p in word for p in TEL_PHON): return False
#     if any(word.startswith(c) for c in EN_CLUST): return False
#     return True

# # ---------- load ----------
# df = pd.read_csv(DATA_PATH)
# if "text" not in df.columns:
#     raise ValueError("data.csv must have a 'text' column")

# print("Normalizing all text...")

# cleaned = []
# freq = Counter()

# # ---------- stream normalize + count ----------
# for t in df["text"].astype(str):
#     s = normalize_sentence(t)
#     cleaned.append(s)
#     freq.update(s.split())

# # ---------- select candidates ----------
# candidates = {w for w,c in freq.items() if c >= 8 and looks_telugu(w)}
# print(f"Clustering {len(candidates)} Telugu-like words...")

# # ---------- cluster ----------
# mapping = cluster_variants(candidates, freq)

# # ---------- stream write ----------
# with open(OUTPUT_PATH, "w", encoding="utf8") as f:
#     for s in cleaned:
#         toks = [mapping.get(tok, tok) for tok in s.split()]
#         f.write(" ".join(toks) + "\n")

# with open("token_mapping.json", "w", encoding="utf8") as f:
#     json.dump(mapping, f, indent=2)

# print("Cleaning complete!")
# print("Saved cleaned_corpus.txt")
# print("Saved token_mapping.json")
