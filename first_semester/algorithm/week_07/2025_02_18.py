perms = []
def perm(selected, remain):
    global perms
    if not remain:
        perms.append(selected)
    else:
        for i in range(len(remain)):
            select_i = remain[i]
            remain_list = remain[:i] + remain[i + 1:]
            perm(selected + [select_i], remain_list)


perm([], [1, 2, 3, 5])
print(perms)

# 사전 순으로 생성하지 않음.
def f(i, N):
    if i == N:
        print(p)
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i] # 자리 교환
            f(i + 1, N)
            p[i], p[j] = p[j], p[i] # 원상 복구

p = [0, 1, 2]
N = 3
f(0, N)