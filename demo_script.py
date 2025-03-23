"""
demo_script.py - A very simple Python script to demonstrate basic features.

Date: January 2025
"""

#####################################
# Define main Function
#####################################

def main() -> None:
    """
    Main function to illustrate Python basics
    """
    print("Starting MAIN function.\n")
    print("Name Python files with lowercase and underscores.\n")
    print("In Python, comments start with a '#' symbol and are not executed.")
    print("  Comments can also be wrapped in triple single quotes or triple back tics.\n")

    print("Variables are used to store values.")
    print("  Type hints are optional, and recommended for clarity.")
    print("  example_number = 42")
    print("  count: int = 42")
    print("  temp_F: float = 42.2")
    print(' user_name: str = "Data Analyst"\n')

    example_number = 42
    count: int = 42
    temp_F: float = 42.2
    user_name: str = "Data Analyst"
    print(f"Result: {example_number=},{count=},{temp_F=},{user_name=}.\n")

    # Calling functions
    print("Functions in Python are blocks of reusable code.")
    print("You can call a function by using its name followed by parentheses.\n")

    print("We use f-strings to combine text and values in Python.")
    print("  Put the f immediately before the opening quote of the string text.\n")

    print("Python has many built-in functions, like min(), max(), len(), etc.")
    numbers = [1, 2, 3]
    minimum = min(numbers)
    maximum = max(numbers)
    count = len(numbers)
    print(f"For the list of numbers: {numbers}")
    print(f"  The minimum value is min(numbers): {minimum}")
    print(f"  The maximum value is max(numbers): {maximum}")
    print(f"  The length of the list is len(numbers): {count}\n")

    is_important: bool = True

    print(f"In Python, indentation matters = {is_important}!")
    print(f"In Python, spelling matters = {is_important}!")
    print(f"In Python, uppercase/lowercase matters = {is_important}!\n")

    print("Experiment with this demo script to learn the basics quickly.\n")

    # End the script
    print("Exiting MAIN function.")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    print("DEMO - Ready for work.")
    main()
    print("DEMO - Execution complete.")