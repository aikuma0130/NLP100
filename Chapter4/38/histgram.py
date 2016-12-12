import MeCab
import sys
import numpy as np
import matplotlib.pyplot as plt

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

def word_count(lines):
    wc = {}
    for morphemes in lines:
        for morpheme in morphemes:
            if morpheme['surface'] == '':
                continue
            elif morpheme['surface'] in wc:
                wc[morpheme['surface']] += 1
            else:
                wc[morpheme['surface']] = 1

    return sorted(wc.items(),key=lambda x: x[1],reverse=True)

if __name__ == '__main__':
    lines = read_mecab_file('../neko.txt')
    word_count_list = word_count(lines)

    data = []
    for info in word_count_list:
        data.append(info[1])

    plt.hist(np.array(data), range=(20,130))
    plt.show()
