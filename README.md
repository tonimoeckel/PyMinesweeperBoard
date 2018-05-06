# Minesweeper Board Builder

This project is part of a python exercise. 

This little app adds numbers to a minesweeper board. Input is a empty minesweeper board as string array, with "*" as mines. Output are the solved numbers that indicate how many mines are horizonally, vertically or diagonally next to the mine. 
The mine board must be square and has to be bordered by "#" signs.

Input: Array of strings
Output: Array of strings

## Sample

 
```python
from minesweeperboard import board

input = ['########',
         '# *  * #',
         '#  *   #',
         '#    * #',
         '#   * *#',
         '# *  * #',
         '#      #',
         '########']

res = board(input)
print(res)
```

## Tests

A test, that checks validation and functionality is included. 