def areDistinct(str, i, j):
    visited = [0] * 26

    for k in range(i, j + 1):
        if visited[ord(str[k]) - ord('a')]:
            return False

        visited[ord(str[k]) - ord('a')] = True

    return True


def longestUniqueSubsttr(str):
    n = len(str)

    res = 0

    for i in range(n):
        for j in range(i, n):
            if areDistinct(str, i, j):
                res = max(res, j - i + 1)

    return res
