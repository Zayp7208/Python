milage = float(input())
cost = float(input())

miles_20 = 20 / milage * cost
miles_75 = 75 / milage * cost
miles_500 = 500 / milage * cost

print(f'{miles_20:.2f} {miles_75:.2f} {miles_500:.2f}')