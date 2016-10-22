
def head(filepath, num):
    with open(filepath) as f:
        sentence = f.read()

    result = []
    for index, line in enumerate(sentence.split('\n')[::-1][1:]):
        if index == num:
            break
        result.append(line)

    return "\n".join(result[::-1]) + '\n'


if __name__ == '__main__':
    import sys
    print(head('../hightemp.txt', int(sys.argv[1])), end='')
