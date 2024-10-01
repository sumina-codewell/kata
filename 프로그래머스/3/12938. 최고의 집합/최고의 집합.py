def solution(n, s):
    if n > s:
        return [-1]

    answer = []

    m = s//n

    for i in range(n):
        answer.append(m)
        s -= m

    if s >= 0:
        for i in range(s):
            answer[i] += 1

    answer.sort()
    print(answer)
    return answer