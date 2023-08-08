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
    print("Usage: xkcdpwgen.py [-w <words>] [-c <capitals>] [-n <numbers>] [-s <symbols>]")
    sys.exit(2)
for opt, arg in opts:
    if opt in ("-h", "--help"):
        print("Usage: xkcdpwgen.py [-w <words>] [-c <capitals>] [-n <numbers>] [-s <symbols>]")
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
    wordlist = f.readlines()

password = ""
for i in range(words):
    password += wordlist[randint(0, len(wordlist)-1)].strip()
    if i != words-1:
        password += " "
    if capitals > 0:
        password = password.capitalize()
        capitals -= 1
    elif capitals < 0:
        password = password.lower()
        capitals += 1
    if numbers > 0:
        password += str(randint(0, 9))
        numbers -= 1
    if symbols > 0:
        password += specialChar[randint(0, len(specialChar)-1)]
        symbols -= 1
print(password)
