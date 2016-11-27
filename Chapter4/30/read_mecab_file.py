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

if __name__ == '__main__':
    result = read_mecab_file('../neko.txt')
    print(result)

