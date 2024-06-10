import random


def count(nums):
    max_num = max(nums)
    count_list = [None] * (max_num+1)
    print(f"count_list:{count_list}")
    for i in range(len(count_list)):
        amount = nums.count(i)
        print(f"amount:{amount}")
        count_list[i] = amount
        print(f"count_list:{count_list}")
    for i in range(1, len(count_list)):
        count_list[i] += count_list[i-1]
        print(f"added count_list:{count_list}")
    result = [None] * 7
    for i in range(len(nums)-1, -1, -1):
        print(i)
        print(f"nums[i]:{nums[i]}")
        print(f"count_list[nums[i]]:{count_list[nums[i]]}")
        result[count_list[nums[i]]-1] = nums[i]
        count_list[nums[i]] -= 1
        print(f"result:{result}")
        print(f"after count_list:{count_list}")
    return result
    

    

    return nums

if __name__ == '__main__':
    nums = [4, 3, 6, 2, 3, 4, 7]
    #nums = [random.randint(0,1000) for _ in range(10)]
    print(count(nums))