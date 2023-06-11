def palindromeNumber(x):
    ans = str(x) == str(x)[::-1]
    return ans


def main():
    x = 121
    print(palindromeNumber(x))


if __name__ == "__main__":
    main()