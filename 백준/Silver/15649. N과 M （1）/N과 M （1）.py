import sys
input = sys.stdin.readline

n, m = map(int, input().split())
visit = [False] * (n+1)
result = []

def tracking(num):
    if num == m:
        print(' '.join(map(str, result)))
        return m
    for i in range(1, n+1):
        if visit[i] == False:
            visit[i] = True
            result.append(i)
            tracking(num+1)
            visit[i] = False
            result.pop()


tracking(0)


# 1부터 n까지 for
# visit = False라면 저장하고 다시 tracking 수열의 길이가 m이 되면 리턴