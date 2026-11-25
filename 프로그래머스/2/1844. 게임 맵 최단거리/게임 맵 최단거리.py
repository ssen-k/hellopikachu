def solution(maps):
    answer = 0
    
    n = len(maps)
    m = len(maps[0])
    
    visit = [[0] * m for _ in range(n)]
    
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    
    que = [(0, 0)]
    visit[0][0] = 1
    
    while que:
        ey, ex = que.pop(0)
        for i in range(4):
            ny = ey + dy[i]
            nx = ex + dx[i]
            if 0 <= ny < n and 0 <= nx < m:
                if maps[ny][nx] == 1 and visit[ny][nx] == 0:
                    visit[ny][nx] = visit[ey][ex] + 1
                    que.append((ny, nx))
                    
    if visit[n-1][m-1] == 0:
        answer = -1
        return answer
    
    else:
        return visit[n-1][m-1]
                
                
