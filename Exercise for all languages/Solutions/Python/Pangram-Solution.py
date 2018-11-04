# Solution to Pangram Problem


def is_pangram(phrase):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in phrase:
            return False

    return True

# Not there could be multiple answers to this problem,
# I have provided a beginner friendly answer
