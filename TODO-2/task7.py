import pytest


def Add(a):
    sum = 0
    cur = 0
    negative = 0
    negatives = ""
    delimiter = ""
    i = -1
    for j in range (3, len(a)):
        if a[j] == ']':
            i = j + 2
            break
        delimiter += a[j]
    while i < len(a):
        if a[i] == '\n' or (i + len(delimiter) < len(a) and a[i:i+len(delimiter)] == delimiter):
            if a[i] != '\n':
                i += len(delimiter) - 1
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