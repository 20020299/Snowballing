def hammingWeight(n):
    n = str(n)
    one_count = 0
    for i in n:
        if i == "1":
            one_count += 1
    return one_count


def main():
    n = 11111111111111111111111111111101
    print(hammingWeight(n))


if __name__ == "__main__":
    main()
