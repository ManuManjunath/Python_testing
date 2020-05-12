"""
Sample code for recursive function.
This calls the function "guessValue" within itself until a condition is met.
"""
import random

# Define limits
lower = 1
higher = 100

attempt = 1
# First store a random number
original = random.randint(lower, higher)
print("Original value is", original)
print(f"Original limits are {lower} to {higher}")

# Now try to guess the original random number
def guessValue(lower, higher):
    guessedValue = random.randint(lower, higher)
    if guessedValue == original:
        print("Correct guess: ", guessedValue)
        return guessedValue
    elif guessedValue > original:
        # If you have guessed higher, change your guessing upper limit
        print("You guessed higher: ", guessedValue)
        newHigher = guessedValue -1
        print(f"New limits are {lower} to {newHigher}")
        guessValue(lower, newHigher)
    else:
        # If you have guessed lower, change your guessing lower limit
        print("You guessed lower: ", guessedValue)
        newLower = guessedValue + 1
        print(f"New limits are {newLower} to {higher}")
        guessValue(newLower, higher)

guessValue(lower, higher)

"""
Output - 
Original value is 87
Original limits are 1 to 100
You guessed lower:  9
New limits are 10 to 100
You guessed lower:  28
New limits are 29 to 100
You guessed lower:  76
New limits are 77 to 100
You guessed higher:  89
New limits are 77 to 88
You guessed lower:  80
New limits are 81 to 88
You guessed lower:  83
New limits are 84 to 88
Correct guess: 87
"""
