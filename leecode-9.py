'''给你一个数字数组 arr 。

如果一个数列中，任意相邻两项的差总等于同一个常数，那么这个数列就称为 等差数列 。

如果可以重新排列数组形成等差数列，请返回 true ；否则，返回 false 。'''
arr = [0,6,3,9]
arr = sorted(arr)
d = arr[1] - arr[0]
n = 1
result = True
for i in range (len(arr)):
    if arr[i] == arr[0] + (n - 1) * d:
        n = n + 1
        result = result
    else:
        result = False
print(result)
