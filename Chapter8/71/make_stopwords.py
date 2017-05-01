import sys

def main():
    word_count = {}
    with open('../sentiment.txt') as f:
        for line in f:
            for word in line[3:].split(' '):
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    percent = 0.05
    end = int(len(sorted_word_count) * percent)
    word_sum = sum([ word_count[1] for word_count in sorted_word_count ])
    stop_words = []
    sorted_word_count.reverse()
    for index, word_count in enumerate(sorted_word_count):
        #if index == 2000:
        #    break
        if word_count[1] == 1 or word_count[1] >= 500:
            continue
        stop_words.append(word_count[0])
        #per = word_count[1] * 100 / word_sum
        #print(word_count[0] + ": " + str(per) + "%, " + str(word_count[1]))

    with open('../stopwords.txt', 'w') as f:
        for word in stop_words:
            f.write(word + '\n')

if __name__ == '__main__':
    main()
