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
        print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]\n\n" +
              "Generate a secure, memorable password using the XKCD method\n\n" +
              "Optional args:\n" +
              "    -h, --help            Show this help message and exit\n" +
              "    -w WORDS, --words WORDS\n" +
              "                          Include WORDS words in the password (default=4)\n" +
              "    -c CAPS, --caps CAPS  Capitalize the first letter of CAPITALS random words\n" +
              "                          (default=0)\n" +
              "    -n NUMBERS, --numbers NUMBERS\n" +
              "                          Insert NUMBERS random numbers in the password\n" +
              "                          (default=0)\n" +
              "    -s SYMBOLS, --symbols SYMBOLS\n" +
              "                          Insert SYMBOLS random symbols in the password\n" +
              "                          (default=0)")
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
