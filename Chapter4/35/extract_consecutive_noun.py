import MeCab
import sys

def read_mecab_file(filename):
    with open(filename) as f:
        lines = f.readlines()

    result = []
    m = MeCab.Tagger()
    for line in lines:
        node = m.parseToNode(line)
        li = []
        while node:
            feature = node.feature.split(',')
            li.append({
                'surface': node.surface,
                'base': feature[6],
                'pos': feature[0],
                'pos1': feature[1],
            })
            node = node.next
        result.append(li)

    return result

def extract_consecutive_noun(morphemes):
    result = []
    nouns = []
    consecutive_noun = False
    for morpheme in morphemes:
        if consecutive_noun == True:
            if morpheme['pos'] == '名詞':
                nouns.append(morpheme['surface'])
            else:
                if len(nouns) > 1:
                    result.append("".join(nouns))
                consecutive_noun = False
                nouns = []
        else:
            if morpheme['pos'] == '名詞':
                nouns.append(morpheme['surface'])
                consecutive_noun = True

    return result

def extract_target_morpheme(morphemes, key=None, value=None):
    result = []
    for morpheme in morphemes:
        if key != None and value != None:
            if morpheme[key] == value:
                result.append(morpheme)
        else:
            result.append(morpheme)

    return result

if __name__ == '__main__':
    lines = read_mecab_file('../neko.txt')
    result = []
    for morphemes in lines:
        result += extract_consecutive_noun(morphemes)
    print(result)

