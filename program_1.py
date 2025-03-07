# Program #1: Rainfall
# Design a program that lets the user enter the total rainfall for each of 12 months into a list.
# The program should calculate and display the total rainfall for the year,
# the average monthly rainfall, # and the months with the highest and lowest amounts.
def rainfalls():
    rainfall = []  # List to store monthly rainfall data

    for i in range(1, 13):
        q_rain = int(input(f"What is the total rainfall amount of month {i}: "))
        rainfall.append(q_rain)

    total_rainfall = sum(rainfall)
    average_rainfall = total_rainfall / 12
    max_rainfall = max(rainfall)
    min_rainfall = min(rainfall)
    max_month = rainfall.index(max_rainfall) + 1
    min_month = rainfall.index(min_rainfall) + 1

    print(f"Total rainfall: {total_rainfall}")
    print(f"Average monthly rainfall: {average_rainfall:.2f}")
    print(f"Month {max_month} had the highest rainfall: {max_rainfall}")
    print(f"Month {min_month} had the lowest rainfall: {min_rainfall}")

rainfalls()


