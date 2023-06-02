def binarySearch(nums, target):
    n = len(nums)
    l = 0
    r = n - 1
    while l <= r:
        mid = l + (r - l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return -1


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 0
    print(binarySearch(nums, target))


if __name__ == "__main__":
    main()
