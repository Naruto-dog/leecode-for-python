digits = [0,1,2]
length = len(digits)
num = 0
for i in range(length):
    j = length - 1 - i
    num = 10 ** j * digits[i] + num
num = num + 1
result =list(str(num))
result = list(map(int, result))

print(result)
