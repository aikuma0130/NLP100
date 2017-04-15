import sys

def main():
    with open('../rt-polaritydata/rt-polarity.pos', 'r') as f:
            positive_sentences = f.read()

if __name__ == '__main__':
    main()
