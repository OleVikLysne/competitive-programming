import sys; input=sys.stdin.readline

c, a = map(int, input().split())
A = map(int, input().split())
arr = [0]*(c+2)
arr[-1] = 10**9+1

def binary_search(val):
    lower, upper = 0, c+2
    while lower + 1 < upper:
        mid = (lower+upper)//2
        if arr[mid] == 0:
            print(f"Q {mid}", flush=True)
            arr[mid] = int(input())

        if arr[mid] == val:
            return mid
        if arr[mid] > val:
            upper = mid
        else:
            lower = mid
    return lower

print("A", *(binary_search(x) for x in A))