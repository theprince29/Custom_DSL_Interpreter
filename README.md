
> ### Compumatrice inc. #2 Coding Challenge Problem 

```bash Problem 2: Custom DSL Interpreter with Memory
Build an interpreter for a mini programming language with commands like SET, ADD, MUL, PRINT, IF.

Input: List of strings
Output: List of printed values

Example:
[
 "SET x 2",
 "SET y 3",
 "IF y > x THEN",
 " ADD x 1",
 " PRINT x",
 "ENDIF"
]

Output: ["3"] 
```


# Custom DSL Interpreter

This project is a custom-built DSL interpreter made in Python. It lets users write and run scripts in a simple, task-specific language that’s easy to understand and use for particular purposes.

## Features

- Parse and execute custom DSL scripts
- Extensible command set
- Error handling and reporting
- Easy integration with other Python projects

## Getting Started

1. **Clone the repository:**
    ```bash
    git clone https://github.com/theprince29/Custom_DSL_Interpreter.git
    cd Custom_DSL_Interpreter
    ```


3. **Run the interpreter:**
    ```bash
    python run.py 
    ```

## Usage

Write your DSL command in run.py Example:
```bash
commands_0 = [
    "SET age 20",
    "IF age >= 18 THEN",
    " PRINT 1",
    "ENDIF",
    "IF age < 18 THEN",
    " PRINT 0",
    "ENDIF"
]   
```

Then run:
```bash
python run.py
```

