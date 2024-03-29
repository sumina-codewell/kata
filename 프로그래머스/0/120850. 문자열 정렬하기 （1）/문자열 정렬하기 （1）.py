import re
def solution(my_string):
    nums= re.findall(r'\d', my_string)
    answer = (map(int, nums))
    return sorted(list(answer))