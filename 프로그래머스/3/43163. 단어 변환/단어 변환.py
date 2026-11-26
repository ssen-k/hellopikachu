def check(now, next):
    n = len(now)
    count = 0
    for i in range(n):
        if now[i] == next[i]:
            count += 1
    return count

def solution(begin, target, words):
    answer = 0

    if target not in words:
        return 0

    n = len(begin)

    visit = []

    que = [(begin, 0)]
    while que:
        words1, cnt = que.pop()
        if words1 == target:
            return cnt
        for x in range(len(words)):
            if words[x] not in visit and check(words1, words[x]) == n-1:
                visit.append(words[x])
                que.append((words[x], cnt + 1))

    return answer

