dates = input()

dates = dates.split(' ')

dates.sort()

dates = dates[:3]

dates = [str(date) for date in dates]

ans = ' '.join(dates)
print(ans)
