# app.py

print("Hello, Jenkins!")

unused_variable = 123        # Pylint warning: unused variable
x = "1" + 2                  # Mypy type warning: incompatible types
def f():
    pass                      # Flake8 may complain if style rules broken
