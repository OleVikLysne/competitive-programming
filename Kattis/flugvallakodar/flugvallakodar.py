import sys; input=sys.stdin.readline; print=sys.stdout.write

primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]

class Node:
    def __init__(self):
        self.mask = 1
        self.children = [None]*26

def search(i, node: Node, depth, name, mask, char_occ):
    if depth == 2:
        if node.mask % mask == 0:
            return None
    if depth == 3:
        return []
    visited = [False]*26
    for j in range(i, len(name)):
        char = name[j]
        char_occ[char] -= 1
        if visited[char]:
            continue
        visited[char] = True
        if char_occ[char] == 0 and mask % primes[char] == 0:
            mask //= primes[char]
        if (next_node := node.children[char]) is not None:
            if depth == 2:
                continue
            if (res := search(j+1, next_node, depth+1, name, mask, char_occ)) is not None:
                res.append(char)
                return res
        else:
            if depth == 2:
                node.children[char] = True
                node.mask *= primes[char]
                return [char]
            next_node = Node()
            node.children[char] = next_node
            res =  search(j+1, next_node, depth+1, name, mask, char_occ)
            if res is not None:
                node.mask *= primes[char]
                res.append(char)
                return res
    return None

root = Node()
n = int(input())
for _ in range(n):
    inp = input()
    mask = 1
    name = []
    char_occ = [0]*26
    for i in range(len(inp)-1):
        char = ord(inp[i]) - 65
        if char > 26:
            char -= 32
        if mask % primes[char] != 0:
            mask *= primes[char]
        char_occ[char] += 1
        name.append(char)

    res = search(0, root, 0, name, mask, char_occ)
    if res is None:
        print(":( ")
    else:
        print(f"{''.join(chr(res[i]+65) for i in range(len(res)-1, -1, -1))} ")
