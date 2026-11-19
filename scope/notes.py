# **Local Variable vs Global Variable**

# | Local Variable                                     | Global Variable                                           |
# | -------------------------------------------------- | --------------------------------------------------------- |
# | Declared inside a function.                        | Declared outside all functions.                           |
# | Accessible within its local scope.                 | Accessible throughout its module, subject to scope rules. |
# | Created when the function executes.                | Created when the module-level assignment executes.        |
# | Normally cannot be accessed outside its function.  | Can be accessed inside and outside functions.             |
# | Exists in the function's local scope.              | Exists in the module's global scope.                      |
# | Used for temporary operations.                     | Used for values shared across functions.                  |
# | Does not require a special keyword for assignment. | Requires `global` when assigning to it inside a function. |

# **Scope**

# | Scope     | Meaning                                                      |
# | --------- | ------------------------------------------------------------ |
# | Local     | Inside the current function.                                 |
# | Enclosing | Inside the outer function.                                   |
# | Global    | At the module/program level.                                 |
# | Built-in  | Predefined Python names such as `len()`, `print()`, `sum()`. |
# encolsing scope is occerd when the function is defind inside another fuction
