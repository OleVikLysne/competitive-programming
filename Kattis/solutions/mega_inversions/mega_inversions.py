from copy import deepcopy

def update(tree, i, val):
    i+=n
    diff = val-tree[i]
    if diff == 0: return
    tree[i] = val
    while i>1:
        i>>=1
        tree[i]+=diff


def query(tree, l, r):
    l += n
    r += n
    if l == r:
        return tree[l]
    s = tree[l] + tree[r]
    while True:
        pl = l >> 1
        pr = r >> 1
        if pl == pr: return s
        if l % 2 == 0:
            s += tree[l+1]
        if r % 2 == 1:
            s += tree[r-1]
        l, r = pl, pr


def binary_search(arr, val, reverse=False):
    lower, upper = 0, len(arr)
    while True:
        mid = (lower+upper)//2
        if arr[mid] == val: 
            return mid
        if reverse:
            if arr[mid] < val:
                upper = mid
            else:
                lower = mid
        else:
            if arr[mid] < val:
                lower = mid
            else:
                upper = mid


n = int(input())
arr = [int(x) for x in input().split()]

offset = 0
for i in range(n):
    arr[i] = arr[i]*n + offset
    offset+=1

sorted_arr = deepcopy(arr)
sorted_arr.sort()
tree = [0]*n*2
output = [1 for _ in range(n)]
for i in range(n):
    k = binary_search(sorted_arr, arr[i])
    output[i]*=query(tree, k, n-1)
    update(tree, k, 1)
    
tree = [0]*n*2
sorted_arr.reverse()
for i in range(n-1, -1, -1):
    k = binary_search(sorted_arr, arr[i], reverse=True)
    output[i]*=query(tree, k, n-1)
    update(tree, k, 1)

print(sum(output))