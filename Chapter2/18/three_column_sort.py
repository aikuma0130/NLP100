
def three_column_sort(filename):
    with open(filename) as f:
        sentence = f.read()

    return "\n".join([ "\t".join(row) for row in sorted([ [ row for row in line.split('\t') ] for line in sentence.split('\n')[:-1] ], key=lambda rows: float(rows[2]))])
    #sentence = [ [ row for row in line.split('\t') ] for line in sentence.split('\n')[:-1] ]
    #print(sentence)

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    print(three_column_sort(filename))
