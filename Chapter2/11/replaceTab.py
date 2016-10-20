
def replaceTab(sentence):
    result = []
    for c in sentence:
        if c == '\t':
            result.append(' ')
        else:
            result.append(c)

    return "".join(result)

if __name__ == '__main__':
    sentence = 'This	is		a			pen.'
    expect = 'This is  a   pen.'
    actual = replaceTab(sentence)
    print(sentence)
    print(actual)
    assert expect == actual
