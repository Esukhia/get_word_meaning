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
from botok import WordTokenizer
from pathlib import Path
import yaml
from yaml.loader import SafeLoader


def get_tokens(wt):
    """
    tokenize tibetan paragraph with pos
    """
    tokens = wt.tokenize(tibetan_para, split_affixes=False)
    return tokens


def word_pos_meaning():
    """
    Returns word pos meaning
    """
    with open('tibetan_dict.yml') as f:
        data = yaml.load(f, Loader=SafeLoader)

    outputs = []
    with open('tokenized_para.csv', 'r') as file:
        for line in file:
            word, pos = line.split(' ')[:2]
            definition = data.get(word.strip())
            outputs.append(
                word if definition is None
                else f"{word} {pos} {definition} "
            )
    print(outputs)


word_pos_meaning()

if __name__ == "__main__":
    wt = WordTokenizer()
    tibetan_tokenized_string = ""
    tibetan_para = Path('tibetan_paragraph.txt').read_text(encoding='utf-8')
    tokens = get_tokens(wt)
    for token in tokens:
        tibetan_tokenized_string += f"{token.text} {token.pos}\n"
    Path('tokenized_para.csv').write_text(tibetan_tokenized_string, encoding='utf-8')
