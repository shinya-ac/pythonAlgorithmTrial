import random

def selection_sort(num):
    print("<<<<<処理スタート>>>>>")
    for x in range(len(num)):
        print(f"for x:{x}")
        temp = num[x]
        location: int
        swag_flg = False
        for i in range(len(num)-(x+1)):
            print(f"----------for i:{i}-----------")
            print(f"num:{num}")
            print(f"temp:{temp}")
            if temp > num[x+i+1]:
                temp = num[x+i+1]
                location = (x+i+1)
                print(f"location:{location}")
                swag_flg = True
        print(f"num[i]:{num[x]}")
        print(f"num[location]:{num[location]}")
        if swag_flg == True:
            num[x], num[location] = num[location], num[x]
    return num


if __name__ == '__main__':
    nums = [random.randint(0,1000) for i in range(10)]
    # nums = [2,5,1,8,7,3,4,8]
    print(selection_sort(nums))
