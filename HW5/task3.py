import pickle

if __name__ == '__main__':
    with open('./test/data/text.txt', 'r') as file:
        text = file.read().lower()

        # v1
        # letters = 'abcdefghijklmnopqastuvwxyz'
        letters = set(text)
        print(letters)
        for letter in letters:  # Only count letters
            if letter.isalpha():
                print(f"{letter}: {list(text).count(letter)}")

        # v2
        # letter_count = {}
        #
        # for letter in text:
        #     if letter.isalpha():  # Only count letters
        #         if letter in letter_count:
        #             letter_count[letter] += 1
        #         else:
        #             letter_count[letter] = 1
        #
        # for letter, count in letter_count.items():
        #     print(letter, count)



