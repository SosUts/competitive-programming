#!/usr/bin/env python3
# from typing import *


# def solve(N: int, Q: int, A: List[int], T: List[int], X: List[int], Y: List[int]) -> Tuple[str, List[str], List[str]]:
def solve(N, Q, A, T, X, Y):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys

    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    Q = int(next(tokens))
    A = [None for _ in range(N)]
    T = [None for _ in range(Q)]
    X = [None for _ in range(Q)]
    Y = [None for _ in range(Q)]
    for i in range(N):
        A[i] = int(next(tokens))
    for i in range(Q):
        T[i] = int(next(tokens))
        X[i] = int(next(tokens))
        Y[i] = int(next(tokens))
    assert next(tokens, None) is None
    b, e, f = solve(N, Q, A, T, X, Y)
    print(b)
    for i in range(b):
        print(e[i])
        print(f[i])


if __name__ == "__main__":
    main()
