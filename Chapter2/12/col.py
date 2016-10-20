
def col(sentence, row):
    result = []
    for line in sentence.split('\n')[:-1]:
        l = []
        for col in line.split('\t'):
            l.append(col)
        result.append(l)

    return "\n".join([ line[row-1] for line in result ]) + "\n"

if __name__ == '__main__':
    with open('../hightemp.txt') as f:
        sentence = f.read()
        with open('./col1.txt', '+w') as col1:
            col1.write(col(sentence, 1))
        with open('./col2.txt', '+w') as col2:
            col2.write(col(sentence, 2))
