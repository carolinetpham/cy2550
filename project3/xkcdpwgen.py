#!/usr/bin/python3
import argparse
import random

# Generate a password using the XKCD method
def run(args):
    words = args.words
    caps = args.caps
    numbers = args.numbers
    symbols = args.symbols
    # Read in the word list
    with open('words.txt') as f:
        wordList = [word.strip() for word in f.readlines()]
    # Generate the password
    passwordWords = random.choices(wordList, k=words)
    # Capitalize random words
    if caps:
        passwordWords = [word.capitalize() for word in passwordWords]
    password = ''.join(passwordWords)
    # Insert numbers and symbols
    if numbers:
        for i in range(numbers):
            position = random.randint(0, len(password))
            password = password[:position] + str(random.randint(0, 9)) + password[position:]

    if symbols:
        symbolList = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', ';', ':', '<', '>', ',', '.', '?', '/']
        for i in range(symbols):
            position = random.randint(0, len(password))
            password = password[:position] + random.choice(symbolList) + password[position:]

    return password

# Run the program
def main():
    parser = argparse.ArgumentParser(description='Generate a secure, memorable password using the XKCD method')
    parser.add_argument('-w', '--words', type=int, default=4, help='include WORDS words in the password (default: 4)')
    parser.add_argument('-c', '--caps', type=int, default=0, help='capitalize the first letter of CAPS random words (default: 0)')
    parser.add_argument('-n', '--numbers', type=int, default=0, help='insert NUMBERS random numbers in the password (default: 0)')
    parser.add_argument('-s', '--symbols', type=int, default=0, help='insert SYMBOLS random symbols in the password (default: 0)')
    args = parser.parse_args()

    password = run(args)
    # Print the passworrd
    print(password)
    return password

if __name__ == '__main__':
    main()
