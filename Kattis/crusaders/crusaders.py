import sys; input=sys.stdin.readline

c, a = map(int, input().split())
A = map(int, input().split())
arr = [0]*(c+1)
def binary_search(val):
    lower, upper = 0, c+1
    while lower+1 < upper:
        mid = (lower+upper)//2
        if arr[mid] == 0:
            print(f"Q {mid}", flush=True)
            arr[mid] = int(input())
        if arr[mid] <= val:
            lower = mid
        else:
            upper = mid
        if arr[lower] == val:
            break
    return lower

print("A", *(binary_search(x) for x in A))
