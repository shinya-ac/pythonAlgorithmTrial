# def binary_search(nums, t):
#     def _binary_search(nums, i):
#             m=len(nums)//2

#             if len(nums) == 0:  # 配列が空の場合
#                 return -1

#             # [0,1,5,7,9,11,15,20,24,30]
#             if nums[m] == t:
#                  return i + m
#             if nums[m] > t:
#                  # インデックス0~4の配列
#                  # [0,1,5,7,9]
#                  return _binary_search(nums[:m], i)
#             else:
#                  # インデックス5~9の配列
#                  # m=5
#                  # [11,15,20,24,30]
#                  return _binary_search(nums[m+1:], i+m+1)
#     result = _binary_search(nums, 0)

#     return result

# 再帰関数なし
# def binary_search(numbers, value):
#     left, right = 0, len(numbers) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if numbers[mid] == value:
#             return mid
#         elif numbers[mid] < value:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1

# 再帰関数あり
def binary_search(numbers, value):
    def _binary_search(numbers, value, left, right):
        if left > right:
            return -1

        mid = (left + right) // 2
        if numbers[mid] == value:
            return mid
        elif numbers[mid] < value:
            return _binary_search(numbers, value, mid + 1, right)
        else:
            return _binary_search(numbers, value, left, mid - 1)

    return _binary_search(numbers, value, 0, len(numbers) - 1)



if __name__ == '__main__':
    nums = [0,1,5,7,9,11,15,20,24, 30]
    print(binary_search(nums, 5))