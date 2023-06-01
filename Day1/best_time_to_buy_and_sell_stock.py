def profit(prices):
    a = []
    tmp = prices.copy()
    for i in range(len(prices)):
        x = prices[i]
        del tmp[0]
        for j in tmp:
            t = x - j
            a.append(t)

    ans = min(a)
    if ans >= 0:
        return 0
    else:
        return -ans


def main():
    prices = [7, 6, 4, 3, 1]
    print(profit(prices))


if __name__ == "__main__":
    main()
