def solution(num_list):
    sa=1
    ba=0  
    if len(num_list)<=10:
        for i in num_list:
            sa *= i
        return sa
    else:
        for i in num_list:
            ba += i
        return ba
            