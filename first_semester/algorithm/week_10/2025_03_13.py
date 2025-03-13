# 2개 이상을 포함하는 경우를 구하는 함수수
def get_sub(tar):
    global cnt
    friends = []
    for i in range(n):
        if tar & 0x1:
            friends.append(arr[i])
        tar >>= 1
    if len(friends) >= 2:
        cnt += 1

arr = ['A', 'B', 'C', 'D', 'E']
n = len(arr)
cnt = 0

for target in range(1 << n):
    get_sub(target)

print(cnt)


# def get_count(tar):
#     cnt = 0
#     for i in range(n):
#         if tar & 0x1:
#             cnt += 1
#         tar >>= 1
#     return cnt


def get_count(tar):
    cnt = 0
    for i in range(n):
        if (tar >> i) & 0x1:
            cnt += 1
    return cnt


answer = 0

for target in range(1 << n):
    if get_count(target) >= 2:
        answer += 1

print(answer)


# 5 명 중 3 명(level과 관련) 뽑는 문제
n = 3
path = []

# 중복 순열
def recur(cnt):
    # n 명을 뽑으면 끝
    if cnt == n:
        print(*path)
        return
    
    # 5 명을 고려해야함
    for i in range(len(arr)):
        path.append(arr[i])
        recur(cnt + 1)
        path.pop()

recur(0)


print("---------------------------------------------------------")
n = 3
path = []

# 조합
def recur(cnt, start):
    # n 명을 뽑으면 끝
    if cnt == n:
        print(*path)
        return
    
    # 5 명을 고려해야함
    # for i in range(이전에 뽑았던 인덱스 + 1, len(arr)):
    # start: 이전 재귀로부터 넘겨 받아야 하는 값
    for i in range(start, len(arr)):
        path.append(arr[i])
        # 다음 재귀부터는 i + 1부터 고려
        recur(cnt + 1, i + 1)
        path.pop()

visited = [0] * (len(arr) + 1)
recur(0, 0)

print("주사위 문제_____________________________________________")

dice = [1, 2, 3, 4, 5, 6]
n = 3
path = []
def return_product(cnt, start):
    if cnt == n:
        print(path)
        return
    for i in range(start, len(dice)):
        path.append(dice[i])
        return_product(cnt + 1, i)
        path.pop()

return_product(0, 0)