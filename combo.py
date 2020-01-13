def cn2(n):
    i = 0
    j = 1
    while i < n:
        yield i, j

        if j < n:
            j += 1
            continue

        i += 1
        j = i + 1
