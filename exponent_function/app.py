

def raise_to_power_num(base_num, pow_num):
    return int(base_num) ** int(pow_num)

print(raise_to_power_num(3, 3))

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 2))