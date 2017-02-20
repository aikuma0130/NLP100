import sys
import re
import xml.etree.ElementTree as ET
import pydot
import copy

class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk():
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.surfaces = "".join([ morph.surface for morph in morphs if morph.surface not in ['、','。']])
        self.dst = dst
        self.srcs = srcs
        self.is_visit = False
        self.cases = [ morph.surface for morph in morphs if morph.pos == '助詞' ]
        self.verbs = [ morph.base for morph in morphs if morph.pos == '動詞']

    def get_morph_index(self, pos, pos1):
        for index, morph in enumerate(self.morphs):
            if morph.pos == pos and morph.pos1 == pos1:
                return index
        return -1

    def has_pos(self, pos, pos1=None):
        for morph in self.morphs:
            if morph.pos == pos:
                if pos1 is None:
                    return True
                elif morph.pos1 == pos1:
                    return True
        return False

    @staticmethod
    def print_diagraph(name, sentence):
        graph = pydot.Dot(name)
        for chunk in sentence:
            if chunk.is_visit == True:
                continue
            chunk.is_visit = True
            node = pydot.Node(chunk.surfaces)
            graph.add_node(node)
            if chunk.dst != -1:
                graph.add_edge(pydot.Edge(chunk.surfaces, sentence[chunk.dst].surfaces))
        print(graph.to_string())
        graph.write_jpeg('graph_neko.jpg', prog='dot')

    @staticmethod
    def fromstring(cabocha_xml):
        analyzed_xml = re.findall('(<sentence>.+?</sentence>)', cabocha_xml, flags=re.DOTALL) 
        result = []
        for sentence in analyzed_xml:
            root = ET.fromstring(sentence)
            chunks = []
            dependencies = {}
            for chunk in root:
                src = int(chunk.attrib['id'])
                dst = int(chunk.attrib['link'])
                dependencies[src] = dst
                srcs = [ k for k, v in dependencies.items() if v == src ]
                morphs = []
                for tok in chunk:
                    surface = tok.text
                    base = tok.attrib['feature'].split(',')[6]
                    pos = tok.attrib['feature'].split(',')[0]
                    pos1 = tok.attrib['feature'].split(',')[1]
                    morphs.append(Morph(surface=surface, base=base, pos=pos, pos1=pos1))
                chunks.append(Chunk(morphs, dst, srcs))
            result.append(chunks)
        return result

    @staticmethod
    def get_chunks_until_root(sentence, index):
        chunks = [ sentence[index], ]
        dst = sentence[index].dst
        if dst != -1:
            chunks.extend(Chunk.get_chunks_until_root(sentence, dst))
        return chunks

    @staticmethod
    def extract_noun_path(sentence):
        result = []
        for index, chunk in enumerate(sentence):
            if not chunk.has_pos('名詞'):
                continue
            chunks_until_root = Chunk.get_chunks_until_root(sentence, index)
            if len(chunks_until_root) >= 2:
                result.append(chunks_until_root)
        return result

if __name__ == '__main__':
    
    with open('../neko.txt.cabocha') as f:
        cabocha_xml = f.read()
    sentences = Chunk.fromstring(cabocha_xml)
    #print([ chunk.surfaces for chunk in sentences[7]])
    #Chunk.extract_noun_path(sentences[7])
    for sentence in sentences:
        for noun_paths in Chunk.extract_noun_path(sentence):
            print(" -> ".join([ chunk.surfaces for chunk in noun_paths]))
