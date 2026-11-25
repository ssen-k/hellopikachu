def solution(n, computers):
    answer = 0
    
    visit = [False] * n
    result = []
    
    def bfs(start):
        que = [start]
        each = 0
        visit[start] = True
        while que:
            now = que.pop()
            for i in range(n):
                if computers[now][i] == 1 and visit[i] == False:
                    visit[i] = True
                    que.append(i)
                    
    
    for j in range(n):
        if visit[j] == False:
            result.append(bfs(j))
            answer += 1
        
        
    return answer