input_data = input()
size =len(input_data)

stack = [0] * size

ans = 1
if input_data[0] == ')':
    ans = 0
else:
    top = -1

    for data in input_data:
        if data == '(':
            top += 1
            stack[top] = data
        elif data == ')':
            if top == -1:
                ans = 0
                break
            else:
                top -= 1
                # stack.pop(top) - 여는 소괄호만 있으므로 비교 작업 생략

    # 여는 괄호가 남아있으면
    if top > -1:
        ans = 0


print(ans)
