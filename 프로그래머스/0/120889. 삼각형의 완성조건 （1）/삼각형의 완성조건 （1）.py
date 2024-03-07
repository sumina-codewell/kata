def solution(sides):
    t = sorted(sides)
    if t[0]+t[1]>t[2]:
        return 1
    else:
        return 2