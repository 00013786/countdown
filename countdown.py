try:

    number = int(input("Enter random number: "))


    def countup(n):
        if n == 0:

            print('Blastoff!')

        else:

            print(n)

            countup(n + 1)


    def countdown(n):
        if n <= 0:

            print('Blastoff!')

        else:

            print(n)

            countdown(n - 1)


    if number > 0:
        countdown(number)
    elif number < 0:
        countup(number)
    else:
        print("you entered zero")

except ValueError:
    print("ValueError Please Enter Valid Number")