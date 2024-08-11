def kmp(text, pattern):
    lps = build_lps(pattern)
    i, j = 0, 0
    while i < len(text):
        if j == len(pattern):
            return True
        if pattern[j] == text[i]:
            i += 1
            j += 1
        elif j != 0:
            j = lps[j-1]
        else:
            i += 1
    return False


def build_lps(pattern):
    n = len(pattern)
    lps = [0]*n
    length = 0
    i = 1
    while i < n:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length != 0:
            length = lps[length-1]
        else:
            i += 1
    return lps