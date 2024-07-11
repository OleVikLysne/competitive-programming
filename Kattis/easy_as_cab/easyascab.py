import sys
import string
AMBIG = "AMBIGUOUS"
IMPOS = "IMPOSSIBLE"
def f():
    line_0 = sys.stdin.__next__().split(" ")
    unique_chars, num_lines = line_0[0], int(line_0[1])
    unique_chars = string.ascii_lowercase.index(unique_chars)+1
    word_list = [sys.stdin.__next__().replace("\n", "") for _ in  range(num_lines)]
    data = {}

    if len(word_list) == 1:
        if len(set(word_list[0])) == 1:
            print(word_list[0][0])
        else:
            print(AMBIG)
        return

    for word in word_list:
        for char in word:
            data[char] = ("", "") #in_nodes first, out_nodes second

    for j in range(1, len(word_list)):
        i = j-1
        prev_word, cur_word = word_list[i], word_list[j]
        for k, prev_char in enumerate(prev_word):
            if k >= len(cur_word):
                print(IMPOS)
                return
            cur_char = cur_word[k]
            if cur_char == prev_char: #no information gained
                continue
            data[prev_char] = (data[prev_char][0], data[prev_char][1] + cur_char)
            data[cur_char] = (data[cur_char][0] + prev_char, data[cur_char][1])
            break

    if cycle(data):
        print(IMPOS)
        return

    res = verify_path_length(data, unique_chars)
    if isinstance(res, str):
        print(res)
    else:
        print(AMBIG)


def path_helper(data: dict, node: str, visited: set, stack):
    visited.add(node)
    _, out_nodes = data[node]
    for neighbour in out_nodes:
        if neighbour not in visited:
            stack = path_helper(data, neighbour, visited, stack)

    stack += node
    return stack

def verify_path_length(data: dict, unique_chars):
    #find some root with in_degree 0 (doesnt matter if there are multiple)
    root = None
    for vertex, (in_nodes, _) in data.items():
        if len(in_nodes)==0:
            root = vertex
            break
    visited = set()
    stack = ""
    for vertex in data.keys():
        if vertex not in visited:
            stack = path_helper(data, vertex, visited, stack)
    
    paths = {vertex : "" if vertex != root else root for vertex in data.keys()}
    for char in reversed(stack):
        if len(paths[char]) != 0:
            _, out_nodes = data[char]
            for neighbour in out_nodes:
                if len(paths[neighbour]) <= len(paths[char]):
                    paths[neighbour] = paths[char] + neighbour
                    if len(paths[neighbour]) == unique_chars:
                        return paths[neighbour]

    return False



def cycle_helper(data: dict, node: str, visited: set, rec_stack: set):
    visited.add(node)
    rec_stack.add(node)
    _, out_nodes = data[node]
    for neighbour in out_nodes:
        if neighbour not in visited:
            if cycle_helper(data, neighbour, visited, rec_stack):
                return True
        elif neighbour in rec_stack:
            return True
    rec_stack.remove(node)
    return False


def cycle(data: dict):
    visited = set()
    rec_stack = set()
    for node in data.keys():
        if node not in visited:
            if cycle_helper(data, node, visited, rec_stack):
                return True
    return False

f()