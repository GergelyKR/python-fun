# It allows a script to be both reusable as a module (importable by other scripts) and executable (run directly for testing or standalone use).
# It helps separate the library code (functions, classes) from the script code (execution logic).
# It prevents certain code (like tests or demo code) from running when the file is imported.

def some_function():
    print("This is a function.")

if __name__ == "__main__":
    print("This script is being run directly.")
    some_function()
else:
    print("This script is being imported as a module.")