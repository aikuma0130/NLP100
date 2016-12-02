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

def extract_a_no_b(morphemes):
    result = []
    a = ''
    a_no = False
    pre_morpheme = False
    for morpheme in morphemes:
        if a_no == True and morpheme['pos'] == '名詞':
            result.append(a + 'の' + morpheme['surface'])
            a = ''
            a_no = False

        if morpheme['surface'] == 'の' and 'pos' in pre_morpheme and pre_morpheme['pos'] == '名詞':
            a = pre_morpheme['surface']
            a_no = True

        pre_morpheme = morpheme

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
        result += extract_a_no_b(morphemes)
    print(result)

