from stemming.porter2 import stem
import sys
import re
import random


class NLP(object):
    stop_words = []
    with open('../stopwords.txt') as f:
        for w in f:
            stop_words.append(w.rstrip())

    @classmethod
    def is_stopword(self, word):
        if word in self.stop_words:
            return True
        else:
            return False


class SentimentTestData():
    def __init__(self, line, polarity):
        self.line = line
        self.polarity = polarity
        self.feature = []
        self._extract_feature()

    def _extract_feature(self):
        for word in re.split('\s\s*', self.line.strip()):
            if not NLP.is_stopword(word):
                self.feature.append(stem(word))


class Sentiments(object):
    def __init__(self):
        self.data = []

    def read_data(self, filename, polarity):
        with open(filename, 'r') as f:
            for data in f:
                self.data.append(SentimentTestData(data, polarity))

    def shuffle(self):
        random.shuffle(self.data)

if __name__ == '__main__':
    sentiments = Sentiments()
    sentiments.read_data('../rt-polaritydata/rt-polarity-utf8.pos', 1)
    sentiments.read_data('../rt-polaritydata/rt-polarity-utf8.neg', -1)
    sentiments.shuffle()

    print(sentiments.data[0].line)
    print(sentiments.data[0].polarity)
    print(sentiments.data[0].feature)

