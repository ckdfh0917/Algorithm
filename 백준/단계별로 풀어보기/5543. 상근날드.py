menu = [int(input()) for _ in range(5)]

burger = min(menu[0:3])
coke = min(menu[3:5])
print(burger+coke-50)