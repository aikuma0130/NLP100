def unionSet(a,b):
    result = set()
    for w in a:
        result.add(w)
    for w in b:
        result.add(w)

    return list(result)

def productSet(a,b):
    result = []
    for w in a:
        if w in b:
            result.append(w)

    return result

def differenceSet(a,b):
    product = productSet(a,b)
    result = []
    for w in a:
        if w not in product:
            result.append(w)

    return result

if __name__ == '__main__':
    from ngram import ngram
    sentence1 = "paraparaparadise"
    sentence2 = "paragraph"
    
    X = ngram(2, sentence=sentence1, mode='char')
    Y = ngram(2, sentence=sentence2, mode='char')
    
    union = unionSet(X, Y)
    product = productSet(X, Y)
    difference1 = differenceSet(X, Y)
    difference2 = differenceSet(Y, X)
    
    print("unionSet is {0}".format(union))
    print("productSet is {0}".format(product))
    print("differenceSet X-Y is {0}".format(difference1))
    print("differenceSet Y-X is {0}".format(difference2))

    print("'se' is in X : {0}".format(str('se' in X)))
    print("'se' is in Y : {0}".format(str('se' in Y)))
