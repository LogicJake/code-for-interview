class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        len1 = len(first)
        len2 = len(second)

        if abs(len1 - len2) > 1:
            return False

        if len1 > len2:
            first, second = second, first

        for i in range(len(first)):
            if first[i] != second[i]:
                return first[i:] == second[i + 1:] or first[i +
                                                            1:] == second[i +
                                                                          1:]
        return True
