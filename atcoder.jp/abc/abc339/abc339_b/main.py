#!/usr/bin/env python3
# from typing import *


# def solve(H: int, W: int, N: int) -> List[str]:
def solve(H, W, N, grid):
    h = w = 0
    direction = (
        # (h, w) インデックスを+1すると時計回り、減らすと反時計回り
        (-1, 0),  # ↑を向いているとき
        (0, 1),  # →
        (1, 0),  # ↓
        (0, -1),  # ←
    )
    next_ = 0
    for _ in range(N):
        if grid[h][w] == ".":
            grid[h][w] = "#"
            next_ = (next_ + 1) % 4
        else:
            grid[h][w] = "."
            next_ = (next_ - 1) % 4
        h = (h + direction[next_][0]) % H
        w = (w + direction[next_][1]) % W
    return grid


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    H, W, N = map(int, input().split())
    grid = [["."] * W for _ in range(H)]
    grid = solve(H, W, N, grid)
    for h in grid:
        print(*h, sep="")
    # for h in grid_H:
    #     for w in grid_W:
    #         print(h, w, sep="")


if __name__ == "__main__":
    main()