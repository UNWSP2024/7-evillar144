# Program #3: US_Population

def main():
    # List to store the data (year, state, population)
    population_data = []

    # Loop to get user input
    while True:
        # Get year input
        year = input("Enter year (-1 to stop): ")
        if year == "-1":
            break  # Stop the loop if user enters -1

        # Get state and population input
        state = input("Enter state name: ")
        population = input("What is the population? ")

        # Convert year and population to integers before storing
        try:
            year = int(year)
            population = int(population)

            # Store the data in a list
            population_data.append([year, state, population])
        except ValueError:
            print("Invalid input. Please enter numeric values for year and population.")

    # Ask for a year to sum the total population
    try:
        year_to_check = int(input("\nEnter a year to get total population: "))
        sum_population_for_year(population_data, year_to_check)
    except ValueError:
        print("Invalid input. Please enter a valid year.")


def sum_population_for_year(data, year):
    # Variable to keep track of total population
    total = 0

    # Loop through the list and add populations for the given year
    for entry in data:
        if entry[0] == year:
            total += entry[2]

    # Print the result
    if total > 0:
        print(f"Total population for {year}: {total}")
    else:
        print(f"No data found for the year {year}.")


# Run the program
if __name__ == '__main__':
    main()
