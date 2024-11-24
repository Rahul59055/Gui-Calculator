# Scientific Calculator

This is a Python-based scientific calculator built using the `Tkinter` library for the graphical user interface (GUI) and the `math` module for mathematical operations. The calculator supports basic arithmetic operations as well as advanced functions like square root, logarithms, exponentials, factorial, and more.

## Features

- **Basic Arithmetic Operations**: Addition, subtraction, multiplication, and division.
- **Advanced Mathematical Functions**:
  - Square root (`sqrt`)
  - Factorial (`!`)
  - Exponentiation (`^`)
  - Exponential function (`exp`)
  - Logarithms (base 10 and natural log)
  - Pi constant insertion (`pi`)
- **Error Handling**: Displays "Error" for invalid operations.
- **Clear and Delete Functions**: Clear the entry or delete the last character.

## Requirements

- Python 3.x
- `Tkinter` library (usually included with Python)
- `math` module (usually included with Python)

## Installation

1. Install Python from the [official website](https://www.python.org/downloads/) if not already installed.
2. The `Tkinter` and `math` modules are included with Python, so no separate installation is needed.

## Usage

### GUI Overview:

- **Display Screen**: A large entry field at the top of the window to show the current expression and results.
- **Buttons**:
  - The calculator includes buttons for numbers (0-9), decimal point (`.`), operators (`+`, `-`, `*`, `/`), and special functions like `sqrt`, `log`, `ln`, `exp`, `^` (power), and `!` (factorial).
  - The `C` button clears the current expression.
  - The `del` button deletes the last character.
  - The `=` button evaluates and displays the result.
  - The `pi` button inserts the mathematical constant π.

### Functions:

- **Button Click**: When a number or operator button is clicked, it appends the respective value to the current expression in the display.
- **Evaluate Expression (`=`)**: This button evaluates the entered expression and displays the result. It uses Python’s built-in `eval()` function, which safely processes mathematical expressions.
- **Clear Entry (`C`)**: Clears the current expression.
- **Delete Last (`del`)**: Deletes the last character from the current expression.
- **Square Root (`sqrt`)**: Computes the square root of the entered number.
- **Factorial (`!`)**: Computes the factorial of the entered integer.
- **Exponentiation (`^`)**: Allows raising a number to a power.
- **Exponential (`exp`)**: Computes e^x where e is the base of the natural logarithm.
- **Logarithms**:
  - **Logarithm base 10 (`log`)**
  - **Natural Logarithm (`ln`)**

## Example:

1. Press `7`, `+`, `3`, and `=` to compute `7 + 3`, which will display `10` in the result area.
2. Press `5`, `^`, `2`, and `=` to compute `5^2`, which will display `25`.
3. Press `sqrt`, then enter a number (e.g., `25`), and it will display `5` for the square root of `25`.

## License

This project is open-source and licensed under the MIT License. You are free to use, modify, and distribute this code.

## Author

Created by [Your Name]. 

## Acknowledgements

- Python programming language
- Tkinter library for building the GUI
- `math` module for mathematical functions
