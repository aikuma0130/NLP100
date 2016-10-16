
def ngram(n, sentence, mode='char'):
    def char_ngram(n, sentence):
        result = []
        word = ''
        for i, c in enumerate(sentence.replace(' ', '')):
            i += 1
            word = word + c
            if i % n == 0:
                result.append(word)
                word = ''
        if word != '':
            result.append(word)
        return result

    def word_ngram(n, sentence):
        words = sentence.split(' ')
        word = []
        result = []
        for i, w in enumerate(words):
            word.append(w.rstrip('.,'))
            i += 1
            if i % n == 0:
                result.append(word)
                word = []
        if len(word) != 0:
            result.append(word)
        return result

    if mode == 'char':
        return char_ngram(n, sentence)
    elif mode == 'word':
        return word_ngram(n, sentence)

sentence = "I am an NLPer"

print(ngram(2, sentence=sentence, mode='char'))
print(ngram(2, sentence=sentence, mode='word'))
