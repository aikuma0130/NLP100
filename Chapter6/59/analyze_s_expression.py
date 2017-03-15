import corenlp
import json
import re
from stemming.porter2 import stem
import sys
import pydot

class Sentence():
    def __init__(self, sentence):
        self.lines = re.sub('([.;:?!]) ([A-Z])', "\g<1>\n\g<2>", sentence.replace('\n', ' ')).split('\n')
        self.words = self._get_words()

    def _get_words(self):
        words = []
        for line in self.lines:
            for word in line.split(' '):
                words.append(word.rstrip('.,'))
            words.append('')
        return words

class SExpression():

    @staticmethod
    def parse_np(raw_s_expr, recursive=True):
        match = re.search('\(NP ', raw_s_expr)
        if not match:
            return
        parenthesis_count = 0
        attribute = word = ''
        words = []
        attr = False
        #print(raw_s_expr)
        #print(match.start())
        np_s_expr = raw_s_expr[match.start()+4:]
        #print(np_s_expr)
        for char_i, char in enumerate(np_s_expr):
            if char == '(':
                parenthesis_count += 1
                attr = True
                continue
            elif char == ')':
                parenthesis_count -= 1
                if parenthesis_count == -1:
                    index = char_i + 1
                    break
                else:
                    words.append(word)
                    attribute = word = ''
                    continue
            elif char == ' ':
                attr = False
                if attribute == 'NP':
                    #print('attribute : ' + attribute)
                    SExpression.parse_np(np_s_expr[char_i-3:], recursive=False)
                continue
            else:
                if attr:
                    attribute += char
                else:
                    word += char
        print(" ".join(words))
        if index != len(np_s_expr) and recursive:
            SExpression.parse_np(np_s_expr[index:])

if __name__ == '__main__':
    with open('../nlp.txt', 'r') as f:
        strings = f.read()
    sentence = Sentence(strings)

    parser = corenlp.StanfordCoreNLP(corenlp_path='/usr/local/lib/stanford-corenlp/', memory="3g")
    #parse_result = parser.raw_parse('Bills on ports and immigration were submitted by Senator Brownback, Republican of Kansas.')
    #s_expression = SExpression.parse(parse_result['sentences'][0]['parsetree'])
    for line in sentence.lines:
        #print(line)
        parse_result = parser.raw_parse(line)
        words = parse_result['sentences'][0]['words']
        dependencies = parse_result['sentences'][0]['dependencies']
        print(parse_result['sentences'][0]['parsetree'])
        print('')
        SExpression.parse_np(parse_result['sentences'][0]['parsetree'])
        #np_list = SExpression.parse_np(parse_result['sentences'][0]['parsetree'])

        #print(json.dumps(s_expression, indent=4))
        sys.exit()

        pred_candidate = {}
        for word, info in words:
            pred_candidate[word] = {
                            "subj": "",
                            "obj": ""
                           }

        for dependency, src_word, dst_word in dependencies:
            if re.match('nsubj', dependency):
                pred_candidate[src_word]["subj"] = dst_word
            elif re.match('dobj', dependency):
                pred_candidate[src_word]["obj"] = dst_word

        for pred, part_of_speech in pred_candidate.items():
            if part_of_speech["subj"] != "" and part_of_speech["obj"] != "":
                print(part_of_speech["subj"] + "\t" + pred + "\t" + part_of_speech['obj'])
