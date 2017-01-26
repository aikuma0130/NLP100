import sys
sys.path.append('../40')
from Morph import Morph
import re
import xml.etree.ElementTree as ET

class Chunk():
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

    @staticmethod
    def fromstring(cabocha_xml):
        analyzed_xml = re.findall('(<sentence>.+?</sentence>)', cabocha_xml, flags=re.DOTALL) 
        result = []
        for sentence in analyzed_xml:
            root = ET.fromstring(sentence)
            chunks = []
            dependencies = {}
            for chunk in root:
                src = chunk.attrib['id']
                dst = chunk.attrib['link']
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

if __name__ == '__main__':
    
    with open('../neko.txt.cabocha') as f:
        cabocha_xml = f.read()
    sentences = Chunk.fromstring(cabocha_xml)
    chunks = [ chunk for chunk in sentences[7] ]
    for chunk in chunks:
        chunk_text = "".join([ morph.surface for morph in chunk.morphs ])
        print(chunk_text + " : " + chunk.dst)
