#!/usr/bin/env python3
# from typing import *


# def solve(N: int, M: int, s: List[int], t: List[int]) -> List[str]:
def solve(N, M, s, t):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N, M = map(int, input().split())
    s = [None for _ in range(M)]
    t = [None for _ in range(M)]
    for i in range(M):
        s[i], t[i] = map(int, input().split())
    ans = solve(N, M, s, t)
    for i in range(M):
        print(ans[i])


if __name__ == "__main__":
    main()