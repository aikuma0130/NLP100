import corenlp
import json

if __name__ == '__main__':
    parser = corenlp.StanfordCoreNLP(corenlp_path='/usr/local/lib/stanford-corenlp/', memory="1g")
    with open('../nlp.txt', 'r') as f:
        txt_data = f.read()
    json_data = parser.raw_parse(txt_data)
    print(json_data)
