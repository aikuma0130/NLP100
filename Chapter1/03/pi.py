sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
words = [ len(w.rstrip(',.')) for w in sentence.split(' ')]

print(words)
