# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-13 14:49:03
# @Last Modified time: 2019-01-13 15:30:28


def main():
    num = int(input())

    H = []
    for i in range(num):
        temp = [int(i) for i in input().split()]
        H.append(temp)

    W = []
    for i in range(num):
        temp = [int(i) for i in input().split()]
        W.append(temp)

    res = 0
    for i in range(num):
        start_w, end_w = W[i]
        for i in range(num):
            start_h, end_h = H[i]
            if end_w < start_h or start_w > end_h:
                res += 0
            elif start_w <= start_h and end_w >= end_h:
                res += end_h - start_h
            elif start_w >= start_h and end_w <= end_h:
                res += end_w - start_w
            elif end_w >= start_h and end_w <= end_h:
                res += end_w - start_h
            elif start_w <= end_h and start_w >= start_h:
                res += end_h - start_w

    print(res)


if __name__ == '__main__':
    main()
