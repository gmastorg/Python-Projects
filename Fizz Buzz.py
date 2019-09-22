"""
Gabriela Canjura
Fizz Buzz
prints numbers 1-20 for multiples of 3 prints fizz
for multiples of 5 prints buzz for multiples of both
prints fizz buzz
"""

def main():

    i = 1 # counter to keep track of number

    while i <= 20:
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
main()
