#!/usr/bin/env python3
# from typing import *



# def solve(N: int, K: int, a: List[int], b: List[int]) -> int:
def solve(N, K, a, b):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, K = map(int, input().split())
    a = [None for _ in range(N)]
    b = [None for _ in range(N)]
    for i in range(N):
        a[i], b[i] = map(int, input().split())
    a1 = solve(N, K, a, b)
    print(a1)

if __name__ == '__main__':
    main()