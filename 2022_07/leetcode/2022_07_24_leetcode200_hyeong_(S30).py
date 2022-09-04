from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        result = 0
        if not grid:
            return 0
        row, col = len(grid), len(grid[0])
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    result += 1
        return result

    def dfs(self, grid, s_row, s_col):
        if s_row < 0 or s_row >= len(grid) or s_col < 0 or s_col >= len(grid[0]):
            return
        if grid[s_row, s_col] == '0':
            return
        grid[s_row][s_col] = '0'
        self.dfs(grid, s_row + 1, s_col)
        self.dfs(grid, s_row, s_col + 1)
        self.dfs(grid, s_row - 1, s_col)
        self.dfs(grid, s_row, s_col - 1)