import pytest


def Add(a):
    sum = 0
    cur = 0
    negative = 0
    negatives = ""
    delimiter = set()
    i = -1
    for j in range(3, len(a)):
        if a[j] == '\n':
            i = j + 1
            break
        elif a[j] != '[' and a[j] != ']':
            delimiter.add(a[j])
    while i < len(a):
        if a[i] in delimiter or a[i] == '\n':
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