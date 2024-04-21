# Part 1: Calculate average rainfall over a period of years

def get_numeric_input(prompt):
    """Function to get valid numeric input from the user."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def calculate_average_rainfall():
    """Function to calculate average rainfall."""
    total_rainfall = 0
    num_years = int(get_numeric_input("Enter the number of years: "))
    
    for year in range(1, num_years + 1):
        for month in range(1, 13):
            rainfall = get_numeric_input(f"Enter the inches of rainfall for Year {year}, Month {month}: ")
            total_rainfall += rainfall
    
    total_months = num_years * 12
    average_rainfall = total_rainfall / total_months
    
    print(f"Number of months: {total_months}")
    print(f"Total inches of rainfall: {total_rainfall}")
    print(f"Average rainfall per month: {average_rainfall:.2f} inches")

# Part 2: Calculate points awarded for book purchases

def calculate_points():
    """Function to calculate points awarded based on number of books purchased."""
    num_books = int(get_numeric_input("Enter the number of books purchased this month: "))
    
    if num_books >= 8:
        points = 60
    elif num_books >= 6:
        points = 30
    elif num_books >= 4:
        points = 15
    elif num_books >= 2:
        points = 5
    else:
        points = 0
    
    print(f"Points awarded: {points}")

# Main function to run the program

def main():
    """Main function to execute both parts of the program."""
    print("Part 1: Calculate average rainfall over a period of years")
    calculate_average_rainfall()
    
    print("\nPart 2: Calculate points awarded for book purchases")
    calculate_points()

if __name__ == "__main__":
    main()