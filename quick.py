import random

def quick_sort(nums):
    def _quick_sort(nums, low, high):
        if low < high: 
            partition_index = partition(nums, low, high)
            print(f"low: {low}, high: {high}, partition_index: {partition_index}, nums: {nums}")
            _quick_sort(nums, low, partition_index-1)# partition_indexが-1(high)ずつされていく。その結果partition_indexが0になると再帰終了(lowもhighも0)
            _quick_sort(nums, partition_index+1, high)# partition_indexが+1(low)ずつされていく。その結果partition_indexが配列の個数-1分になると再帰終了(lowもhighも配列の個数-1分)
        else:# 出力確認のためだけのelse文
            print(f"\033[31mlow: {low}, high: {high}\033[0m")
    _quick_sort(nums, 0, len(nums)-1)
    return nums


def partition(nums, low, high):
    i = low -1
    pivot = nums[high]
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    print(nums)
    return i + 1

# def quick(nums):# 再帰関数
#     # ここでは「まだ整列していない配列」をswap関数に渡す
#     # swap関数からは「すでに整列した配列」とそのインデックス番号、また、「まだ整列できていない配列」とそのインデックス番号が返される
#     # すでに整列した配列に関してはresult配列にそれを加える
#     # まだ整列していない配列はまた（再帰的に）swapに投入する
#     # 最終的にresult配列の個数が当初のnums配列の個数と等しくなったら完成=全ての整列が完了
#     result_nums = list(len(nums))
#     while len(result_nums) == len(nums):
#         left, center, right = swap(nums)
#         result_nums.extend(left)
#         result_nums.extend(center)
#         result_nums.extend(right)
#     left_ok = False
#     right_ok = False
#     left = []
#     center = []
#     right = []
#     while left_ok == True and right_ok == True:
#         left, center, right, left_ok, right_ok = swap(nums)

#     return left + center + right

    
#     #     print("\033[31mt: {}\033[0m".format(t))

# def swap(nums):
#     print("nums:\033[31mt: {}\033[0m".format(nums))
#     sorted_nums, pivot_location, swaped = partition(nums)
#     # if swaped == False:
#     #     return nums, nums, nums, True,  True
#     print("sorted_nums:\033[31mt: {}\033[0m".format(sorted_nums))
#     if pivot_location != 0:
#         left_nums = sorted_nums[0:pivot_location]
#         print(f"left_nums:{left_nums}")
#         if left_nums != []:
#             sorted_left_nums, _, left_ok = partition(left_nums)
#     if pivot_location != len(nums):
#         right_nums = sorted_nums[pivot_location+1:]
#         print(f"right_nums:{right_nums}")
#         if right_nums != []:
#             sorted_right_nums, _, right_ok = partition(right_nums)
#     print(f"[nums[pivot_location]]:{[sorted_nums[pivot_location]]}")
#     print(f"sorted_left_nums:{sorted_left_nums}")
#     print(f"sorted_right_nums:{sorted_right_nums}")
#     if sorted_left_nums != [] and sorted_right_nums != []:
#         # return sorted_left_nums + [nums[pivot_location]] + sorted_right_nums, True
#         return sorted_left_nums , [nums[pivot_location]] , sorted_right_nums

# def partition(nums):
#     before_nums = nums
#     done = False
#     pivot = nums[-1]
#     i = -1
#     for j in range(len(nums)):
#         if nums[j] <= pivot:
#             print(f"i:{i}")
#             print(f"j:{j}")
#             i += 1
#             nums[i], nums[j] = nums[j], nums[i]
#         if j == len(nums)-1:
#             pivot_location = i
#             print(f"pivot_location:{pivot_location}")
#         if before_nums == nums:
#             done = True
#         print(f"roop nums:{nums}")
#     return nums, pivot_location, done
        
#         # 一旦保存
        



if __name__ == '__main__':
    nums = [1, 8, 3, 9, 4, 5, 7]
    # nums = [random.randint(0,1000) for _ in range(10)]
    print(quick_sort(nums))

# 再帰関数の簡単な例
# def say_hello(times):
#     def _say_hello(n):
#         if n > 0:  # ベースケース: nが0より大きい場合にのみ処理を実行
#             print('hello')  # 'hello'を出力
#             _say_hello(n - 1)  # 内部関数自体を再帰的に呼び出し、回数を1減らす

#     _say_hello(times)  # 内部関数を初回呼び出し

# say_hello(5)
    
# 初期状態
# 配列: [1, 8, 3, 9, 4, 5, 7]

# low = 0, high = 6 (配列の長さ - 1)
# 1回目のパーティショニング
# ピボット: 7 (high = 6の要素)
# パーティション後の配列: [1, 3, 4, 5, 7, 9, 8]
# partition_index = 4
# 分割後の配列をソートするために、再帰的に自身を2回呼び出す:
# 左部分配列: low = 0, high = 3
# 右部分配列: low = 5, high = 6
# 左部分配列のソート ([1, 3, 4, 5])
# ピボット: 5 (high = 3の要素)
# パーティション後: [1, 3, 4, 5] (変化なし、ピボットがすでに正しい位置にある)
# 分割後の左部分配列: low = 0, high = 2
# 左部分配列の更なるソート ([1, 3, 4])
# ピボット: 4 (high = 2の要素)
# パーティション後: [1, 3, 4] (変化なし、ピボットがすでに正しい位置にある)
# 分割後の左部分配列: low = 0, high = 1
# 最も左の部分配列のソート ([1, 3])
# ピボット: 3 (high = 1の要素)
# パーティション後: [1, 3] (変化なし、ピボットがすでに正しい位置にある)
# ここで、low = 0, high = 0のソートは必要なく、再帰呼び出しは終了
# 右部分配列のソート ([9, 8])
# ピボット: 8 (high = 6の要素)
# パーティション後の配列: [8, 9]
# 分割後の右部分配列: low = 6, high = 6 (さらなるソートは不要)