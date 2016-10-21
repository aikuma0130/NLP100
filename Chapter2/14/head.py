
def head(filepath, num):
    with open(filepath) as f:
        sentence = f.read()

    result = []
    for index, line in enumerate(sentence.split('\n')):
        if index == num:
            break
        result.append(line)

    return "\n".join(result) + '\n'


if __name__ == '__main__':
    import sys
    print(head('../hightemp.txt', int(sys.argv[1])), end='')
