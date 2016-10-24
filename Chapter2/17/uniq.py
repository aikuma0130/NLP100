
def uniq(filename):
    with open(filename) as f:
        sentence = f.read()

    result = set()
    for r in [ [ row for row in line.split('\t') ] for line in sentence.split('\n')[:-1] ]:
        result.add(r[0])

    result = list(result)
    result.sort()
    return "\n".join(result)

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    print(uniq(filename))
