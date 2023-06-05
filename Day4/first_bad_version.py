bad = 0


def isBadVersion(version):
    if version >= bad:
        return True
    return False


def firstBadVersion(n):
    if n < 2:
        return n
    start = 1
    end = n
    while start <= end:
        mid = (start + end) // 2
        if isBadVersion(mid) and not isBadVersion(mid - 1):
            return mid
        elif isBadVersion(mid - 1):
            end = mid - 1
        else:
            start = mid + 1


n = 5
bad = 2
ans = firstBadVersion(n)
print(ans)
