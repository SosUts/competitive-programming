#!/usr/bin/env python3
# from typing import *



# def solve(N: int, K: int, Q: int, A: List[int], L: List[int]) -> List[str]:
def solve(N, K, Q, A, L):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = int(next(tokens))
    K = int(next(tokens))
    Q = int(next(tokens))
    A = [None for _ in range(K)]
    L = [None for _ in range(Q)]
    for i in range(K):
        A[i] = int(next(tokens))
    for i in range(Q):
        L[i] = int(next(tokens))
    assert next(tokens, None) is None
    a = solve(N, K, Q, A, L)
    print(*[a[i] for i in range(K)])

if __name__ == '__main__':
    main()