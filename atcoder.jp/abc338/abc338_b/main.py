#!/usr/bin/env python3
# from typing import *
from collections import Counter


# def solve(S: str) -> str:
def solve(S):
    counter = Counter(S)
    counter = counter.most_common()
    max_value = counter[0][1]
    max_list = [i[0] for i in counter if i[1] == max_value]
    # print(max_value, max_list)
    print(sorted(max_list)[0])


# generated by oj-template v4.8.1 (https://github.com/online-judge-tools/template-generator)
def main():
    S = input()
    solve(S)


if __name__ == "__main__":
    main()
