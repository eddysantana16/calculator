# Professional Command-Line Calculator

This project is a professional-grade command-line calculator application developed in Python. It supports basic arithmetic operations with a REPL interface, maintains a history of calculations, and includes comprehensive error handling and testing.

## Features

- REPL interface for continuous user interaction.
- Supports addition, subtraction, multiplication, and division.
- Special commands: `help`, `history`, and `exit`.
- Input validation and comprehensive error handling.
- Maintains a history of calculations.
- 100% test coverage using `pytest` and `pytest-cov`.
- Continuous integration configured with GitHub Actions.

## Setup

## Clone the repository:

   git clone <https://github.com/eddysantana16/calculator.git>
   cd calculator
   
## Create and activate a virtual environment:

    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate

## Install dependencies:

    pip install -r requirements.txt

## Run the application:

    python main.py
        You'll see a welcome message and prompt to enter commands or operations.

            add – perform addition

            subtract – perform subtraction

            multiply – perform multiplication

            divide – perform division

            help – display available commands and operations

            history – show past calculations

            exit – quit the application

## Testing

    Run tests with coverage:

        pytest --cov=app tests/

## Project Structure
```
calculator/
├── app/
│   ├── calculator/
│   ├── calculation/
│   ├── operation/
├── tests/
├── .github/
│   └── workflows/
├── main.py
├── requirements.txt
├── README.md
├── pytest.ini
```

## Continuous Integration: 

GitHub Actions are configured to run tests and enforce 100% coverage on every push or pull request.

## License

MIT License

## Author

Eddy Santana