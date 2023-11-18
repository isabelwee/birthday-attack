#! /usr/bin/env python3
from hashlib import sha256
import sys

LAST_DIGIT = 63

def main():
    # hash the two texts
    # if they aren't the same and the end, add a space to the end of fake
    # hash the two file
    if (len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} <number of digits to match>", file=sys.stderr)
        sys.exit(1)
        
    with open("fake.txt", "rb") as fake:
        fakeText = fake.read()
    with open("real.txt", "rb") as real:
        realText = real.read()
    
    numSpaces = 0

    i = LAST_DIGIT
    while True:
        fakeHash = sha256(fakeText).hexdigest()
        realHash = sha256(realText).hexdigest()

        matches = match(i, fakeHash, realHash)
        if not matches[0]:
            # add space to fakehash
            fakeText = fakeText + b" "
            numSpaces += 1
        else:
            i -= 1

        if matches[1] == int(sys.argv[1]):
            break

    print(f"number of digits matched: {matches[1]}")
    print(f"real hash: {realHash}")    
    print(f"fake hash: {fakeHash}")
    print(f"number of spaces added: {numSpaces}")


# checks if the last digit up to the curr digit are all the same
def match(curr, fakeHash, realHash):
    numMatches = 0
    for i in range(LAST_DIGIT, curr - 1, -1):
        if fakeHash[i] != realHash[i]:
            numMatches = 0
            return False, numMatches
        else:
            numMatches += 1
            
    return True, numMatches
main()