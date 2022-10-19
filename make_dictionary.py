from pathlib import Path


def convert_dict_to_yaml():
    """
    Convert Tibetan_dict.txt file into yaml file containing dictionary
    having key as word and value as meaning of it
    """
    tibetan_dict_txt_file = Path("test_dict.txt")
    tibetan_dict = {}
    tibetan_dict_txt_content = tibetan_dict_txt_file.read_text()
    tibetan_dict_entries = tibetan_dict_txt_content.splitlines()
    for tibetan_dict_entry in tibetan_dict_entries:
        tibetan_dict_entry_info = tibetan_dict_entry.split("༑")
        tibetan_dict[str(tibetan_dict_entry_info[0])] = tibetan_dict_entry_info[1]
    Path('Tibetan_Dictionary.yaml')


convert_dict_to_yaml()
