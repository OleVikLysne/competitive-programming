from sys import stdin, stdout
B = 10**18+7 # largest prime less than 2**32
A = 31 # cool prime number
n = int(stdin.readline())
lengths = set()
hashes = {}
trie_root = {}


def rolling_hash(string):
    k = len(string)-1
    hashed_str = sum(s * pow(A, k-i, B) for i, s in enumerate(string)) % B
    return hashed_str


def hash_typos(string, hashed_str):
    k = len(string)-1
    typo_hash = ( hashed_str - string[0] * pow(A, k, B) ) % B
    yield typo_hash
    for i in range(1, len(string)):
        typo_hash -= (string[i] * pow(A, k-i, B)) % B
        typo_hash += (string[i-1] * pow(A, k-i, B)) % B
        typo_hash %= B
        yield typo_hash


def add_to_trie(root, word):
    current = root
    for char in word:
        if char not in current:
            current[char] = {}
        current = current[char]
    current["*"] = True


def find_typo(root, word, i):
    current = root
    for j in range(i):
        char = word[j]
        if char not in current:
            return False
        current = current[char]
    
    for j in range(i+1, len(word)):
        char = word[j]
        if char not in current:
            return False
        current = current[char]
    
    return "*" in current


for _ in range(n):
    string = tuple(ord(x) for x in stdin.readline().strip())
    h = rolling_hash(string)
    hashes[h] = string
    add_to_trie(trie_root, string)
    lengths.add(len(string))



found = False
for string_hash, string in hashes.items():
    if len(string)-1 not in lengths:
        continue
    for i, typo_hash in enumerate(hash_typos(string, string_hash)):
        if typo_hash in hashes and find_typo(trie_root, string, i):
            for char in string:
                stdout.write(chr(char))
            stdout.write("\n")
            found = True
            break
if not found:
    stdout.write("NO TYPOS")