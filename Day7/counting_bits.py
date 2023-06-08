def countSetBits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count


def countBits(n):
    ans = [0]
    for i in range(1, n + 1):
        tmp = countSetBits(i)
        ans.append(tmp)

    return ans


def main():
    n = 6
    print(countBits(n))


if __name__ == "__main__":
    main()
