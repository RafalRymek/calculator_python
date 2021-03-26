class Calculator:

    def __init__(self):
        pass

    @staticmethod
    def add(x, y):
        if x is not None and y is not None:
            return x + y
        elif x is not None:
            return x
        elif y is not None:
            return y
        return 0

    @staticmethod
    def subtract(x, y):
        return x - y

    @staticmethod
    def multiply(x, y):
        return x * y

    @staticmethod
    def divide(x, y):
        if y == 0:
            return "Validation error. You can’t divide by 0…"
        else:
            return round((x / y), 3)

    @staticmethod
    def choice_maker():
        print("**************************\nWelcome to the Calculator\n**************************")

        while True:
            user_input = input("Calculation (y) or quit (q) ")

            if user_input == "q":
                print("Bye!")
                break

            first_num = float(input("Enter first number: "))
            second_num = float(input("Enter second number: "))
            print(" 1. for ADDITION")
            print(" 2. for SUBTRACTION")
            print(" 3. for MULTIPLICATION")
            print(" 4. for DIVISION")

            choice = input("Please select operation: ")
            if choice == "1":
                print(Calculator.add(first_num, second_num))
            elif choice == "2":
                print(Calculator.subtract(first_num, second_num))
            elif choice == "3":
                print(Calculator.multiply(first_num, second_num))
            elif choice == "4":
                print(Calculator.divide(first_num, second_num))
            else:
                print("Something goes wrong, please try again")


if __name__ == "__main__":
    boot_calc = Calculator()
    boot_calc.choice_maker()
