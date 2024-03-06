def solution(money):
    answer = []
    aa=money//5500
    rest_money=money-(aa*5500)
    answer += [aa,rest_money]
    return answer