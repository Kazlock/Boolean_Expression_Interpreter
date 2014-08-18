def del_duplicates(xs):
    seen = []
    for i, x in enumerate(xs):
        if x in seen:del(xs[i])
        else: seen.append(x)
