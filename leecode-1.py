class Solution:
    def mergeAlternately(self, word1, word2):
        result = ''
        len1 = len(word1) - len(word2)
        word3 = word2[len(word2) + len1::]
        word2 = word2[:len(word2) + len1:]
        # print(f'word1:{word1}  word2:{word2}  word3:{word3}')
        for wd1 in word1:
            result = result + wd1
            for wd2 in word2:
                result = result + wd2
                word2 = word2[1::]
                # print(f'word2:{word2}')
                break
        result = result + word3
        print(result)
if __name__ == '__main__':
    run = Solution()
    run.mergeAlternately('abc', 'pqr')