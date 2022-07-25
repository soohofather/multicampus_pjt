# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())

for i in range(0, T):
    oxox = input()
    cnt = 0
    result = 0
    for ii in oxox:
        if ii == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)