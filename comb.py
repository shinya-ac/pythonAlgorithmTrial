import random

# def comb_sort(numbers):
#     #処理
#     input_len = len(numbers)
#     gap = input_len // 1.3
#     int_gap = int(gap)
#     print(len(numbers))
#     print(int_gap)

#     for x in range(input_len):
#         if(int_gap == 1):
#             swap_flg = True
#             start = 0
#             end = len(numbers) - 1
#             while swap_flg:
#                 print("int_gap0処理スタート")
#                 swap_flg = False
#                 for i in range(start, end):
#                     if numbers[i] > numbers[i+1]:
#                         numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
#                         swap_flg = True
#             break
#         for i in range(len(numbers)-int_gap):
#             print("----------周回"+str(i)+"-----------")
#             print("numbers[i]"+str(numbers[i]))
#             print("numbers[i+int_gap]"+str(numbers[i+int_gap]))
#             if(numbers[i] > numbers[i+int_gap]):
#                 print("numbers[i+int_gap]"+str(numbers[i+int_gap]))
#                 numbers[i], numbers[i+int_gap] = numbers[i+int_gap], numbers[i]
#             print("numbers"+str(numbers))
#         print("ループ前int_gap："+str(int_gap))
#         int_gap = int(int_gap // 1.3)
#         print("ループ後int_gap："+str(int_gap))
            
#     return numbers

def comb_sort(numbers):
    len_numbers = len(numbers)
    gap = len_numbers
    swapped = True

    while gap != 1 or swapped:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1

        swapped = False

        for i in range(0, len_numbers - gap):
            if numbers[i] > numbers[i + gap]:
                numbers[i], numbers[i + gap] = numbers[i + gap], numbers[i]
                swapped = True
    return numbers

#処理
    # 配列の個数%1.3すると5になる
    # 先頭から5個離れた数字と先頭の数字を比べて並べ替えるかどうか
    # 先頭から1個ずらした場所から5個離れた数字を比べて並べ替えられるかどうか
    # 二週目からは一週目の幅だった5をもとに5%1.3すると3になる
    # 先頭から3個離れている数字と比べて…さらに先頭から1進んだところから3個離れているところを比べて…
    # としていく。最後はギャップが2%1.3で1になる
    # 先頭の数字とその次の数字で比べていく、と言うのを順番にやる。途中で入れ替えることがあれば「swap_flg」をtrueにする

if __name__ == '__main__':
    nums = [random.randint(0,1000) for i in range(10)]
    # nums = [2,5,1,8,7,3,4,8]
    print(comb_sort(nums))

# python comb.py