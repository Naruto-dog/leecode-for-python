class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1 = list(s)
        if len(s) == len(t):
            for i in t:
                if i not in s1:
                    return False
                else:
                    s1.remove(i)
            return True
        else:
            return False


if __name__ == '__main__':

    run = Solution()
    result = run.isAnagram('rat','car')
    print(result)