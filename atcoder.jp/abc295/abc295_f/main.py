#!/usr/bin/env python3
# from typing import *

MOD = 998244353

# def solve(a: str, b: str, c: str, d: List[str], e: List[str], f: List[str], g: str) -> Tuple[int, int, int, int, int, int]:
def solve(a, b, c, d, e, f, g):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    a = next(tokens)
    d = [None for _ in range(a)]
    e = [None for _ in range(a)]
    f = [None for _ in range(a)]
    b = next(tokens)
    c = next(tokens)
    for i in range(a):
        d[i] = next(tokens)
        e[i] = next(tokens)
        f[i] = next(tokens)
    g = next(tokens)
    assert next(tokens, None) is None
    a, b, c, d, e, f = solve(a, b, c, d, e, f, g)
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)

if __name__ == '__main__':
    main()