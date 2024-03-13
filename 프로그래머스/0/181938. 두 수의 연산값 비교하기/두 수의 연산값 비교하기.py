def solution(a, b):
    if int(str(a)+str(b)) < 2*a*b:
        return 2*a*b
    else:
        return int(str(a)+str(b))