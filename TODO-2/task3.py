def Add(a):
    sum = 0
    cur = 0
    for i in a:
        if i == ',' or i == '\n':
            sum += cur
            cur = 0
        elif i == ' ':
            pass
        else:
            cur = cur * 10 + int(i)
    return sum + cur