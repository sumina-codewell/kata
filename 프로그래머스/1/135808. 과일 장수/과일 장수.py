def solution(k, m, score):
    sorted_score = sorted(score, reverse=True)
    answer = []
    box = [sorted_score[i*m : m*(i+1)] for i in range(0, (len(sorted_score)+m-1)//m)]
    for i in box:
        if len(i) == m:
            value = min(i) * m
            answer.append(value)
    return sum(answer)