def subSet(word):
    word = list(word)
    ans = []

    def help(index, tmp):
        if tmp != '':
            ans.append(tmp)

        for i in range(index, len(word)):
            help(i + 1, tmp + word[i])

    help(0, '')
    return ans


word = 'abc'
print(subSet(word))
