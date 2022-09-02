class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def search_islands(row_idx, col_idx, label):
            stack = [[row_idx, col_idx]]
            while stack:
                curr_row, curr_col = stack.pop()
                checked[curr_row][curr_col] = label
                for move_idx in range(4):
                    next_row = curr_row + dx[move_idx]
                    next_col = curr_col + dy[move_idx]
                    if next_row < 0 or next_row >= row_len or next_col < 0 or next_col >= col_len:
                        continue
                    elif checked[next_row][next_col] == 0 and grid[next_row][next_col] == "1":
                        stack.append([next_row, next_col])

        result = 0
        row_len = len(grid)
        col_len = len(grid[0])
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        checked = [[0 for _c in range(col_len)] for _r in range(row_len)]
        for grid_row in range(row_len):
            for grid_col in range(col_len):
                if checked[grid_row][grid_col] == 0 and grid[grid_row][grid_col] == "1":
                    result += 1
                    search_islands(grid_row, grid_col, result)

        return result
