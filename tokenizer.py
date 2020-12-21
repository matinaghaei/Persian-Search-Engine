import re
from positions import Positions


def cut_right(string, to_be_cut):
    if string.endswith(to_be_cut):
        return string[:-len(to_be_cut)]
    return string


def cut_left(string, to_be_cut):
    if string.startswith(to_be_cut):
        return string[len(to_be_cut):]
    return string


def normalize(token):
    t = token.strip('\u200b').strip('\u200c')
    t = cut_left(t, 'می\u200b')
    t = cut_left(t, 'می\u200c')
    t = cut_left(t, 'نمی\u200b')
    t = cut_left(t, 'نمی\u200c')
    t = cut_right(t, '\u200bها')
    t = cut_right(t, '\u200cها')
    t = cut_right(t, '\u200bهای')
    t = cut_right(t, '\u200cهای')
    t = cut_right(t, '\u200bتر')
    t = cut_right(t, '\u200cتر')
    t = cut_right(t, '\u200bترین')
    t = cut_right(t, '\u200cترین')
    return t.replace('\u200b', '').replace('\u200c', '')


def tokenize(string):
    tokens = re.split('\.|،|؛|\(|\)|«|»|/|:|؟|\s|-', string)
    normalized_tokens = []
    p = 0
    for token in tokens:
        if len(token) > 0 and not token.isnumeric():
            normalized_tokens.append(normalize(token))
            p += 1
    return normalized_tokens


class Tokenizer:

    def __init__(self, docs):
        self.documents = docs
        self.positionals = []
        self.build_positionals()

    def build_positionals(self):
        for i in range(len(self.documents)):
            tokens = tokenize(self.documents[i])
            positional = []
            p = 0
            for token in tokens:
                positional.append((token, p))
                p += 1
            positional.sort()
            merged_positional = []
            j = 0
            while j < len(positional):
                token = positional[j][0]
                positions = Positions(i, positional[j][1])
                k = j + 1
                while k < len(positional) and token == positional[k][0]:
                    positions.add(positional[k][1])
                    k += 1
                merged_positional.append((token, positions))
                j = k
            self.positionals.extend(merged_positional)
