import sys
import copy
N = int(sys.stdin.readline())

answer = []
def dfs(stack: list, level: int):
    global answer
    if level == N:
        answer.append(copy.deepcopy(stack))
        return

    for c in range(N):
        row, column = level, c
        flag = True
        for p_r, p_c in enumerate(stack):
            if p_c == column:
                flag = False
                break
            if abs(row-p_r) == abs(column-p_c):
                flag = False
                break

        if flag:
            stack.append(column)
            dfs(stack, level+1)
            stack.pop()
dfs([], 0)
final = []
for record in answer:
    temp = []
    for c in record:
        start = "."*c + "Q" + "."*(N-c-1)
        temp.append(start)
    final.append(temp)

print(final)