def climbingStairs(n):
    a = 1
    b = 1

    for i in range(n - 1):
        tmp = a
        a = a + b
        b = tmp

    return a


def main():
    print(climbingStairs(10))


if __name__ == "__main__":
    main()
