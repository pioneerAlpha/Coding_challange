def rec(st, end):
    st+=1
    if st==end:
        print(str(st), end=' ')
        return
    print(str(st), end=' ')
    rec(st, end)
    print(str(st), end=' ')
n = int(input())
rec(0, n)
