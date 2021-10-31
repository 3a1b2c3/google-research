class Solution:
    #https://leetcode.com/problems/unique-paths/discuss/497402/Python3-approaches-(math-DFS-and-DP)-with-detailed-explanation
    def uniquePaths1(self, m: int, n: int) -> int:
        from math import factorial
        return factorial((m-1)+(n-1))//(factorial(n-1) * factorial(m-1))

    def uniquePaths(self, m: int, n: int) -> int:   
        '''            treating the grid as if it was a Binary DAG.
            Binary -> because only two choices out of 4 are allowed
            Acyclic -> because movement is restricted
            time: O(V+2E) where V is the number of cells in the grid = (mn) ---> O(mn + 2E)**
            space: O(m*n) for the stack**
            __ 2 __
            DFS solution (TLE 37/62)
            -- treating the grid with only two types of movement as if it was a Binary DAG.
                - Binary -> because only two choices out of 4 are allowed
                - Acyclic -> because movement is restricted
            time: O(V+2E) where V is the number of cells in the grid = (m*n) ---> O(m*n + 2E)
            space: O(m*n) for the stack
     '''  
        if not m or not n:
            return 0
        if m == 1 or n == 1:
            return 1

        stack = [(0,0)]
        count = 0
        dirs = [(1,0), (0,1)] # only two movements (left and right)
        # bcuz movement is restricted downwards - we dont need to worry about the dfs expanding upwards and thus no need for a visited set
        while stack:
            node = stack.pop()
            x, y = node
            if x == m-1 and y == n-1: # leaf node reached (finish cell)
                    count += 1
                    # print('-----*****-----')
            for dir in dirs:
                    new_x, new_y = x+dir[0], y+dir[1]
                    # within bounds:
                    if new_x >= 0 and new_x <= m-1 and new_y >= 0 and new_y <= n-1:
                        stack.append((new_x, new_y))
        return count

    def uniquePaths2(self, m: int, n: int) -> int:
          '''
        3 - Dynamic programming

            bottom - up (solve the smaller problem first)

            How many ways I can reach the next cell?

            Top row:

                there's only one way to visit/reach the cells at the top row if we start from (0,0)
                in each cell, we will memoize the value 1 which indicates that each one of those cells
                can only be visited once

            Left most column:

                there's only one way to visit/reach those cells as well

            for the rest of the grid:

                each cell can literally be visited in two ways (from the left and from above)
                so for each cell the value that reprsenets the number of ways it can be reached will be
                incremented from above and from left

                __ 3 __
                Dynamic programming
                bottom - up
                solve the smaller problem first

                how many ways I can reach the next cell

                    - Top row:
                            there's only one way to visit/reach the cells at the top row if we start from (0,0)
                            in each cell, we will memoize the value 1 which indicates that each one of those cells
                            can only be visited once


                    - Left most column:
                            there's only one way to visit/reach those cells as well 


                    - for the rest of the grid:
                            - each cell can literally be visited in two ways (from the left and from above)
                            so for each cell the value that reprsenets the number of ways it can be reached will be
                    incremented from above and from left      
        '''
        if not m or not n:
            return 0
        
        if m == 1 or n == 1:
            return 1
        
        # build a grid/matrix to use for memoization
        g = [[0 for i in range(m)] for i in range(n)]
        # print(g)
        
        # top most row
        for i in range(m):
            g[0][i] = 1
        # left most col
        
        for i in range(n):
            g[i][0] = 1
        # print(g)
        
        for i in range(1, n):
            for j in range(1, m):
                g[i][j] = g[i-1][j] + g[i][j-1]
        # print(g)
        
        return g[n-1][m-1]
        
