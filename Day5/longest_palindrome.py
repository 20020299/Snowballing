from collections import Counter


def longestPalindrome(s):
    c = Counter(s)
    ans = 0
    odd_found = False
    for count in c.values():
        if odd_found:
            if count > 1:
                if count % 2 == 0:
                    ans += count
                else:
                    ans += count - 1
        else:
            if count % 2 == 0:
                ans += count
            else:
                ans += count
                odd_found = True

    return ans


def main():
    s = 'abccccdd'
    print(longestPalindrome(s))


if __name__ == "__main__":
    main()
