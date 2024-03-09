def get_second_smallest_element(nums):
    smallest_num = nums[0]
    second_smallest_num = nums[0]
    for num in nums:
        # go through list and update the smallest number.
        # if it is updated then update the second smallest to be the previous largest.
        if second_smallest_num > num > smallest_num:
            second_smallest_num = num
        if num < smallest_num:
            second_smallest_num = smallest_num
            smallest_num = num
    return second_smallest_num


def main():
    print(get_second_smallest_element([-15, -112, 14, -29, 17, 360, 86, 128, -12, 0, 23]))


if __name__ == "__main__":
    main()