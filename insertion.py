import random


# def insertion(nums):
    # for i in range(len(nums)-1):
    #     if nums[i] < nums[i+1]:
    #         continue
    #     else:
    #         nums[i], nums[i+1] = nums[i+1], nums[i]
    #         temp = nums[i]
    #         for x in range(i):
    #             if nums[i-(x+1)] < temp:
                    
    #                 continue
    #             else:
    #                 nums[i], nums[i-(x+1)] = nums[i-(x+1)], nums[i]
    #                 continue
    # return nums

def insertion(nums):
    len_numbers = len(nums)
    for i in range(1, len_numbers):
        temp = nums[i]
        j = i-1
        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1

            nums[j+1] = temp
    return nums


if __name__ == '__main__':
    # nums = [1,7,3,2,8,5]
    nums = [random.randint(0,1000) for i in range(10)]
    print(insertion(nums))