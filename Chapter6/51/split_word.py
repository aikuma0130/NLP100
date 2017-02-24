import re

class Sentence():
    def __init__(self, sentence):
        self.lines = re.sub('([.;:?!]) ([A-Z])', "\g<1>\n\g<2>", sentence.replace('\n', '')).split('\n')

if __name__ == '__main__':
    with open('../nlp.txt', 'r') as f:
        strings = f.read()
    sentence = Sentence(strings)
    for line in sentence.lines:
        for word in line.split(' '):
            print(word)
        print()

