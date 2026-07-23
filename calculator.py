print("Simple Calculator - Version 3")

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("\nEnter your choice (1/2/3/4): ")

num_count = int(input("How many numbers do you want to calculate? "))

numbers = []

for i in range(num_count):
    number = float(input(f"Enter number {i + 1}: "))
    numbers.append(number)

if choice == "1":
    result = sum(numbers)
    expression = " + ".join(str(num) for num in numbers)

elif choice == "2":
    result = numbers[0]
    expression = str(numbers[0])

    for num in numbers[1:]:
        result -= num
        expression += f" - {num}"

elif choice == "3":
    result = 1
    expression = ""

    for i, num in enumerate(numbers):
        result *= num

        if i == 0:
            expression = str(num)
        else:
            expression += f" * {num}"

elif choice == "4":
    result = numbers[0]
    expression = str(numbers[0])

    for num in numbers[1:]:
        if num == 0:
            print("Error: Cannot divide by zero")
            exit()

        result /= num
        expression += f" / {num}"

else:
    print("Invalid choice")
    exit()

print("\nCalculation:")
print(f"{expression} = {result}")