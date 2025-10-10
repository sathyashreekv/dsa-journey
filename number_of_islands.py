def number_of_islands(grid:list[list[int]])->int:
    if not grid:
        return 0
    rows,col=len(grid),len(grid[0])
    islands=0
    def dfs(r,c):
        if r<0 or c<0 or r>=rows or c>=col or grid[r][c]=='0':
            return
        grid[r][c]='0'
        dfs(r+1,c)
        dfs(r-1,c)
        dfs(r,c+1)
        dfs(r,c-1)
    for r in range(rows):
        for c in range(col):
            if grid[r][c]=='1':
                islands+=1
                dfs(r,c)
    return islands

if __name__=="__main__":
    grid=[
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    print(f"Number of islands: {number_of_islands(grid)}")


