import streamlit as st
import numpy as np
import tensorflow as tf
import sentencepiece as spm
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ------------------------------
# Load model & tokenizer
# ------------------------------
@st.cache_resource
def load_model_and_tokenizer():
    model = tf.keras.models.load_model("final_model.keras")
    sp = spm.SentencePieceProcessor()
    sp.load("spm.model")
    return model, sp

model, sp = load_model_and_tokenizer()

# ------------------------------
# Label mapping (same as training)
# ------------------------------
label_map = {
    0: "NEGATIVE",
    1: "NEUTRAL",
    2: "POSITIVE"
}

MAX_LEN = 60

# ------------------------------
# Streamlit UI
# ------------------------------
st.set_page_config(page_title="Telugu Sentiment Analyzer", layout="centered")

st.title("Telugu–English Sentiment Analysis")
st.write("Enter a Telugu-English (romanized) sentence below:")

user_input = st.text_area("Input text", height=120)

if st.button("Predict Sentiment"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        # Encode text
        ids = sp.encode_as_ids(user_input.lower())
        padded = pad_sequences([ids], maxlen=MAX_LEN, padding="post")

        # Predict
        preds = model.predict(padded)
        pred_class = int(np.argmax(preds))
        confidence = float(np.max(preds)) * 100

        # Display result
        st.subheader("Prediction Result")
        st.success(f"Sentiment: {label_map[pred_class]}")
        st.info(f"Confidence: {confidence:.2f}%")
