from random import randint
import sys, getopt

words = 4
capitals = 0
numbers = 0
symbols = 0
specialChar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

try:
    opts, args = getopt.getopt(sys.argv[1:], "hw:c:n:s:", ["help", "words=", "capitals=", "numbers=", "symbols="])
except getopt.GetoptError:
    print("Usage: xkcdpwgen [-h] [-w WORDS] [-c CAPITALS] [-n NUMBERS] [-s SYMBOLS]")
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-h", "--help"):
        print("Usage: xkcdpwgen [-h] [-w WORDS] [-c CAPITALS] [-n NUMBERS] [-s SYMBOLS]")
        print("Generates a password using the XKCD method.")
        print("Options:")
        print("  -h, --help\t\t\tShow this help message and exit.")
        print("  -w, --words\t\t\tNumber of words in the password. Default is 4.")
        print("  -c, --capitals\t\tNumber of words to capitalize. Default is 0.")
        print("  -n, --numbers\t\t\tNumber of numbers to add to the end of the password. Default is 0.")
        print("  -s, --symbols\t\t\tNumber of symbols to add to the end of the password. Default is 0.")
        sys.exit()
    elif opt in ("-w", "--words"):
        words = int(arg)
    elif opt in ("-c", "--capitals"):
        capitals = int(arg)
    elif opt in ("-n", "--numbers"):
        numbers = int(arg)
    elif opt in ("-s", "--symbols"):
        symbols = int(arg)

with open("wordlist.txt") as f:
    wordlist = f.read().splitlines()

password = ""
for i in range(words):
    x = randint(0, len(wordlist) - 1)
    temp = wordlist[x]
    if capitals >= (words - i):
        temp = temp[0].upper() + temp[1:]
    elif capitals > 0:
        if randint(0, 1) == 1:
            temp = temp[0].upper() + temp[1:]
            capitals -= 1
    password += temp

for j in range(numbers):
    x = randint(0, len(password) - 1)
    password = password[:x] + str(randint(0, 9)) + password[x:]

for k in range(symbols):
    x = randint(0, len(password) - 1)
    password = password[:x] + specialChar[randint(0, len(specialChar) - 1)] + password[x:]

print(password)
