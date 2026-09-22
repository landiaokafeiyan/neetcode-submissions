class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        q = deque()

        def addCell(r, c):
            if (min(r, c) < 0 or r == ROWS or c == COLS or
                (r, c) in visit or grid[r][c] == -1
            ):
                return
            visit.add((r, c))
            q.append([r, c])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visit.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addCell(r + 1, c)
                addCell(r - 1, c)
                addCell(r, c + 1)
                addCell(r, c - 1)
            dist += 1
from collections import deque

def islandsAndTreasure(grid):
    rows = len(grid)
    cols = len(grid[0])

    queue = deque()

    # Put all treasure cells into the queue.
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 0:
                queue.append((r, c))

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    while queue:
        r, c = queue.popleft()

        for dr, dc in directions:
            nr = r + dr
            nc = c + dc

            # Outside grid
            if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                continue

            # Water / obstacle
            if grid[nr][nc] == -1:
                continue

            # Already visited
            if grid[nr][nc] != 2147483647:
                continue

            # Distance from nearest treasure
            grid[nr][nc] = grid[r][c] + 1

            queue.append((nr, nc))