def reverseBits(n):
    res = 0

    for i in range(32):
        res = res << 1
        bit = n % 2
        res += bit
        n = n >> 1

    return res


def main():
    n = 11111111111111111111111111111101
    print(reverseBits(n))


if __name__ == "__main__":
    main()
