import random

def cocktail_sort(numbers):
    #処理
    # bubbleのように配列のそれぞれの隣り合う要素をインデックス0から順に比べていき、
    # indexよりindex+1が大きい場合は順番を入れ替える(つまり数の大きい要素を一番右に寄せる)というのは同じ
    # 上記に加えて-indexの要素(配列の一番最後の要素)と-index-1の要素の大小を比べていき、
    # -indexよりも-index-1の要素のほうが小さければ順番を入れ替える(つまり数の小さい要素を要素の左に寄せる)という処理も入れる
    # そして前者後者ともに要素を入れ替えたときはフラグをTrueにするという処理も入れる
    # 並べ替えを順次行っていき、並べ替えた結果フラグが反転しなかったらその時点でソートの完了を探知し処理全体を終了するというのがシェイカー(cocktail)ソート

    # for x in range(len(numbers)):
    #     swap_flg = False
    #     for i in range(len(numbers)-(x+1)):
    #         if(numbers[i] > numbers[i+1]):
    #             numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    #             swap_flg = True
    #     if(swap_flg == False):
    #         break
    #     for j in range(1,len(numbers)-x):
    #         if(numbers[-j] < numbers[j-1]):
    #             numbers[-j], numbers[j-1] = numbers[j-1], numbers[-j]
    #             swap_flg = True
    #     if(swap_flg == False):
    #         break
    # return numbers

    
    len_numbers = len(numbers)
    swapped = True
    start = 0
    end = len_numbers - 1
    while swapped:
        swapped = False

        for i in range(start, end):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        if not swapped:
            break

        swapped = False
        end = end - 1

        for i in range(end-1, start-1,-1):
            # print(i)
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                swapped = True

        start = start + 1

    return numbers




if __name__ == '__main__':
    nums = [random.randint(0,1000) for i in range(10)]
    # nums = [2,5,1,8,7,3]
    print(cocktail_sort(nums))

# python cocktail.py