import pandas as pd
from telugu_normalizer import normalize_sentence

df = pd.read_csv("data.csv")

with open("cleaned_corpus.txt", "w", encoding="utf8") as f:
    for text in df["text"].astype(str):
        f.write(normalize_sentence(text) + "\n")

print("cleaned_corpus.txt created")
