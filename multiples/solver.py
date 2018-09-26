def sum_of_multiples_3_5(n):
    sum = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


if __name__ == '__main__':
    sum_of_multiples_3_5(10)
