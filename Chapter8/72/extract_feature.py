from stemming.porter2 import stem
import sys
import re

sys.path.append('../71')
from stop_words import StopWord as sw


class Sentiment():
    def __init__(self):
        pass

    @staticmethod
    def extract_feature(sentence):
        feature = []
        for word in re.split('\s\s*', sentence.strip()):
            if not sw.is_stopwords(word):
                feature.append(stem(word))
        return feature

if __name__ == '__main__':
    with open('../sentiment.txt', 'r') as f:
        for line in f.readlines():
            print(Sentiment.extract_feature(line[3:]))

