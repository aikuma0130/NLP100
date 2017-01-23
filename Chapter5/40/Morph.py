class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

import re
import xml.etree.ElementTree as ET
if __name__ == '__main__':
    
    with open('../neko.txt.cabocha') as f:
        xml = f.read()
    analyzed_xml = re.findall('(<sentence>.+?</sentence>)', xml, flags=re.DOTALL) 
    result = []
    for s in analyzed_xml:
        sentence = []
        root = ET.fromstring(s)
        for chunk in root:
            for tok in chunk:
                surface = tok.text
                base = tok.attrib['feature'].split(',')[6]
                pos = tok.attrib['feature'].split(',')[0]
                pos1 = tok.attrib['feature'].split(',')[1]
                sentence.append(Morph(surface=surface, base=base, pos=pos, pos1=pos1))
        result.append(sentence)

    print( [ sentence.surface  for sentence in result[2] ] )
