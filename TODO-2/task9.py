import pytest


def Add(a):
    sum = 0
    cur = 0
    negative = 0
    negatives = ""
    delimiter = ""
    delimiters = set()
    i = -1
    for j in range (3, len(a)):
        if a[j] == '\n':
            i = j + 1
            break
        if a[j] == ']':
            delimiters.add(delimiter)
            delimiter = ""
        elif a[j] != '[':
            delimiter += a[j]
    while i < len(a):
        size_delimiter = 0
        for d in delimiters:
            if i + len(d) < len(a) and a[i:i+len(d)] == d:
                size_delimiter = len(d)
        if a[i] == '\n' or size_delimiter != 0:
            if a[i] != '\n':
                i += size_delimiter - 1
            if cur <= 1000:
                if negative:
                    sum -= cur
                    negatives += f"{-cur} "
                else:
                    sum += cur
            cur = 0
            negative = 0
        elif a[i] == ' ':
            pass
        elif a[i] == '-':
            negative = 1
        else:
            cur = cur * 10 + int(a[i])
        i += 1
    if cur <= 1000:
        if negative == 1:
            negatives += f"{-cur}"
            sum -= cur
        else :
            sum += cur
    if len(negatives) != 0:
        with pytest.raises(ValueError):
            raise ValueError(f"No negatives are allowed {negatives}")
    return sum