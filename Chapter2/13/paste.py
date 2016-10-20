
def paste(file1,file2):
    with open(file1) as f:
        f1 = f.read()
    with open(file2) as f:
        f2 = f.read()

    result = []
    for l1, l2 in zip(f1.split('\n')[:-1], f2.split('\n')[:-1]):
        result.append(l1 + '\t' + l2)

    return '\n'.join(result) + '\n'

if __name__ == '__main__':
    col1 = '../12/col1.txt'
    col2 = '../12/col2.txt'
    print(paste(col1, col2), end='')
