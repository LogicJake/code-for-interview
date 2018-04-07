# encoding:utf-8
'''
    link:https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/description/
    time:2018-4-1
'''
class Solution(object):
    len = 0
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = self.count(s)
        print(res)
        return res['data'].__len__()

    def count(self,s):
        # print(s)
        rres = {}
        if s.__len__() == 0:
            return 0
        elif s.__len__() == 1:
            rres['flag'] = 1
            rres['data'] = s
            return rres
        else:
            res = self.count(s[:(s.__len__() - 1)])
            print(res)
            if res['flag'] == 1:
                data = res['data']
                if not (s[s.__len__()-1]  in data):
                    rres['flag'] = 1
                    rres['data'] = data+s[s.__len__()-1]
                    return rres
                else:
                    rres['flag'] = 0
                    rres['data'] = data
                    return rres
            else:
                return res



if __name__ == '__main__':
    solution = Solution()
    res = solution.lengthOfLongestSubstring("pwwkew")
    print(res)