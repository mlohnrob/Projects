A = list(map(int, input().split()))
element = int(input())

def binary_search(A, element):
    
    def S(cnt):
        if cnt == 0: return True
        else: return A[cnt-1] < element

    l = 0
    r = len(A)

    while l < r:
        m = (l + r + 1) // 2
        if S(m): l = m
        else: r = m - 1

    print(l)
    return l < len(A) and A[l] == element

print(binary_search(A, element))
