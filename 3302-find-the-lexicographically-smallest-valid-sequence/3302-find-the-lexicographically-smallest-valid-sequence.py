class Solution:
    def validSequence(self, word1, word2):
        n = len(word1)
        m = len(word2)

        last = [-1] * m

        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        ans = []
        j = 0
        changed = False

        for i in range(n):
            if j == m:
                break

            if word1[i] == word2[j]:
                ans.append(i)
                j += 1

            elif not changed:
                if j == m - 1 or i < last[j + 1]:
                    ans.append(i)
                    j += 1
                    changed = True

        if j == m:
            return ans

        return []