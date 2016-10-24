
def three_column_sort(filename):
    with open(filename) as f:
        sentence = f.read()

    return "\n".join([ "\t".join(column) for column in sorted([ [ column for column in line.split('\t') ] for line in sentence.split('\n')[:-1] ], key=lambda columns: float(columns[2]))])

if __name__ == '__main__':
    import sys
    filename = sys.argv[1]
    print(three_column_sort(filename))
