import sys
sys.path.append('../40')
sys.path.append('../41')
from Morph import Morph
from Chunk import Chunk

def has_pos(chunk, pos):
    for morph in chunk.morphs:
        if morph.pos == pos:
            return True
    return False


if __name__ == '__main__':
    
    with open('../neko.txt.cabocha') as f:
        cabocha_xml = f.read()
    sentences = Chunk.fromstring(cabocha_xml)
    for sentence in sentences:
        for chunk in sentence:

            if chunk.dst == -1:
                continue

            if has_pos(chunk, '名詞'):
                src_text = "".join([ morph.surface for morph in chunk.morphs if morph.surface not in ['、','。']])
            else:
                continue

            for idx, chk in enumerate(sentence):
                if idx == chunk.dst:
                    dst_index = idx

            if has_pos(sentence[dst_index], '動詞'):
                dst_text = "".join([ mph.surface for mph in sentence[dst_index].morphs if mph.surface not in ['、','。']])
            else:
                continue

            print(src_text + "\t" + dst_text)
