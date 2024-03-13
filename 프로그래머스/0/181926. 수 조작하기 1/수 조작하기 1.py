def solution(n, control):
    via = []
    for i in control:
        if i =='w':
            via.append(+1)
        elif i =='s':
            via.append(-1)
        elif i =='d':
            via.append(+10)
        elif i =='a':
            via.append(-10)
    final=0
    for i in via:
        final += i
    return n+final