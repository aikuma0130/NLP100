import re
from stemming.porter2 import stem

class Sentence():
    def __init__(self, sentence):
        self.lines = re.sub('([.;:?!]) ([A-Z])', "\g<1>\n\g<2>", sentence.replace('\n', '')).split('\n')
        self.words = self._get_words()

    def _get_words(self):
        words = []
        for line in self.lines:
            for word in line.split(' '):
                words.append(word.rstrip('.,'))
            words.append('')
        return words

if __name__ == '__main__':
    with open('../nlp.txt', 'r') as f:
        strings = f.read()
    sentence = Sentence(strings)
    for word in sentence.words:
        print("{0}\t{1}".format(word, stem(word)))

