from functionalities import add, sub, mul, div, floor_div, mod, expo

def main():
    print('Welcome to Terminal based simple calculator app')
    while True:
        input1 = input('Enter first number: ')
        input2 = input('Enter second number: ')
        
        try:
            # Convert inputs to numbers
            input1 = float(input1)
            input2 = float(input2)
        except ValueError:
            print("Please enter valid numbers.")
            continue
        
        operation = input('Choose operation to perform (+, -, *, /, //, %, **): ')
        
        if operation == '+':
            print(f'Result of {input1} and {input2} is: {add(input1, input2)}')
        elif operation == '-':
            print(f'Result of {input1} and {input2} is: {sub(input1, input2)}')
        elif operation == '*':
            print(f'Result of {input1} and {input2} is: {mul(input1, input2)}')
        elif operation == '/':
            print(f'Result of {input1} and {input2} is: {div(input1, input2)}')
        elif operation == '//':
            print(f'Result of {input1} and {input2} is: {floor_div(input1, input2)}')
        elif operation == '%':
            print(f'Result of {input1} and {input2} is: {mod(input1, input2)}')
        elif operation == '**':
            print(f'Result of {input1} and {input2} is: {expo(input1, input2)}')
        else:
            print("Invalid operation. Exiting.")
            break


if __name__ == '__main__':
    main()