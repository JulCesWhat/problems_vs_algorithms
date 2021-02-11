

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        return None

    x_num = number
    y_num = (x_num + 1) // 2
    while y_num < x_num:
        x_num = y_num
        y_num = (x_num + number // x_num) // 2
    return x_num


print(sqrt(100))
# 10

print(sqrt(0))
# 0

print(sqrt(5))
# 2

print(sqrt(-1))
# None

print(sqrt(-100))
# None
