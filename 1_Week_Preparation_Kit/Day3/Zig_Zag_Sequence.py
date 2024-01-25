def findZigZagSequence(a, n):
    a.sort()
    # mid = int((n + 1)/2) # bug
    mid = int((n)/2) # fix
    a[mid], a[n-1] = a[n-1], a[mid] # swap(a[mid], a[-1])

    st = mid + 1
    # ed = n - 1 # bug
    ed = n - 1 - 1 # fix
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        # ed = ed - 1 # bug
        ed = ed - 1 # fix

    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

# test_cases = int(input())
test_cases = 1
for cs in range (test_cases):
    # n = int(input())
    n = 7
    # a = list(map(int, input().split()))
    a = [1, 2, 3, 4, 5, 6, 7]
    findZigZagSequence(a, n)

'''
test case0
>>1
>>7
>>1 2 3 4 5 6 7
1 2 3 7 6 5 4
'''
