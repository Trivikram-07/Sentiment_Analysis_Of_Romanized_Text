import sentencepiece as spm
import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

# Load tokenizer
sp = spm.SentencePieceProcessor(model_file="spm.model")

df = pd.read_csv("data.csv")

label_map = {"NEG":0, "NTL":1, "POS":2}
df["label"] = df["label"].map(label_map)

def encode(text):
    return sp.encode(text.lower(), out_type=int)

X = [encode(t) for t in df["text"].astype(str)]
X = pad_sequences(X, maxlen=60)
y = to_categorical(df["label"], 3)

Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.15)

model = Sequential([
    Embedding(input_dim=8000, output_dim=128, mask_zero=True),
    LSTM(128),
    Dense(3, activation="softmax")
])

model.compile("adam", "categorical_crossentropy", metrics=["accuracy"])
model.fit(Xtr, ytr, epochs=10, batch_size=64, validation_split=0.1)

print("Test accuracy:", model.evaluate(Xte, yte))
model.save("final_model.keras")
