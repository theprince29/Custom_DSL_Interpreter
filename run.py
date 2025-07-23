from main import custom_dsl_interpreter as interpreter

commands_0 = [
    "SET age 20",
    "IF age >= 18 THEN",
    " PRINT 1",
    "ENDIF",
    "IF age < 18 THEN",
    " PRINT 0",
    "ENDIF"
]   

commands_1 = [
 "SET x 2",
 "SET y 3",
 "IF y > x THEN",
 " DIV x y",
 " PRINT x",
 "ENDIF",
 "SET x z"
]

commands_2 = ["SET x y"]
# print(interpreter(commands_0))  # Output: ['1']
print(interpreter(commands_2))  # Output: ['3']

