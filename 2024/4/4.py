from typing import List

def string_to_letter_grid(input: str) -> List[List[str]]:
    return [list(l) for l in input.split()]

def count_xmas(g: List[List[str]]) -> int:
    if len(g) == 0:
        return 0
    w = len(g[0])
    h = len(g)
    c = 0
    for x in range(w):
        for y in range(h):
            if g[y][x] == 'X':
                # if we can go across to the right
                if x < w - 4:
                    if ''.join(g[y][x+1:x+4]) == 'MAS':
                        c += 1
                        #print(x, y)
                # left
                if x > 2:
                    if ''.join(g[y][x-3:x][::-1]) == 'MAS':
                        c += 1
                        #print(x, y)
                # up
                if y > 2:
                    if g[y-1][x] + g[y-2][x] + g[y-3][x] == 'MAS':
                        c += 1
                        #print(x, y)
                # down
                if y < h - 4:
                    if g[y+1][x] + g[y+2][x] + g[y+3][x] == 'MAS':
                        c += 1
                        #print(x, y)
                # up-right
                if y > 2 and x < w - 4:
                    if g[y-1][x+1] + g[y-2][x+2] + g[y-3][x+3] == 'MAS':
                        c += 1
                        #print(x, y)
                # up-left
                if y > 2 and x > 2:
                    if g[y-1][x+1] + g[y-2][x+2] + g[y-3][x+3] == 'MAS':
                        c += 1
                        #print(x, y)



    return c
                        
                    
                

s = '''
MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
'''

g = string_to_letter_grid(s)
count_xmas(g)