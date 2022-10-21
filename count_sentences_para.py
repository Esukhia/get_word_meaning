from botok import WordTokenizer
from botok.tokenizers.sentencetokenizer import sentence_tokenizer
from pathlib import Path


def get_tokens(wt, text):
    tokens = wt.tokenize(text, split_affixes=False)
    return tokens


def sentence_token():
    wt = WordTokenizer()
    tibetan_para = Path('./tibetan_paragraph.txt').read_text(encoding='utf-8')
    tokens = get_tokens(wt, tibetan_para)
    sentences = sentence_tokenizer(tokens)
    print(len(sentences))
