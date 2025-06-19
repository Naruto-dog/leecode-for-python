def signfunc(pro):
    if pro < 0:
        return -1
    elif pro == 0:
        return 0
    else:
        return 1
nums = [-1,-2,-3,-4,3,2,1]
product = 1
for num in nums:
    product = product * num
print(signfunc(product))