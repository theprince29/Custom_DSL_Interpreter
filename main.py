def get_value(token, memory):
    if token.lstrip("-").isdigit():
        return int(token)
    return memory.get(token, 0)

def custom_dsl_interpreter(commands):
    memory = {}
    output = []
    errors = []
    executing = [True]

    for line_no, line in enumerate(commands, start=1):
        tokens = line.strip().split()

        if not tokens:
            continue

        command = tokens[0]

        try:
            # === IF Condition ===
            if command == "IF":
                if len(tokens) < 5 or tokens[4] != "THEN":
                    raise SyntaxError("Invalid IF syntax. Use: IF x > y THEN")
                var1, op, var2 = tokens[1], tokens[2], tokens[3]
                val1 = get_value(var1, memory)
                val2 = get_value(var2, memory)

                if op == ">":
                    condition = val1 > val2
                elif op == "<":
                    condition = val1 < val2
                elif op == "==":
                    condition = val1 == val2
                elif op == "!=":
                    condition = val1 != val2
                elif op == ">=":
                    condition = val1 >= val2
                elif op == "<=":
                    condition = val1 <= val2
                else:
                    raise ValueError(f"Unknown operator '{op}' in IF condition")

                executing.append(condition and executing[-1])

            elif command == "ENDIF":
                if len(tokens) != 1:
                    raise SyntaxError("ENDIF should not have arguments")
                if len(executing) > 1:
                    executing.pop()
                else:
                    raise RuntimeError("ENDIF without matching IF")

            elif executing[-1]:  # Only run commands if currently executing
                if command == "SET":
                    if len(tokens) != 3:
                        raise SyntaxError("SET syntax: SET var value")
                    var, val_token = tokens[1], tokens[2]
                    memory[var] = get_value(val_token, memory)

                elif command in ("ADD", "SUB", "MUL", "DIV", "MOD"):
                    if len(tokens) != 3:
                        raise SyntaxError(f"{command} syntax: {command} var value")
                    var, val_token = tokens[1], tokens[2]
                    val = get_value(val_token, memory)

                    if command == "ADD":
                        memory[var] = memory.get(var, 0) + val
                    elif command == "SUB":
                        memory[var] = memory.get(var, 0) - val
                    elif command == "MUL":
                        memory[var] = memory.get(var, 0) * val
                    elif command == "DIV":
                        if val == 0:
                            raise ZeroDivisionError("Division by zero")
                        memory[var] = memory.get(var, 0) // val
                    elif command == "MOD":
                        if val == 0:
                            raise ZeroDivisionError("Modulo by zero")
                        memory[var] = memory.get(var, 0) % val

                elif command == "PRINT":
                    if len(tokens) != 2:
                        raise SyntaxError("PRINT syntax: PRINT var")
                    var = tokens[1]
                    output.append(str(get_value(var, memory)))

                else:
                    raise ValueError(f"Unknown command '{command}'")

        except Exception as e:
            errors.append(f"[Line {line_no}] Error: {e}")

    # Optionally print errors
    if errors:
        print("Errors detected:")
        for err in errors:
            print(err)

    return output
