#!/usr/bin/env python3
# from typing import *



# def solve(N: int, M: int, a: List[int], b: List[int], Q: int, x: List[int], y: List[int]) -> List[str]:
def solve(N, M, a, b, Q, x, y):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    a = [None for _ in range(M)]
    b = [None for _ in range(M)]
    for i in range(M):
        a[i], b[i] = map(int, input().split())
    Q = int(input())
    x = [None for _ in range(Q)]
    y = [None for _ in range(Q)]
    for i in range(Q):
        x[i], y[i] = map(int, input().split())
    c = solve(N, M, a, b, Q, x, y)
    for i in range(Q):
        print(c[i])

if __name__ == '__main__':
    main()