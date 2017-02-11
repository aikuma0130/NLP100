import sys
sys.path.append('../40')
sys.path.append('../41')
from Morph import Morph
from Chunk import Chunk

if __name__ == '__main__':
    
    with open('../neko.txt.cabocha') as f:
        cabocha_xml = f.read()
    sentences = Chunk.fromstring(cabocha_xml)
    for sentence in sentences:
        for chunk in sentence:
            if chunk.dst == -1:
                continue
            src_text = "".join([ morph.surface for morph in chunk.morphs if morph.surface not in ['、','。']])
            for idx, chk in enumerate(sentence):
                if idx == chunk.dst:
                    dst_text = "".join([ mph.surface for mph in chk.morphs if mph.surface not in ['、','。']])
            print(src_text + "\t" + dst_text)
