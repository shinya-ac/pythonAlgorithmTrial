import random


def gnome(nums):
    for i in range(len(nums)-1):
        # print(f"num[i]:{nums[i]}")
        # print(f"num[i+1]:{nums[i+1]}")
        if nums[i] < nums[i+1]:
            # print(f"iteration{i}(remain):{nums}")
            continue
        else:
            nums[i] , nums[i+1] = nums[i+1] , nums[i]
            reverse(i, nums)
            # print(f"iteration{i}(exchange&reverse):{nums}")
            # import pdb; pdb.set_trace()
    return nums

def reverse(location, nums):
    for i in range(location):
        #print(f"reverse iteration{i}:{nums}")
        #print(f"location-{i}:{location-i}")
        #print(f"location-{i}-1:{location-i-1}")
        if nums[location-i] > nums[location-i-1]:
            continue
        else:
            #print(f"num[location]:{nums[location]}")
            #print(f"num[location-i-1]:{nums[location-i-1]}")
            nums[location-i] , nums[location-i-1] = nums[location-i-1] , nums[location-i]
            continue

if __name__ == '__main__':
    nums = [random.randint(0,1000) for i in range(10)]
    # nums = [2,5,1,8,7,3]
    print(gnome(nums))

# 「import pdb; pdb.set_trace()」の使い方
# l (list): 現在の実行ポイントの周囲のコードを表示します。
# n (next): 次の行に進みますが、関数の内部には入りません。
# s (step): 次の行に進みますが、関数があればその関数の内部にステップインします。
# c (continue): 次のブレークポイントまでプログラムの実行を再開します。
# p (print): 引数として与えた式の値を表示します。例えば、p xは変数xの値を表示します。
# q (quit): デバッグセッションを終了し、プログラムの実行を停止します。
    # 例：p nums　　→ 　その時点のイテレーションのnumsの値を確認できる
    #    q　　→ 　デバッグを終了する