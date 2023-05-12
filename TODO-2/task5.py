import pytest


def Add(a):
    sum = 0
    cur = 0
    negative = 0
    negatives = ""
    for i in range(4, len(a)):
        if a[i] == a[2] or a[i] == '\n':
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
    if negative == 1:
        negatives += f"{-cur}"
        sum -= cur
    else :
        sum += cur
    if len(negatives) != 0:
        with pytest.raises(ValueError):
            raise ValueError(f"No negatives are allowed {negatives}")
    return sum