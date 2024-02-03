import random

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "I used to be a baker, but I couldn't make enough dough.",
        "What do you call a fish with no eyes? Fsh."
    ]

    random_joke = random.choice(jokes)
    print(random_joke)

tell_joke()