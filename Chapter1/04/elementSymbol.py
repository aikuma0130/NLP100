sentence = 'Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.'

words = [ w.rstrip('.,') for w in sentence.split(' ') ]

result = {}
for i, w in enumerate(words):
    if i+1 in [1,5,6,7,8,9,15,16,19]:
        result[w[0]] = i+1
    else:
        result[w[0:2]] = i+1

print(result)
