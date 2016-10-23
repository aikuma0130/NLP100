
def split(filename, n):
    N = int(n)
    with open(filename) as f:
        sentence = f.read()

    for index, line in enumerate(sentence.split('\n')[:-1]):
        if (index + 1) % N == 1:
            tf = open('xa' + str((index + 1) // N), 'w')

        tf.write(line + '\n')

        if (index + 1) % N == 0:
            tf.close()

if __name__ == '__main__':
    import sys
    filename = '../hightemp.txt'
    n = sys.argv[1]

    split(filename, n)
