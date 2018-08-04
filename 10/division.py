print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input('\nFirst number: ')
    if first_number == 'q':
        break
    secend_number = input('Second number: ')
    if secend_number == 'q':
        break
    try:
        answer = int(first_number) / int(secend_number)
    except ZeroDivisionError:
        print("You can't divide by 0!")
    else:
        print(answer)
