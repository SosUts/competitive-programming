#!/usr/bin/env python3
# from typing import *

YES = 'Yes'
NO = 'No'

# def solve(N: int, S: int, D: int, X: List[int], Y: List[int]) -> str:
def solve(N, S, D, X, Y):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, S, D = map(int, input().split())
    X = [None for _ in range(N)]
    Y = [None for _ in range(N)]
    for i in range(N):
        X[i], Y[i] = map(int, input().split())
    a = solve(N, S, D, X, Y)
    print(a)

if __name__ == '__main__':
    main()