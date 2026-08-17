def kilometers_to_miles():
    kilometers = float(input("Enter kilometers: "))
    miles = kilometers * 0.621371
    print(f"{kilometers} km = {miles:.2f} miles")


def miles_to_kilometers():
    miles = float(input("Enter miles: "))
    kilometers = miles * 1.60934
    print(f"{miles} miles = {kilometers:.2f} km")


def kilograms_to_pounds():
    kilograms = float(input("Enter kilograms: "))
    pounds = kilograms * 2.20462
    print(f"{kilograms} kg = {pounds:.2f} pounds")


def pounds_to_kilograms():
    pounds = float(input("Enter pounds: "))
    kilograms = pounds * 0.453592
    print(f"{pounds} pounds = {kilograms:.2f} kg")


def celsius_to_fahrenheit():
    celsius = float(input("Enter Celsius: "))
    fahrenheit = (celsius * 9 / 5) + 32
    print(f"{celsius}°C = {fahrenheit:.2f}°F")


def fahrenheit_to_celsius():
    fahrenheit = float(input("Enter Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5 / 9
    print(f"{fahrenheit}°F = {celsius:.2f}°C")


def main():
    while True:
        print("\n===== Unit Converter =====")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Kilograms to Pounds")
        print("4. Pounds to Kilograms")
        print("5. Celsius to Fahrenheit")
        print("6. Fahrenheit to Celsius")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            kilometers_to_miles()

        elif choice == "2":
            miles_to_kilometers()

        elif choice == "3":
            kilograms_to_pounds()

        elif choice == "4":
            pounds_to_kilograms()

        elif choice == "5":
            celsius_to_fahrenheit()

        elif choice == "6":
            fahrenheit_to_celsius()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()