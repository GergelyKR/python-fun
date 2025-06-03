# if __name__ == "__main__": (this script can be imported OR run standalone)
#                            Functions and classes in this module can be reused
#                            without the main block of code executing

# ex. library = Import library for functionality
#               When running library directly, display a help page

def some_function():
    print("This is a function.")

if __name__ == "__main__":
    print("This script is being run directly.")
    some_function()
else:
    print("This script is being imported as a module.")