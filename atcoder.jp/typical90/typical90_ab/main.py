#!/usr/bin/env python3
# from typing import *



# def solve(N: int, lx: List[int], ly: List[int], rx: List[int], ry: List[int]) -> List[str]:
def solve(N, lx, ly, rx, ry):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    lx = [None for _ in range(N)]
    ly = [None for _ in range(N)]
    rx = [None for _ in range(N)]
    ry = [None for _ in range(N)]
    for i in range(N):
        lx[i], ly[i], rx[i], ry[i] = map(int, input().split())
    A = solve(N, lx, ly, rx, ry)
    for i in range(N):
        print(A[i])

if __name__ == '__main__':
    main()