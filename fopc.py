from pyparsing import Word, alphas, infixNotation, Literal

# Define the basic elements
variable = Word(alphas, exact=1)
operand = variable | Literal("True") | Literal("False")
operators = [
    ("not", 1, 1, "right"),
    ("and", 2, 2, "left"),
    ("or", 2, 2, "left"),
]

# Define the grammar using infix notation
expression = infixNotation(
    operand,
    operators,
)

# Parse FOPC expression
def parse_fopc(expression_str):
    try:
        result = expression.parseString(expression_str)[0]
        return result
    except Exception as e:
        print(f"Error parsing expression: {e}")
        return None

# Example usage
expression_str = "P and (Q or R)"
parsed_result = parse_fopc(expression_str)

if parsed_result is not None:
    print(f"Original Expression: {expression_str}")
    print(f"Parsed Result: {parsed_result}")
