from itertools import chain

def wordcount(filename, col):
    with open(filename) as f:
        sentence = f.read()

    result = {}
    for word in chain.from_iterable([ [ column for index, column in enumerate(row.split('\t')) if (index + 1) == col ] for row in sentence.split('\n')[:-1] ]):
        if word in result:
            result[word] += 1
        else:
            result[word] = 1

    return "\n".join([ " ".join(map(lambda x: str(x), column)) for column in [ list(word) for word in sorted(result.items(), key=lambda x: int(x[1]), reverse=True) ]])

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    print(wordcount(filename, 1))

