###################################################
# CS 22, Prof. Muldrow
# Name: Soliday Ek
# Assignment: Week 1 Homework
# Due Date: 10/1/2023
###################################################
import random
# Create a function to calculate the average steps for a month
def get_steps(monthName, daysPerMonth, stepFile):
    total_steps = 0

    startIndex = 0
    # I had used the match/case blocks to determine where my program should start to increment the total of steps from each individual months
  
    match monthName:
        case "January":
            startIndex = 0  # Start index of the month
        case "February":
            startIndex = 31  # Start index of the month
        case "March":
            startIndex = 59
        case "April":
            startIndex = 90
        case "May":
            startIndex = 120
        case "June":
            startIndex = 151
        case "July":
            startIndex = 181
        case "August":
            startIndex = 212
        case "September":
            startIndex = 243
        case "October":
            startIndex = 273
        case "November":
            startIndex = 304
        case "December":
            startIndex = 334
        case _:
            startIndex = 0  # Default case
# Open the file first and read the steps from certain index to another index. It depends on which month is it
    with open(stepFile, "r") as f:
        for i, line in enumerate(f):
            if i >= startIndex and i < startIndex + daysPerMonth:
                total_steps += int(line.strip())  # Convert to integer and accumulate steps

    average_steps = total_steps // daysPerMonth
    print(f"{monthName} had an average of {average_steps} steps.")

# Create an even-odd function that counts the number of even and odd numbers
def evensOdds(num):
    odd_count = 0
    even_count = 0

    num = int(num)
    if num % 2 == 0:
        print(str(num) + " is even")
        even_count += 1
    else:
        print(str(num) + " is odd")
        odd_count += 1

    return even_count, odd_count

def main():
    print('Program 1')
    # Open the file for writing
    with open("numbers.txt", "w+") as file:
        # Generate and write 10 random numbers using the randint()
        for _ in range(10):
            random_num = random.randint(1, 1000)
            # Convert the number to a string and add a newline character
            num_str = str(random_num) + '\n'
            file.write(num_str)
        file.close()
    
    # Open a file and read it only
    with open("numbers.txt", "r") as file:
        even_count = 0
        odd_count = 0
        for num in file:
            # Call evensOdds function and then pass each integer from the file
            even, odd = evensOdds(num)
            even_count += even   #this is how you take values and print from another function and into a different function
            odd_count += odd
        file.close()

    print(f"The file contains {even_count} even numbers and {odd_count} odd numbers.\n")
    print('Program 2')
    # program2 - download and read the 'step.txt' file
    stepFile = "steps.txt"
    
    # Call the get_steps function for each month
    get_steps('January', 31, stepFile)
    get_steps('February', 28, stepFile)
    get_steps('March', 31, stepFile)
    get_steps('April', 30, stepFile)
    get_steps('May', 31, stepFile)
    get_steps('June', 30, stepFile)
    get_steps('July', 31, stepFile)
    get_steps('August', 31, stepFile)
    get_steps('September', 30, stepFile)
    get_steps('October', 31, stepFile)
    get_steps('November', 30, stepFile)
    get_steps('December', 31, stepFile)

# I put this in order for the program to check if this script is run as the main program
if __name__ == "__main__":
    main()
