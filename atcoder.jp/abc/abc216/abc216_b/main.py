#!/usr/bin/env python3
# from typing import *

YES = "Yes"
NO = "No"


# def solve(N: int, S: List[str], T: List[str]) -> str:
def solve(N, S, T):
    pass  # TODO: edit here


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    N = int(input())
    S = [None for _ in range(N)]
    T = [None for _ in range(N)]
    for i in range(N):
        S[i], T[i] = input().split()
    a = solve(N, S, T)
    print(a)


if __name__ == "__main__":
    main()