# python_assignment_sigmoid

simple dfs problem:
1. Take n and m(matrix dimensions) input from the user
2. Create a matrix of n*m size. This matrix contains 'X' and 'O'
3. Now according to question, we need to flip all O's that are 4 directionally surrounded by 'X'
4. call DFS from each cell on the boundary of the board which contains 'O'
5. While performing Dfs, mark all the cells(O's) as -1. -1 indicates that these cells these cells will not be converted to 'X'
6. Now the O's that are left are our target. Convert all these leftover O's to 'X'
7. Now traverse the matrix again and convert all '-1s' back to 'O'. These O's will not be converted, so changing them back

