import corenlp
import json
import re
from stemming.porter2 import stem
import sys

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

    parser = corenlp.StanfordCoreNLP(corenlp_path='/usr/local/lib/stanford-corenlp/', memory="3g")
    for line in sentence.lines:
        json_data = parser.raw_parse(line)
        for word, info in json_data["sentences"][0]['words']:
            print("{0}\t{1}\t{2}".format(word, info['Lemma'], info['PartOfSpeech']))

