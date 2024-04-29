def solution(arr):
    result=[]
    for i in arr:
        for t in range(i):
            result.append(i)
    return result