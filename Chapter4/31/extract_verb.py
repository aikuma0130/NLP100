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

def extract_verb(morphemes):
    result = []
    for morpheme in morphemes:
        if morpheme['pos'] == '動詞':
            result.append(morpheme['surface'])

    return result

if __name__ == '__main__':
    lines = read_mecab_file('../neko.txt')
    result = []
    for morphemes in lines:
        result += extract_verb(morphemes)
    print(result)

