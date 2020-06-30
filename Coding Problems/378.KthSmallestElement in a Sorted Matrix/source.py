class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        temp = []
        print(matrix)
        count = 0
        for i in range(n):
            for j in range(n):
                temp.append(matrix[i][j])
        temp.sort()
        for i in range(n):
            for j in range(n):
                matrix[i][j] = temp[count]
                count +=1
        print(matrix)
        count = 1
        for i in range(n):
            for j in range(n):
                if count == k:
                    return matrix[i][j]
                count +=1
