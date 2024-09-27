import sys 
sys.setrecursionlimit(10000)


def solution(maps):
    maps2 = []
    for i in maps:
        nustr = ''
        for char in i:
            if char == 'X':
                nustr += '0'
            else :
                nustr += char
        maps2.append(nustr)

    maps3 = []    
    for j in maps2:
        intlist = []
        for char in j:
            intlist += [int(char)]
        maps3.append(intlist)

    days = []
    num_list = len(maps3)      #리스트의 갯수(m):4
    for k in range(len(maps3[0])):     #리스트 내 요소의 갯수(k):5
        l = 0      #각 열의 합계 초기화
        for m in range(num_list):
            l += maps3[m][k]
        days.append(l)

    if all(maps3[i][j] == 0 for i in range(len(maps3)) for j in range(len(maps3[0]))):
        return [-1]
    else:
        def dfs(x,y,visited):
            if x < 0 or x >= len(maps3) or y < 0 or y >= len(maps3[0]):
                return 0
            if (x,y) in visited or maps3[x][y] == 0 :
                return 0 

            visited.add((x,y))
            size = maps3[x][y]

            size += dfs(x+1, y, visited)
            size += dfs(x - 1, y, visited)
            size += dfs(x, y + 1, visited)
            size += dfs(x, y-1, visited)

            return size

        result=[]
        visited= set()

        for i in range(len(maps3)):
            for j in range(len(maps3[0])):
                if (i,j) not in visited and maps3[i][j] != 0:
                    island_size = dfs(i,j,visited)
                    if island_size > 0:
                        result.append(island_size)
                        result.sort()

        return result
