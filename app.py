
import ast

from flask import Flask, render_template, request

import target

app = Flask(__name__)

FUNCTIONS = {
    "is_adult": {
        "description": "Check whether a person is an adult.",
        "example": "(18,)",
    },
    "celsius_to_fahrenheit": {
        "description": "Convert Celsius to Fahrenheit.",
        "example": "(25,)",
    },
    "count_vowels": {
        "description": "Count vowels in a string.",
        "example": "('Hello World',)",
    },
    "invert": {
        "description": "Return the opposite of a boolean.",
        "example": "(True,)",
    },
    "greet": {
        "description": "Greet a person or the default guest.",
        "example": "('Mehedi',)",
    },
    "find_max": {
        "description": "Find the largest number in a list.",
        "example": "([10, 25, 7],)",
    },
    "get_price": {
        "description": "Find an item's price in a dictionary.",
        "example": "({'apple': 10, 'banana': 20}, 'apple')",
    },
    "swap": {
        "description": "Swap the positions of two values.",
        "example": "((10, 20),)",
    },
    "common_items": {
        "description": "Find common items in two sets.",
        "example": "({1, 2, 3}, {2, 3, 4})",
    },
    "is_leap_year": {
        "description": "Check whether a year is a leap year.",
        "example": "(2024,)",
    },
    "to_int": {
        "description": "Convert a value to an integer.",
        "example": "('42',)",
    },
    "divide": {
        "description": "Divide one number by another.",
        "example": "(10, 2)",
    },
    "power": {
        "description": "Raise a number to a power.",
        "example": "(2, 3)",
    },
    "square_root": {
        "description": "Calculate the square root of a number.",
        "example": "(25,)",
    },
    "factorial": {
        "description": "Calculate a number's factorial.",
        "example": "(5,)",
    },
    "average": {
        "description": "Calculate the average of a list.",
        "example": "([10, 20, 30],)",
    },
}


@app.route("/", methods=["GET", "POST"])
def index():
    selected_function = ""
    arguments = ""
    result = None
    error = None
    submitted = False

    if request.method == "POST":
        submitted = True
        selected_function = request.form.get("function", "")

        if selected_function not in FUNCTIONS:
            error = "Please select a valid function."
        else:
            arguments = request.form.get("arguments", "")

            try:
                parsed_arguments = ast.literal_eval(arguments)
            except (ValueError, SyntaxError) as exc:
                error = f"Input error: {exc}"
            else:
                if not isinstance(parsed_arguments, tuple):
                    error = (
                        "TypeError: Arguments must be entered as a Python tuple, "
                        "for example: (18,)"
                    )
                else:
                    try:
                        function = getattr(target, selected_function)
                        output = function(*parsed_arguments)
                        result = repr(output)
                    except Exception as exc:
                        error = f"{type(exc).__name__}: {exc}"

    return render_template(
        "index.html",
        functions=FUNCTIONS,
        selected_function=selected_function,
        arguments=arguments,
        result=result,
        error=error,
        submitted=submitted,
    )


@app.route("/health")
def health():
    return {"status": "ok"}, 200


if __name__ == "__main__":
    app.run(debug=False)
