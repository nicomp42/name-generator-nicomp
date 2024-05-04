# Name Generator Utilities
# Utilities.py
# Bill Nicholson
# DirkGentlyHHGG@gmail.com
# https://github.com/nicomp42/name-generator-nicomp


def count_nouns(generated_names, noun):
    count = 0
    for name in generated_names:
        if name.endswith(noun):
            count = count + 1
    return count


if __name__ == "__main__":
    print("countNouns():", count_nouns(["abc123", "def123", "xxx000"], "123"))
    