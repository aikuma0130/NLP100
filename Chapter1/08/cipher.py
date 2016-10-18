
def chipher(word):
    encycropt = ''
    for char in word:
        if char.islower():
            encycropt += chr(219 - ord(char))
        else:
            encycropt += char

    return encycropt

if __name__ == '__main__':
    sentence = 'This is Tom.'
    print("Sentence : " + sentence)
    encycropt = chipher(sentence)
    print("Encycropt : " + encycropt)
    deencycropt = chipher(encycropt)
    print("Deencycropt : " + deencycropt)
