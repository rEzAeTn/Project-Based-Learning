import random

from utils import print_error, print_success, print_warning




class Wordle:

    def __init__(self, file_path, word_len: int = 5, limit: int = 1000):
        self.word_len = word_len
        self.words = self.generate_word_frequency(file_path, word_len, limit)


    # Build Data
    def generate_word_frequency(self, file_path: str, word_len: int, limit: int):
        # Open File & Create List from Data [(Word, Frequency)]
        with open(file_path) as file:
            words_freq = []
            for line in file:
                word, frequency = line.split(', ')
                words_freq.append((word, int(frequency)))


        # Sorted Data
        words_freq = sorted(words_freq, key=lambda w_freq: w_freq[1], reverse=True)

        # Limit Data
        words_freq = words_freq[:limit]

        # Drop Frequency Data
        words = [w_freq[0] for w_freq in words_freq]

        # word_len Letters Words
        words = list(filter(lambda word: len(word) == word_len, words))


        return words



    # Start Game
    def run(self):

        # Create Random Word
        word = random.choice(self.words)
        word = word.upper()


        # Run Game
        num_try = 6
        success = False

        while num_try > 0:

            # Getting Words from User
            guess_word = input(f'Enter a {self.word_len} Letter Word, Q For Exite): ')
            guess_word = guess_word.upper()

            if guess_word == 'Q':
                print_error('Bye')
                break

            # Word Lenght
            if len(guess_word) != self.word_len:
                print_warning(f'Word Must Have {self.word_len} Letters. You Entered {len(guess_word)}!')
                continue


            # # Check Valid Word
            # if guess_word not in self.words:
            #     print_warning('Word Is Not Valid')
            #     continue


            # Check Valid Characters, Invalid Positions, Invalid Character
            for word_letter, guess_letter in zip(word, guess_word):
                if word_letter == guess_letter:
                    print_success(f' {guess_letter} ', end='')
                    print(' ', end='')
                elif guess_letter in word:
                    print_warning(f' {guess_letter} ', end='')
                    print(' ', end='')
                else:
                    print_error(f' {guess_letter} ', end='')
                    print(' ', end='')

            print()

            if word == guess_word:
                print()
                print_success('** YOU WINNER **')
                success = True
                break


            num_try -= 1

        if not success:
            print()
            print_error(f'GAME OVER :( \nThe Word Was: " {word} "')
