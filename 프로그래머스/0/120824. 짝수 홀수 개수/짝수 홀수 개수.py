def solution(num_list):
    i = []
    e=0
    o=0
    for i in num_list:
        if i%2==0:
            e += 1
        else: o += 1
    i = [e,o]
    return i