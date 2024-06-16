import random
# 一旦挫折
def merge_sort(nums):
    devide(nums)
    return


def devide(list):
    def _devide(nums):
        if len(nums) > 1:
            center = round(len(nums)/2)
            left_array = []
            right_array = []
            for i in range(0,center):
                left_array.append(nums[i])
            for i in range(center, len(nums)):
                # return
                right_array.append(nums[i])
            print(center)
            print(left_array)
            print(right_array)
    _devide(list)
    return list


if __name__ == '__main__':
    nums = [1, 8, 3, 9, 4, 5, 7]
    # nums = [random.randint(0,1000) for _ in range(10)]
    print(merge_sort(nums))