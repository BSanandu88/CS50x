#Credit
#Implement a program that determines whether a provided credit card number is valid according to Luhn’s algorithm.

#$ python credit.py
#Number: 378282246310005
#AMEX
#Specification
#In credit.py in ~/pset6/credit/, write a program that prompts the user for a credit card number and then reports (via print) whether it is a valid American Express, MasterCard, or Visa card number, exactly as you did in Problem Set 1, except that your program this time should be written (a) in Python and (b) in CS50 IDE.
#So that we can automate some tests of your code, we ask that your program’s last line of output be AMEX\n or MASTERCARD\n or VISA\n or INVALID\n, nothing more, nothing less.
#For simplicity, you may assume that the user’s input will be entirely numeric (i.e., devoid of hyphens, as might be printed on an actual card).
#Best to use get_int or get_string from CS50’s library to get users’ input, depending on how you to decide to implement this one.
#Usage
#Your program should behave per the example below.

#$ python credit.py
#Number: 378282246310005
#AMEX
#Testing
#No check50 for this problem, but be sure to test your code for each of the following.

#Run your program as python credit.py, and wait for a prompt for input. Type in 378282246310005 and press enter. Your program should output AMEX.
#Run your program as python credit.py, and wait for a prompt for input. Type in 371449635398431 and press enter. Your program should output AMEX.
#Run your program as python credit.py, and wait for a prompt for input. Type in 5555555555554444 and press enter. Your program should output MASTERCARD.
#Run your program as python credit.py, and wait for a prompt for input. Type in 5105105105105100 and press enter. Your program should output MASTERCARD.
#Run your program as python credit.py, and wait for a prompt for input. Type in 4111111111111111 and press enter. Your program should output VISA.
#Run your program as python credit.py, and wait for a prompt for input. Type in 4012888888881881 and press enter. Your program should output VISA.
#Run your program as python credit.py, and wait for a prompt for input. Type in 1234567890 and press enter. Your program should output INVALID.#


from cs50 import get_int
from math import floor

def main():
	digit1 = 0
	digit2 = 0
	num_digits = 0
	sum_of_double_odds = 0
	sum_of_evens = 0
	cc_number = get_int("Number: ")


	while cc_number > 0:
		digit2 = digit1
		digit1 = cc_number%10


		if num_digits % 2==0:
			sum_of_evens += digit1
		else:
			multiple = 2*digit1
			sum_of_double_odds += (multiple//10) + (multiple %10)



		cc_number //=10
		num_digits += 1

	is_valid == 4 and num_digits >= 13 and num_digits <= 16 and is_valid:
        print("VISA\n")
    elif first_two_digits >= 51 and first_two_digits <= 55 and num_digits == 16 and is_valid:
        print("MASTERCARD\n")
    elif (first_two_digits == 34 or first_two_digits == 37) and num_digits == 15 and is_valid:
        print("AMEX\n")
    else:
        print("INVALID\n")

if __name__ == "__main__":
    main()
