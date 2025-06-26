'''如果数组是单调递增或单调递减的，那么它是 单调 的。

如果对于所有 i <= j，nums[i] <= nums[j]，那么数组 nums 是单调递增的。 如果对于所有 i <= j，nums[i] >= nums[j]，那么数组 nums 是单调递减的。

当给定的数组 nums 是单调数组时返回 true，否则返回 false。'''
from bdb import Breakpoint

nums = [1,3,2]
inc = 1
dec = 1
result = True
length = len(nums)
for i in range (length-1):
    if nums[i] >= nums[i+1]:
        inc += 1
    if nums[i] <= nums[i + 1]:
        dec += 1
if inc == length or dec == length:
    result = True
else:
    result = False

'''
list1 = sorted(nums)
list2 = sorted(nums, reverse=True))
if nums == list1 or nums == list2:
    result = True
else:
    result = False
'''
