import unittest


class StopWord(object):
    stop_words = []
    with open('../stopwords.txt') as f:
        for w in f:
            stop_words.append(w.rstrip())

    @classmethod
    def is_stopwords(cls, word):
        if word in cls.stop_words:
            return True
        else:
            return False


class TestStopWord(unittest.TestCase):

    def test_is_stopword(self):
        self.assertTrue(StopWord.is_stopwords('the'))
        self.assertFalse(StopWord.is_stopwords('hoge'))


if __name__ == '__main__':
    unittest.main()
