def get_integer_input(message):
    try:
        value = int(input(message))
        return value
    except ValueError:
        print("Invalid number.")
        return None