import sys
import random

def main():
    sentiments = []
    with open('../rt-polaritydata/rt-polarity-utf8.pos', 'r') as f:
        for data in f:
            sentiments.append('+1 ' + data)
    with open('../rt-polaritydata/rt-polarity-utf8.neg', 'r') as f:
        for data in f:
            sentiments.append('-1 ' + data)
    random.shuffle(sentiments)
    with open('../sentiment.txt', 'w') as sentiment_txt:
        sentiment_txt.writelines(sentiments)

if __name__ == '__main__':
    main()
