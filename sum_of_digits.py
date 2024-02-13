def sum_digits(number):
    number = str(number)
    return sum(map(lambda x: int(number[x]), range(len(number))))

my_num = 64
print(sum_digits(my_num))