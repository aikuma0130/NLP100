expected = 'パタトクカシーー'

word_patoka = 'パトカー'
word_takushi = 'タクシー'

result = ''
for w1,w2 in zip(word_patoka, word_takushi):
    result += w1 + w2

print(result)
try:
    assert result == expected
    print('OK')
except:
    print('NG')
