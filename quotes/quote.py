import random

def quote_gen() :
    # Read quotes from the text file
    with open('quotes.txt', 'r') as file:
        quotes = file.read().splitlines()  # Read all lines and remove newline characters

# Get a random quote
    random_quote = random.choice(quotes)
    return random_quote
