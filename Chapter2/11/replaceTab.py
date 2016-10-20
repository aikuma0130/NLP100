
def replaceTab(sentence):
    result = []
    for c in sentence:
        if c == '\t':
            result.append(' ')
        else:
            result.append(c)

    return "".join(result)

if __name__ == '__main__':
    with open('../hightemp.txt') as f:
        sentence = f.read()
        print(replaceTab(sentence), end='')
