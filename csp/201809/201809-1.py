# -*- coding: utf-8 -*-
# @Author: LogicJake
# @Date:   2019-01-13 14:19:48
# @Last Modified time: 2019-01-13 14:47:58


def main():
    num = int(input())
    first_day_prices = [int(i) for i in input().split()]

    second_day_prices = []
    for i in range(num):
        if i != 0 and i != num - 1:
            second_day_prices.append(
                str(
                    (first_day_prices[i - 1] + first_day_prices[i] + first_day_prices[i + 1]) // 3))
        elif i == 0:
            second_day_prices.append(
                str(
                    (first_day_prices[i] + first_day_prices[i + 1]) // 2))
        elif i == num - 1:
            second_day_prices.append(
                str(
                    (first_day_prices[i - 1] + first_day_prices[i]) // 2))

    second_day_prices = ' '.join(second_day_prices)
    print(second_day_prices)


if __name__ == '__main__':
    main()
