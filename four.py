def dfs(grid, i, j):
    rows = len(grid)
    cols = len(grid[0])
    
    # Boundary and water check
    if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == '0':
        return
    
    # Mark as visited (sink the island)
    grid[i][j] = '0'
    
    # Visit all 4 directions
    dfs(grid, i+1, j)  # down
    dfs(grid, i-1, j)  # up
    dfs(grid, i, j+1)  # right
    dfs(grid, i, j-1)  # left


def num_islands(grid):
    if not grid:
        return 0
    
    count = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            
            if grid[i][j] == '1':
                count += 1          # New island found
                dfs(grid, i, j)     # Visit entire island
    
    return count


# Example
grid = [
    ['1','1','0','0'],
    ['1','0','0','1'],
    ['0','0','1','1'],
    ['0','0','0','0']
]

print("Number of Islands:", num_islands(grid))