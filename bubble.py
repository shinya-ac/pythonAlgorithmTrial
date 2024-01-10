import random

def bubble_sort(numbers):
    #処理
    # for i in range(len(numbers)-1):
    #     if(numbers[i] > numbers[i+1]):
    #         numbers[i] = numbers[i+1]
    #         numbers[i+1] = numbers[i]
    # for i in range(len(numbers)-2):
    #     if(numbers[i] > numbers[i+1]):
    #         numbers[i] = numbers[i+1]
    #         numbers[i+1] = numbers[i]
    # …のように繰り返される(二重ループ)

    for x in range(len(numbers)):
        for i in range(len(numbers)-(x+1)):
            if(numbers[i] > numbers[i+1]):
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                # print(numbers)
    return numbers

# str[0]とstr[1]の大小を比べる
# 大小が異なれば入れ替えて、大小が正しければそのままにする
# 次にstr[1]とstr[2]の大小を比べる
# 同様に大小が異なれば入れ替えて、大小が正しければそのままにする
# str[n]とあったときにn-1回これを繰り返す(5個の配列があったとすると4回比較する)
# 最後まで達せばlimitの値が加算される→比較の回数が一回へる(5個の配列があったとすると3回比較されることになる)
# 「1回比較されるまで」継続するので5この配列があったとすると4周ループする(limitが4まで加算されるまで続けられる)

if __name__ == '__main__':
    nums = [random.randint(0,1000) for i in range(10)]
    # nums = [2,5,1,8,7,3]
    print(bubble_sort(nums))

# python bubble.py