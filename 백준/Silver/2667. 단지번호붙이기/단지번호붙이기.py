import sys
input = sys.stdin.readline

n = int(input())
tempMap = [list(map(int, input().strip())) for _ in range(n)]
visit = [[False] * n for _ in range(n)]

result = []
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def dfs(y, x):
    global each
    each += 1
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if 0<= ny < n and 0 <= nx < n:
            if tempMap[ny][nx] == 1 and visit[ny][nx] == False:
                visit[ny][nx] = True
                dfs(ny, nx)

for j in range(n):
    for i in range(n):
        if tempMap[j][i] == 1 and visit[j][i] == False:
            visit[j][i] = True
            each = 0
            dfs(j, i)
            result.append(each)

result.sort()
print(len(result))
for i in result:
    print(i)


#오빠 치루 재발은 안돼!!!!(청테이프 아파)