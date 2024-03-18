def solution(rsp):
    list(rsp)
    win = str.maketrans('205','052')
    return rsp.translate(win)