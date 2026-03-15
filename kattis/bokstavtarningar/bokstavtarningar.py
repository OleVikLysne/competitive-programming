import sys; input = sys.stdin.readline

n, k, m = map(int, input().split())
dice = [input().rstrip() for _ in range(n)]
root = {}

def build_trie(node, visited):
    for i in range(n):
        if (visited >> i) & 1:
            continue
        new_visited = visited | (1 << i)
        for char in dice[i]:
            next_node = node.setdefault(char, {})
            build_trie(next_node, new_visited)


build_trie(root, 0)
s = 0
for _ in range(m):
    word = input().rstrip()
    current = root
    for char in word:
        if (current := current.get(char)) is None:
            break
    else:
        s += 1
print(s)