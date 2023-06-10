def getMissingNo(nums):
    n = len(nums)
    total = (n + 1)*n//2
    sum_of_nums = sum(nums)
    return total - sum_of_nums


def main():
    nums = [3, 0, 1]
    print(getMissingNo(nums))


if __name__ == "__main__":
    main()