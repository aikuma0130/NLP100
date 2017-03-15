import corenlp
import json
import re
from stemming.porter2 import stem
import sys
import pydot

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
    parse_result = parser.raw_parse('Bills on ports and immigration were submitted by Senator Brownback, Republican of Kansas.')
    print(json.dumps(parse_result, indent=4))
    sys.exit()
    #for line in sentence.lines:
    #    parse_result = parser.raw_parse(line)
    #    words = parse_result['sentences'][0]['words']
    #    dependencies = parse_result['sentences'][0]['dependencies']

    #    pred_candidate = {}
    #    for word, info in words:
    #        pred_candidate[word] = {
    #                        "subj": "",
    #                        "obj": ""
    #                       }

    #    for dependency, src_word, dst_word in dependencies:
    #        if re.match('nsubj', dependency):
    #            pred_candidate[src_word]["subj"] = dst_word
    #        elif re.match('dobj', dependency):
    #            pred_candidate[src_word]["obj"] = dst_word

    #    for pred, part_of_speech in pred_candidate.items():
    #        if part_of_speech["subj"] != "" and part_of_speech["obj"] != "":
    #            print(part_of_speech["subj"] + "\t" + pred + "\t" + part_of_speech['obj'])
