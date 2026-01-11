n = int(input())    # the number of improvements since you were frozen.
k = int(input())    # the number of improvements the game receives every year

start_year = 2022

change_years = n // k

print(start_year  + change_years)