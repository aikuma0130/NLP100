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
    #parse_result = parser.raw_parse('Bills on ports and immigration were submitted by Senator Brownback, Republican of Kansas.')
    for line in sentence.lines:
        parse_result = parser.raw_parse(line)
        words = parse_result['sentences'][0]['words']
        indexeddependencies = parse_result['sentences'][0]['indexeddependencies']

        graph = pydot.Dot('test')
        for word, info in words:
            if word in '.,':
                continue
            node = pydot.Node(word)
            graph.add_node(node)

        for dependency, src, dst in indexeddependencies:
            src_word = src.split('-')[0]
            src_index = int(src.split('-')[1]) - 1
            dst_word = dst.split('-')[0]
            dst_index = int(dst.split('-')[1]) - 1

            if re.match('conj_', dependency):
                preposition = dependency.split('_')[1]
                graph.add_edge(pydot.Edge(src_word, preposition))
                graph.add_edge(pydot.Edge(src_word, dst_word))
            elif re.match('prep_', dependency):
                preposition = dependency.split('_')[1]
                graph.add_edge(pydot.Edge(src_word, preposition))
                graph.add_edge(pydot.Edge(preposition, dst_word))
            elif re.match('agent', dependency):
                preposition = 'by'
                graph.add_edge(pydot.Edge(src_word, preposition))
                graph.add_edge(pydot.Edge(preposition, dst_word))
            else:
                graph.add_edge(pydot.Edge(src_word, dst_word))

        print(graph.to_string())
        graph.write_jpeg('graph_nlp.jpg', prog='dot')
        sys.exit()
    #print(json.dumps(parse_result, indent=4))
    #for line in sentence.lines:
    #    json_data = parser.raw_parse(line)
    #    print(json.dumps(json_data, indent=4))
    #    sys.exit()
        #for word, info in json_data["sentences"][0]['words']:
        #    print(word)
                #print("{0}\t{1}\t{2}".format(word, info['Lemma'], info['PartOfSpeech']))
