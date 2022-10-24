"""
You will be given a paragraph in Tibetan. You need to generate a report in csv.
Para report table should contain following things:
- tokenized word
- POS tag
- Word meaning
eg:
ཀུན་སྤྱོད   NOUN    མིའི་བསམ་ཚུལ་སྤྱོད་ཚུལ་གྱི་སྤྱི་མིང་སྟེ། རྟོགས་པ་ལྷ་དང་མཉམ་ཡང་། ཀུན་སྤྱོད་མི་དང་མཐུན་དགོས་ལྟ་བུ།
- need the count of sentences in the given para.
"""
import yaml
import string
from pathlib import Path
from botok import WordTokenizer
from yaml.loader import SafeLoader
from botok.tokenizers.sentencetokenizer import sentence_tokenizer


def get_tokens(wt, tibetan_para):
    """
    tokenize tibetan paragraph with pos
    """
    tokens = wt.tokenize(tibetan_para, split_affixes=False)
    return tokens

def sentence_token():
    """
    count the number of sentences in a given paragraph
    """
    wt = WordTokenizer()
    tibetan_para = Path('./tibetan_paragraph.txt').read_text(encoding='utf-8')
    tokens = get_tokens(wt, tibetan_para)
    sentences = sentence_tokenizer(tokens)
    count_sentence = f"total count of sentence is {len(sentences)}"
    with open('get_para_report.csv', 'a') as file:
        file.write(str(count_sentence))

def word_pos_definition():
    """
    Returns word pos meaning
    """
    with open('tibetan_dict.yml') as f:
        tibetan_dictionary = yaml.load(f, Loader=SafeLoader)

    word_pos_definition_content = []
    with open('tokenized_para.txt', 'r') as file:
        for line in file:
            word = line.split(' ')[0]
            pos = ''.join([i for i in line if i in string.ascii_uppercase])
            definition = tibetan_dictionary.get(word.strip())
            word_pos_definition_content.append(
                word if definition is None
                else f"{word} {pos} {definition} "
            )
    with open('get_para_report.csv', 'w') as final_csv_file:
        final_csv_file.write('\n'.join(word_pos_definition_content))


if __name__ == "__main__":
    
    wt = WordTokenizer()
    tibetan_tokenized_string = ""
    tibetan_para = Path('tibetan_paragraph.txt').read_text(encoding='utf-8')
    tokens = get_tokens(wt, tibetan_para)
    for token in tokens:
        tibetan_tokenized_string += f"{token.text} {token.pos}\n"
    Path('tokenized_para.txt').write_text(tibetan_tokenized_string, encoding ='utf-8')


    word_pos_definition()
    
    # print number of sentences
    sentence_token()