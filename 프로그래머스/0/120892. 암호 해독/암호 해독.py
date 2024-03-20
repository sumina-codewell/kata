def solution(cipher, code):
    q=list(cipher)
    q.insert(0,'a')
    return ''.join(q[code::code])