#!/usr/bin/env python3
# from typing import *


# def solve(N: int, P: List[int], Q: int, A: List[int], B: List[int]) -> List[str]:
def solve(N, P, Q, A, B):
    pass


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))  # 人数
    P = {}  # 人の順番
    for i in range(N):
        P[int(next(tokens))] = i
    Q = int(next(tokens))  # クエリ数
    A = [None for _ in range(Q)]
    B = [None for _ in range(Q)]
    for i in range(Q):
        A[i] = int(next(tokens))
        B[i] = int(next(tokens))
    for i in range(Q):
        if P[A[i]] < P[B[i]]:
            print(A[i])
        else:
            print(B[i])


if __name__ == "__main__":
    main()
