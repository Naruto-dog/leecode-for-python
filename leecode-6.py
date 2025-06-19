class Solution(object):
    def moveZeroes(self, nums):
        i = 1
        while i <= nums.count(0):
            if 0 in nums:
                nums.remove(0)
                nums.append(0)
            else:
                break
            i += 1
        return nums

        # result = []
        # num0 = []
        # i = 0
        # while i < len(nums):
        #     if nums[i] == 0:
        #         num0.append(nums[i])
        #     elif nums[i] != 0:
        #         result.append(nums[i])
        #     i = i + 1
        # result.extend(num0)
        # return result


if __name__ == '__main__':
    run = Solution()
    print(run.moveZeroes([0,2,0,3,1,0,1]))
