def problem_two():
    numbers = (1, 4, 7, 10, 13, 16)
    sum_of_even = 0
    
    for x in numbers:
        if x % 2 == 0:
            sum_of_even += x
    
    average = sum_of_even / len(numbers)
    print(f'The average of even numbers in the tuple is {average:.2f}')

def divider():
    print("=" * 50)
    print()

def main():
    divider()
    problem_two()

if __name__ == "__main__":
    main()
