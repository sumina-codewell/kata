def solution(cards):
    answer=0
    visited=[0 for i in range(len(cards))]
    saveCount=[]
    
    for idx, nowCard in enumerate(cards):
        if visited[idx] == 0:
            groupCount = 1
            visited[idx] = 1
            nextIdx = nowCard-1
            
            while True:
                if visited[nextIdx] == 0:
                    groupCount += 1
                    visited[nextIdx] = 1
                    nextIdx = cards[nextIdx]-1
                else:
                    break
                
            saveCount.append(groupCount)    
    saveCount.sort(reverse=True)
        
    if len(saveCount) >1:
        answer = saveCount[0] * saveCount[1]
    else:
        answer = 0
            
    return answer