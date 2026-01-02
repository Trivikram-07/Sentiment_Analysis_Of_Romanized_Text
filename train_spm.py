import sentencepiece as spm

spm.SentencePieceTrainer.train(
    input="cleaned_corpus.txt",
    model_prefix="spm",
    vocab_size=8000,
    model_type="unigram",
    character_coverage=1.0
)

print("SentencePiece model created successfully!")
