def solution(my_string, is_prefix):
    if is_prefix in my_string and is_prefix[0:2]==my_string[0:2]:
        return 1
    else:
        return 0