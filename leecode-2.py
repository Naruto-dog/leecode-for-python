import random
import time


class Solution:
    @staticmethod
    def findthedifference(s, t):
        s = 'ijhge'
        li = list(s)
        el = chr(random.randint(ord('a'), ord('z')))
        li.append(el)
        t = ''.join(li)

if __name__ == '__main__':
    s = '123654'
    t = '1236554'
    li = list(s)
    result = ''
    for i in t:
        if i not in li:
            result = i
            break
        elif len(li) != 0:
            li.remove(i)
        elif len(li) == 0:
            result = i
    print(result)






