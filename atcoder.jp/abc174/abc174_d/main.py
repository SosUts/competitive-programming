#!/usr/bin/env python3
# from typing import *



# def solve(N: str, c: List[str]) -> int:
def solve(N, c):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    N = next(tokens)
    c = [None for _ in range(N)]
    for i in range(N):
        c[i] = next(tokens)
    assert next(tokens, None) is None
    a = solve(N, c)
    print(a)

if __name__ == '__main__':
    main()