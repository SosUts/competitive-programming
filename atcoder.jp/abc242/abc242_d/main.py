#!/usr/bin/env python3
# from typing import *


# def solve(S: str, Q: int, t: List[int], k: List[int]) -> List[str]:
def solve(S, Q, t, k):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    Q = int(input())
    t = [None for _ in range(Q)]
    k = [None for _ in range(Q)]
    for i in range(Q):
        t[i], k[i] = map(int, input().split())
    a = solve(S, Q, t, k)
    for i in range(Q):
        print(a[i])


if __name__ == "__main__":
    main()
