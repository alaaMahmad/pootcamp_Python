def num_islands(grid):
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    island_count = 0

    # Depth-First Search (DFS) function to fully explore the island and sink land so it isn't counted twice
    def dfs(r, c):
        # Check out-of-bounds conditions and ensure the current cell is land ('1')
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return
        
        # Mark the cell as visited by converting it to water ('0')
        grid[r][c] = '0'

        # Explore in four directions (down, up, right, left)
        dfs(r + 1, c) # Down
        dfs(r - 1, c) # Up
        dfs(r, c + 1) # Right
        dfs(r, c - 1) # Left

    # Iterate through all cells in the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                island_count += 1
                dfs(r, c) # Explore and sink the entire connected island

    return island_count

# Testing the code
matrix = [
  ["1","1","1","0","0"],
  ["0","1","0","0","1"],
  ["0","0","1","1","0"],
  ["0","1","1","0","0"],
  ["0","0","1","0","0"]
]

print(f"Number of Islands: {num_islands(matrix)}")
# Output: 3