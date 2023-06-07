def addBinary(a, b):
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    ans = ''
    tmp = 0

    for i in range(max_len - 1, -1, -1):
        x = tmp
        x += 1 if a[i] == '1' else 0
        x += 1 if b[i] == '1' else 0
        ans = ('1' if x % 2 == 1 else '0') + ans

        tmp = 0 if x < 2 else 1

    if tmp != 0:
        ans = '1' + ans

    return ans


def main():
    a = "1010"
    b = "1011"
    print(addBinary(a,b))


if __name__ == "__main__":
    main()

