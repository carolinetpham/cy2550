import argparse
import random

def generatePwrd(words, capital, number, special):
    # opens the file and reads the words
    with open('words.txt', 'r') as f:
        wrdList = [word.strip() for word in f.readlines()]

    pwdWords = random.choices(wrdList, k=words)
    if capital:
        pwdWords = [word.capitalize() for word in pwdWords]
    password = ''.join(pwdWords)
    # if number is true, add a random number to the password
    if number > 0:
        for _ in range(number):
            position = random.randint(0, len(password))
            password = password[:position] + str(random.randint(0, 9)) + password[position:]
    # if special is true, add a random special character to the password
    if special > 0:
        for _ in range(special):
            position = random.randint(0, len(password))
            password = password[:position] + random.choice('!@#$%^&*()') + password[position:]

    return password

# main function
def main():
    parser = argparse.ArgumentParser(description='Generate a password using xkcd style')
    parser.add_argument('-w', '--words', type=int, default=4, help='Number of words to use in the password')
    parser.add_argument('-c', '--capital', action='store_true', help='Capitalize the first letter of each word')
    parser.add_argument('-n', '--number', type=int, default=0, help='Add a random number to the password')
    parser.add_argument('-s', '--special', type=int, default=0, help='Add a random special character to the password')
    args = parser.parse_args()

    print(generatePwrd(args.words, args.capital, args.number, args.special))

# if the file is run directly, run the main function
if __name__ == '__main__':
    main()