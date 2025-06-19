import time


class Solution(object):
    def repeatedSubstringPattern(self, s):
        # i = 0
        # result = False
        # while i < len(s) / 2:
        #     j = 1
        #     s1 = s[:i+1]
        #     i = i + 1
        #     sl = len(s1)
        #     # print(s1, sl, '前置')
        #     while j * sl < len(s):
        #         if s.find(s1, j * sl, j * sl + sl) == -1:
        #             # print(s1, '不能过','后置')
        #             break
        #         elif (j + 1)* sl == len(s):
        #             # print(j, '过', '最后')
        #             result =True
        #             break
        #         j = j + 1
        #     if result:
        #         break
        # return result
        return (s + s).find(s, 1) != len(s)

if __name__ == '__main__':
    run = Solution()
    res = run.repeatedSubstringPattern('abab')
    print(res)
