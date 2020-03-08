#  leetcode- node an easy problem Man!!

import copy
from collections import deque


class Solution:

    def pushAllRottenOrangesToQueue(self, grid, q):
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 2):
                    q.append((i, j, 0))  # oth minute rotten oranges

    def allFresh(self, grid):
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 2):
                    return False
        return True

    def noOranges(self, grid):
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if(grid[i][j] != 0):
                    return False
        return True

    def allRotten(self, grid):
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if(grid[i][j] == 1):
                    return False
        return True

    def allvisited(self, visited):
        n = len(visited)
        m = len(visited[0])
        for i in range(n):
            for j in range(m):
                if(visited[i][j] not in (0, 3)):
                    return False
        return True

    def addtoQueue(self, i, j, q, visited, d):
        n = len(visited)
        m = len(visited[0])
        if(i+1 < n and visited[i+1][j] == 1):
            q.append((i+1, j, d))
            visited[i+1][j] = 3

        if(i-1 >= 0 and visited[i-1][j] == 1):
            q.append((i-1, j, d))
            visited[i-1][j] = 3

        if(j+1 < m and visited[i][j+1] == 1):
            q.append((i, j+1, d))
            visited[i][j+1] = 3

        if(j-1 >= 0 and visited[i][j-1] == 1):
            q.append((i, j-1, d))
            visited[i][j-1] = 3

    def orangesRotting(self, grid: List[List[int]]) -> int:
        if(self.noOranges(grid) or self.allRotten(grid)):
            return 0
        if(self.allFresh(grid)):
            return -1

        max_minute = 0
        q = deque()
        visited = copy.deepcopy(grid)
        self.pushAllRottenOrangesToQueue(grid, q)
        while(len(q)):
            newRotten = q.popleft()
            self.addtoQueue(newRotten[0], newRotten[1],
                            q, visited, newRotten[2]+1)
            max_minute = max(max_minute, newRotten[2])
            visited[newRotten[0]][newRotten[1]] = 3

        if(self.allvisited(visited)):
            return max_minute
        return -1
