import random

def bogo_sort(numbers):
    random.shuffle(numbers)
    return numbers
    


if __name__ == '__main__':
    print(bogo_sort([1, 5, 3, 2, 6]))

# python bogo.py