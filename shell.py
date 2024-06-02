import random


def shell(nums):
    len_numbers = len(nums)
    gap = len_numbers // 2
    # print(f"len_numbers-gap:{len_numbers-gap}")
    while gap >= 1:
        print(gap)
        for i in range(gap, len_numbers):
            temp = nums[i]
            print(f"temp:{temp}")
            j = i-gap
            while j >= 0 and nums[j] > temp:
                # print(f"nums[j]:{nums[j]}")
                # print(f"temp:{temp}")
                nums[j+gap] = nums[j]
                # print(f"6を奥に置く：nums:{nums}")
                j-=gap
                nums[j+gap] = temp
                # print(f"tempを手前に置くnums:{nums}")
        gap = gap // 2
        

    return nums

if __name__ == '__main__':
    #nums = [5, 6, 9, 2, 3]
    nums = [random.randint(0,1000) for _ in range(10)]
    print(shell(nums))