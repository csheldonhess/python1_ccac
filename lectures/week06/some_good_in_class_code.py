def get_input():
    user_input = input("Give me a number: ")
    return user_input

def is_greater(value_a, value_b):
    """checks if the first parameter is greater than the second; returns a Boolean """
    if value_a > value_b:
        return True
    else:
        return False

# do we want to talk about any of the shortcuts I took there?
# like why there wasn't an else?

def main():
    a = get_input()
    b = get_input()
    if is_greater(a, b):
        print(a, ">", b)
    else:
        print(a, "<=", b)
        
        
main()