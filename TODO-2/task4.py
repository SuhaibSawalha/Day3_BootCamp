def Add(a):
    sum = 0
    cur = 0
    for i in range(4, len(a)):
        if a[i] == a[2] or a[i] == '\n':
            sum += cur
            cur = 0
        elif a[i] == ' ':
            pass
        else:
            cur = cur * 10 + int(a[i])
    return sum + cur