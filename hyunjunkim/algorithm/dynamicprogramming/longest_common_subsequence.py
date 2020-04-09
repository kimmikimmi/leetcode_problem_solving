class Solution(object):

    def longestCommonSubsequence(self, text1, text2):
        r = len(text1) + 1
        c = len(text2) + 1
        
        mat = [[0] * r for i in range(c)]
        print(mat)

        for i in range(1, c):
            for j in range(1, r):
                if text2[i-1] == text1[j-1]:
                    mat[i][j] = mat[i-1][j-1] + 1
                else:
                    mat[i][j] = max(mat[i][j-1], mat[i-1][j])     
                
        print(mat)
        return mat[c-1][r-1]
        


a = Solution()
print(a.longestCommonSubsequence("abcde", "ace"))