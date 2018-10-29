# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2018-10-29 13:06:03
# @Last Modified time: 2018-10-29 13:22:02


class Solution(object):

    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
            local_name, domain_name = email.split('@')
            local_name = local_name.split('+')[0]
            local_name = local_name.replace('.', '')

            res.add(local_name + '@' + domain_name)

        return len(res)

if __name__ == '__main__':
    solution = Solution()
    emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]

    res = solution.numUniqueEmails(emails)
