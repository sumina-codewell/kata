str = input()
n_str=''
for i in str:
    if i.islower():
        j = i.upper()
        n_str += j
    else:
        k = i.lower()
        n_str += k
print(n_str)