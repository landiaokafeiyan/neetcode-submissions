class Solution:
    # I would scan the grid row by row and column by column. Whenever I find a cell containing 1, that means I have found a new island, so I increment the island count. Then I use DFS or BFS to visit all connected land cells belonging to that island and mark them as visited, so they won't be counted again.I would scan the grid row by row and column by column. Whenever I find a cell containing 1, that means I have found a new island, so I increment the island count. Then I use DFS or BFS to visit all connected land cells belonging to that island and mark them as visited, so they won't be counted again.
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        islands = 0
        def bfs(r, c):
            q = deque()
            grid[r][c] = "0"
            q.append((r, c))

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    nr, nc = dr + row, dc + col
                    if (nr < 0 or nc < 0 or nr >= ROWS or
                        nc >= COLS or grid[nr][nc] == "0"
                    ):
                        continue
                    q.append((nr, nc))
                    grid[nr][nc] = "0"
        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)#bfs
                    islands += 1

        return islands