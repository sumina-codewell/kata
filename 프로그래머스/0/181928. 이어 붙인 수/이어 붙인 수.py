def solution(num_list):
    e_n, o_n=[],[]
    for i in num_list:
        if i%2 == 0:
            e_n.append(i)
        else:
            o_n.append(i)
    return(int(''.join(map(str,e_n)))+int(''.join(map(str,o_n))))