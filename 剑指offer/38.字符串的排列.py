from typing import List


class Solution:
    def permutation(self, s: str) -> List[str]:
        chars = list(s)

        path = []
        ans = []

        def help(index):
            if len(path) == len(s):
                ans.append(''.join(path))

            mem = set()
            for i in range(index, len(s)):
                if chars[i] in mem:
                    continue
                mem.add(chars[i])

                chars[i], chars[index] = chars[index], chars[i]
                path.append(chars[index])
                help(index + 1)
                chars[i], chars[index] = chars[index], chars[i]
                path.pop(-1)

        help(0)
        return ans
