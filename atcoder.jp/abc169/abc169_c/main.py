#!/usr/bin/env python3
# from typing import *



# def solve(A: int, B: float) -> int:
def solve(A, B):
    pass  # TODO: edit here

# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    import sys
    tokens = iter(sys.stdin.read().split())
    A = int(next(tokens))
    B = float(next(tokens))
    assert next(tokens, None) is None
    a = solve(A, B)
    print(a)

if __name__ == '__main__':
    main()