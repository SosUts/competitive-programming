#!/usr/bin/env python3
# from typing import *



# def solve(N: int, A: List[int], B: List[int], X: List[int]) -> int:
def solve(N, A, B, X):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    A = [None for _ in range(N - 1)]
    B = [None for _ in range(N - 1)]
    X = [None for _ in range(N - 1)]
    for i in range(N - 1):
        A[i], B[i], X[i] = map(int, input().split())
    a = solve(N, A, B, X)
    print(a)

if __name__ == '__main__':
    main()