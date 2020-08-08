def menu(*args):
    while True:
        choices = '/'.join(args)

        choice = raw_input("Enter a choice ({0}): ".format(choices))

        if choice in args:
            return choice
