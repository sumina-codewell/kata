def solution(my_string):
    a=['a','e','i','o','u']
    b= list(my_string)
    for i in a:
        while i in b:
            b.remove(i)
    return ''.join(b)