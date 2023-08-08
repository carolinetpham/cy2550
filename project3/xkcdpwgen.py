from random import randint
import sys, getopt

# Default values
words = 4
caps = 0
numbers = 0
symbols = 0
specialChar = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']

# Get command line arguments
try:
    opts, args = getopt.getopt(sys.argv[1:], "hw:c:n:s:", ["help", "words=", "capitals=", "numbers=", "symbols="])
except getopt.GetoptError:
    print("Usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]")
    sys.exit(2)

# Parse command line arguments
for opt, arg in opts:
    if opt in ("-h", "--help"):
        # Proper format:
        print("usage: xkcdpwgen [-h] [-w WORDS] [-c CAPS] [-n NUMBERS] [-s SYMBOLS]\n\n" +
              "Generate a secure, memorable password using the XKCD method\n\n" +
              "optional arguments:\n" +
              "    -h, --help            show this help message and exit\n" +
              "    -w WORDS, --words WORDS\n" +
              "                          include WORDS words in the password (default=4)\n" +
              "    -c CAPS, --caps CAPS  capitalize the first letter of CAPS random words\n" +
              "                          (default=0)\n" +
              "    -n NUMBERS, --numbers NUMBERS\n" +
              "                          insert NUMBERS random numbers in the password\n" +
              "                          (default=0)\n" +
              "    -s SYMBOLS, --symbols SYMBOLS\n" +
              "                          insert SYMBOLS random symbols in the password\n" +
              "                          (default=0)")
        sys.exit()
    # Set values based on command line arguments
    elif opt in ("-w", "--words"):
        words = int(arg)
    elif opt in ("-c", "--caps"):
        capitals = int(arg)
    elif opt in ("-n", "--numbers"):
        numbers = int(arg)
    elif opt in ("-s", "--symbols"):
        symbols = int(arg)
# Check for invalid arguments
with open("wordlist.txt") as f:
    wordlist = f.read().splitlines()

# Generate password
password = ""

# Add words
for i in range(words):
    x = randint(0, len(wordlist) - 1)
    temp = wordlist[x]
    if caps >= (words - i):
        temp = temp[0].upper() + temp[1:]
    elif caps > 0:
        if randint(0, 1) == 1:
            temp = temp[0].upper() + temp[1:]
            caps -= 1
    password += temp

# Add numbers and symbols
for j in range(numbers):
    x = randint(0, len(password) - 1)
    password = password[:x] + str(randint(0, 9)) + password[x:]

for k in range(symbols):
    x = randint(0, len(password) - 1)
    password = password[:x] + specialChar[randint(0, len(specialChar) - 1)] + password[x:]

# Print password
print(password)
