import sys

input = sys.stdin.readline

a_occ = [0]*100
b_occ = [0]*100
a_list = []
b_list = []


def sort_swap(arr, jump_arr):
    i = len(arr)-1
    while i > 0 and arr[i-1] > arr[i]:
        j = i - jump_arr[arr[i-1]]
        arr[i], arr[j] = arr[j], arr[i]
        i = j


for n in range(1, int(input()) + 1):
    a, b = map(int, input().split())
    a_list.append(a)
    b_list.append(b)
    a_occ[a] += 1
    b_occ[b] += 1
    sort_swap(a_list, a_occ)
    sort_swap(b_list, b_occ)
    i = n-a_occ[a_list[n-1]]
    maxi = 0
    while i >= 0:
        maxi = max(maxi, a_list[i]+b_list[n-i-1])
        i -= a_occ[a_list[i-1]]
    print(maxi)
