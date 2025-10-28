# 39_stack_basics.py
# 스택 구현 (push/pop) & 시연

mystack = []

def putdata(data):
    """스택에 data를 push"""
    global mystack
    mystack.append(data)

def popdata():
    """스택에서 data를 pop (없으면 None)"""
    global mystack
    if len(mystack) == 0:
        return None
    return mystack.pop()

# 데모
putdata('데이터1')
putdata([3, 4, 5, 6])
putdata(12345)

print('<스택상태>: ', mystack)

ret = popdata()
while ret is not None:
    print('스택에서 데이터 추출:', ret)
    print('<스택상태>: ', mystack)
    ret = popdata()
