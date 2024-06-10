import random

def radix(nums):
    max_num = max(nums)
    num_str = str(max_num)
    num_digits_len = len(num_str) # 桁数
    t = 1
    for _ in range(num_digits_len):
        nums = count(nums, t)
        t *= 10
        print(f"roop nums:{nums}")

        


def count(nums, t):
    digit_nums = [0] * len(nums)
    for i in range(len(nums)):
        digit_nums[i] =  (nums[i] // t) % 10
        print("\033[31mt: {}\033[0m".format(t))
        print(f"nums[i]:{nums[i]}")
        print(f"digit_nums:{digit_nums}")
    max_num = max(digit_nums)
    count_list = [None] * (max_num+1)
    print(f"count_list:{count_list}")
    for i in range(len(count_list)):
        amount = digit_nums.count(i)
        print(f"amount:{amount}")
        count_list[i] = amount
        print(f"count_list:{count_list}")
    for i in range(1, len(count_list)):
        count_list[i] += count_list[i-1]
        print(f"added count_list:{count_list}")
    result = [None] * len(nums)
    for i in range(len(digit_nums)-1, -1, -1):
        print(i)
        print(f"nums[i]:{nums[i]}")
        print(f"count_list[nums[i]]:{count_list[digit_nums[i]]}")
        result[count_list[digit_nums[i]]-1] = nums[i]
        count_list[digit_nums[i]] -= 1
        print(f"result:{result}")
        # print(f"after count_list:{count_list}")
    return result


if __name__ == '__main__':
    # nums = [24, 10, 11, 324, 201, 101, 55]
    # nums = [17, 10, 13, 12, 3, 8, 14]
    nums = [random.randint(0,1000) for _ in range(10)]
    print(radix(nums))