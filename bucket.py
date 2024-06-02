import random
from itertools import chain

# バケットサイズは10
def bucket(nums):
    max_num = max(nums)
    len_numbers = len(nums)
    bucket_size = max_num // len_numbers
    bucket = [[] for _ in range(bucket_size)]
    for i in range(len_numbers):
        shou = nums[i] // bucket_size
        if shou == bucket_size:
            shou = bucket_size-1
        bucket[shou].append(nums[i])
    result_list = list()
    for i in range(bucket_size):
        inserted_nums = insertion(bucket[i])
        print(inserted_nums)
        result_list.append(inserted_nums)
    chained_list = list(chain.from_iterable(result_list))
    return chained_list

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
    nums = [1,5,28,25,100,52, 27, 91, 22, 99]
    #nums = [random.randint(0,1000) for _ in range(10)]
    print(bucket(nums))