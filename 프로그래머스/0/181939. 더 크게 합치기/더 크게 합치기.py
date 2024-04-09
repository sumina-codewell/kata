def solution(a, b):
    str(a), str(b)
    if str(a)+str(b) > str(b)+str(a):
        return int(str(a) + str(b))
    else:
        return int(str(b) + str(a))
