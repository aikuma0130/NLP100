import random

def typoglycemia(sentence):
    result = []
    for word in sentence.split(' '):
        if len(word) <= 4:
            result.append(word)
        else:
            center = [ char for char in word[1:-1] ]
            random.shuffle(center)
            result.append(word[0] + "".join(center) + word[-1])
    return " ".join(result)

if __name__ == '__main__':
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    result = typoglycemia(sentence)
    print(result)
