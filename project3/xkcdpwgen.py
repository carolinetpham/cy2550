import argparse
import random

def run(args):
    words = args.words
    caps = args.caps
    numbers = args.numbers
    symbols = args.symbols

    with open('words.txt') as f:
        wordList = [word.strip() for word in f.readlines()]

    passwordWords = random.choices(wordList, k=words)
    if caps:
        passwordWords = [word.capitalize() for word in passwordWords]
    password = ''.join(passwordWords)

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

    def main():
        parser=argparse.ArgumentParser(description="Generate a secure, memorable password using the XKCD method")
        parser.add_argument("-w", "--words", help="include WORDS words in the password (default=4)", dest="words", type=int, default=4)
        parser.add_argument("-c", "--caps", help="capitalize the first letter of CAPS random words (default=0)", dest="caps", type=int, default=0)
        parser.add_argument("-n", "--numbers", help="insert NUMBERS random numbers in the password (default=0)", dest="numbers", type=int, default=0)
        parser.add_argument("-s", "--symbols", help="insert SYMBOLS random symbols in the password (default=0)", dest="symbols", type=int, default=0)
        parser.set_defaults(func=run)
        args=parser.parse_args()
        args.func(args)

    if __name__ == '__main__':
        main()

