def capital_indexes(param):
    a = []
    length = len(param)
    i = 0
    for x in param:
        if x.isupper():
            a.append(i)
            i = i+1
        else:
            i = i+1
    return a
