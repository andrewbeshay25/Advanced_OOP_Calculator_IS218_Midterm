# Advanced OOP Calculator (IS218 Midterm)

## Project Overview
Welcome to my advanced OOP Calculator! This isn't your everyday calculator—sure, it handles basic operations like addition, subtraction, multiplication, and division, but it goes beyond that. This calculator keeps a detailed log of every action and operation performed, stores a session-long history, and saves all executed operations to a CSV file for easy post-session access. 

### Instruction Video
Watch the setup and usage guide **[here](<YouTube URL>)**.

### Technical Highlights
This project is built to demonstrate advanced object-oriented programming concepts, featuring unit testing and GitHub Actions to enforce code quality. Sensitive configurations are managed using environment variables, adding a layer of security and flexibility to the program. 

## Key Program Functionalities

### 1. Object-Oriented Structure
The calculator is built with a robust OOP architecture, leveraging Python classes and modules to encapsulate functionality. The main components include:
- **Calculation classes** for each arithmetic operation (Addition, Subtraction, etc.)
- **`Calculator` class** to execute operations.
- **`HistoryManager` and `CsvManager` classes** to manage session history and persistent data.

### 2. Factory Methods & Strategy Design Pattern
This project uses the **Factory Method** and **Strategy Design Pattern** to handle different calculations dynamically:
- The **Factory Method** enables creating instances of various operation classes (e.g., `Addition`, `Subtraction`) at runtime.
- The **Strategy Pattern** allows the calculator to switch between different operations seamlessly without hardcoding behavior.

### 3. REPL Interface
The program features a **REPL (Read-Eval-Print Loop)** interface that provides an interactive user experience:
- Users can input commands like `add 3 4` or `multiply 5 6` directly in the console.
- Other REPL commands include viewing operation history, clearing history, and exiting the calculator.

### 4. Logging
This calculator uses Python’s logging module to capture a detailed log of every operation and event:
- Logs are saved to a file specified by an environment variable for convenient reference.
- Logging occurs across the program, from file creation to user commands, providing transparency and traceability.

### 5. Environment Variables
Environment variables are used to manage configurations, such as:
- The path to the logging file and CSV file.
- This setup keeps sensitive information out of the codebase, aligning with best practices.

### 6. Data Persistence with Pandas and CSV
The **CsvManager** class integrates **Pandas** to handle reading and writing operations to a CSV file, enabling persistent storage of calculator history:
- Each operation performed in a session is appended to `operations_log.csv`, with columns for `operation`, `a`, `b`, and `result`.
- This file is accessible after the session ends, making it easy to review past calculations.

### 7. Unit Testing & GitHub Actions
Unit testing is implemented throughout the project to ensure code quality and functionality:
- **`pytest`** is used to test each functionality, from basic calculations to file handling.
- **GitHub Actions** automatically run these tests for each pull request, ensuring only validated code is merged into the main branch.

### Code Structure

```plaintext
├── app
│   ├── calculation.py         # Defines calculation classes
│   ├── calculator.py          # Core calculator logic
│   ├── history_manager.py     # Manages session history
│   
├── tests
│   ├── test_calculator.py     # Tests for Calculator functionality
│   ├── test_file_manager.py   # Tests for file management and logging
│   ├── test_csv_manager.py    # Tests for CSV read/write functionality
├── data
|   ├── csv_manager.py         # Manages CSV operations (data persistence)
├── main.py                    # Entry point with REPL interface and logging setup
├── requirements.txt           # Project dependencies
└── .env                       # Environment variable configurations
```

### Example Usage
Start the REPL interface by running:
```code
python main.py
```
Example commands within the REPL:
- ```add 3 5``` – Adds 3 and 5, displaying and logging the result.
- ```history``` – Shows all operations performed in the current session.
- ```clear``` – Clears the operation history for the session.
