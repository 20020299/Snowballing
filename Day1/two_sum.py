def twoSum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(n):
            if nums[i] + nums[j] == target and i != j:
                num1 = i
                num2 = j
                break

    return num1, num2


def main():
    a = [3, 3]
    x = 6
    num1, num2 = twoSum(a, x)
    print(num1, num2)


if __name__ == "__main__":
    main()
