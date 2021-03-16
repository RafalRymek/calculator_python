class Calculator:

    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        return x / y

    def choice_maker(self):
        print("**************************\nWelcome to the Calculator\n**************************")

        while True:
            user_input = input("Calculation (y) or quit (q) ")

            if user_input == "q":
                print("Bye!")
                break

            first_num = int(input("Enter first number: "))
            second_num = int(input("Enter second number: "))
            print(" 1. for ADDITION")
            print(" 2. for SUBTRACTION")
            print(" 3. for MULTIPLICATION")
            print(" 4. for DIVISION")

            choice = input("Please select operation: ")
            if choice == "1":
                print(Calculator.add(self, first_num, second_num))
            elif choice == "2":
                print(Calculator.subtract(self, first_num, second_num))
            elif choice == "3":
                print(Calculator.multiply(self, first_num, second_num))
            elif choice == "4":
                print(Calculator.divide(self, first_num, second_num))
            else:
                print("Something goes wrong, please try again")


if __name__ == "__main__":
    boot_calc = Calculator()
    boot_calc.choice_maker()
