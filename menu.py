def menu(*args):
    while True:
        choice = raw_input("Enter a choice: ")

        if choice in args:
            return choice
