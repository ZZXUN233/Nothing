from functools import reduce

num_lis = [i for i in range(1001)]


def ifDiv(num):
    if num <= 2:
        return True
    else:
        for i in range(2, round(num/2**0.5)):
            if num % i == 0:
                return False
        return True


result_lis = filter(ifDiv, num_lis)
print(list(result_lis))
