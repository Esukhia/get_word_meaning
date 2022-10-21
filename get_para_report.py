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
from count_sentences_para import sentence_token


def get_tokens(wt):
    """
    tokenize tibetan paragraph with pos
    """
    tokens = wt.tokenize(tibetan_para, split_affixes=False)
    return tokens


def word_pos_definition():
    """
    Returns word pos meaning
    """
    with open('tibetan_dict.yml') as f:
        tibetan_dictionary = yaml.load(f, Loader=SafeLoader)

    word_pos_definition_content = []
    with open('tokenized_para.csv', 'r') as file:
        for line in file:
            word, pos = line.split(' ')[:2]
            definition = tibetan_dictionary.get(word.strip())
            word_pos_definition_content.append(
                word if definition is None
                else f"{word} {pos} {definition} "
            )
    with open('get_para_report.csv', 'w') as final_csv_file:
        final_csv_file.write('\n'.join(word_pos_definition_content))


word_pos_definition()

if __name__ == "__main__":
    wt = WordTokenizer()
    tibetan_tokenized_string = ""
    tibetan_para = Path('tibetan_paragraph.txt').read_text(encoding='utf-8')
    tokens = get_tokens(wt)
    for token in tokens:
        tibetan_tokenized_string += f"{token.text} {token.pos}\n"
    Path('tokenized_para.csv').write_text(tibetan_tokenized_string, encoding='utf-8')

    # print number of sentences
    sentence_count = sentence_token()
    print(f"Number of sentences in the paragraph is {sentence_count}")
