def solution(todo_list, finished):
    alist = list(zip(todo_list, finished))
    answer = []
    for i in alist:
        if False in i:
            answer.append(i)
        else:
            continue
    return list(map(lambda x: x[0], answer))
    