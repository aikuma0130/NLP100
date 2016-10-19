
def wordcount(sentence):
    return len(sentence.split('\n')) - 1

if __name__ == '__main__':
    with open('testfile') as f:
        sentence = f.read()
        print(sentence, end='')
        print("wc -l = {0}".format(wordcount(sentence)))
