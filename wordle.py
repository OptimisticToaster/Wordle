#!/usr/bin/env python3


import os
import sys
import re


class Wordle:


    def __init__(self):
        self.print_column_spacing = 5
        self.print_columns = 6
        self.wordlist_file = 'word_list.txt'

        # Create list of the letters, ASCII 65-90
        self.letter_list = []
        for i in range(26):
            self.letter_list.append(chr(65+i))
        
        # Known letters in the correct positions
        self.correct = ['', '', '', '', '']

        # Known letters but don't know position
        self.close = []

        # Eliminated letters
        self.eliminated = []

        # Ask next step
        self.next_step()


    def next_step(self):
        print('Welcome to the Wordle helper!')
        print("""
        Please enter:
          1 to enter a losing guess
          2 to enter a guess that is partially correct (wrong spot)
          3 to enter a correct letter guess (correct spot)
          4 to print status
          5 to solve
          99 to end
        """)
        choice = input()

        if choice == '1':
            self.guess_wrong()
        
        elif choice == '2':
            self.guess_close()

        elif choice == '3':
            self.guess_correct()
        
        elif choice == '4':
            self.print_status()
        
        elif choice == '5':
            self.solve()
        
        elif choice == '99':
            sys.exit()
        
        else:
            print('Invalid entry. Please try again.')
            self.next_step()


    # Wrong guess
    def guess_wrong(self):
        print('Please enter the letter to be eliminated')
        letter = input().upper()
        self.eliminated.append(letter)
        self.eliminated.sort()
        self.letter_list.remove(letter)
        self.next_step()


    # Close guess
    def guess_close(self):
        print('Please enter the letter that is close')
        letter = input().upper()
        self.close.append(letter)
        self.close.sort()
        self.next_step()


    # Correct guess
    def guess_correct(self):
        print('Please enter the letter')
        letter = input().upper()
        print('Please enter the position [1-5] of the placement')
        placement = input()
        self.correct[int(placement)-1] = letter
        self.next_step()


    # Print status
    def print_status(self):
        os.system('clear')
        # Correct Letters
        print('= Correct Letters =')
        print(self.correct)
        print('')

        # Known Letters
        print('= Known Letters =')
        print(self.close)
        print('')

        # Eliminated Letters
        print('= Eliminated Letters =')
        print(self.eliminated)
        print('')



        # Show what letters are left
        print('= Remaining Letters =')
        space_counter = 0
        for let in self.letter_list:
            if space_counter < self.print_columns:
                space_counter += 1
                print(let, end=self.print_column_spacing*" ")
            else:
                space_counter = 0
                print(let)
        print('')
        self.next_step()


    # Solve
    def solve(self):
        # Create regex of possible solutions
        pattern = ''
        for i in range(5):
            # If known, just use that.
            if self.correct[i] != '':
                pattern += self.correct[i]
            # Otherwise, the pattern is the remaining available letters
            # PLUS consideration that the word must contain any Close letters
            else:
                pattern += self.letter_list.join()

        # List of possible solutions
        possible_solutions = []
        # Get word list
        with open(self.wordlist_file) as wordlist:
            # Step through each line
            for line in wordlist:
                # Check each word as possible solution
                if self.test_word(line.strip()):
                    possible_solutions.append(line.strip())
        print(possible_solutions)


    # Check word for being a possible solution
    def check_word(self, word):
        # Check if the given word could be a soluation
        # given the correct, close, and disqualified letters so far
        pattern_close = '[' + self.close.join() + ']'
        if re.search(pattern, word) and re.search(pattern_close, word):
            return True
        else:
            return False


def main(args):

    w = Wordle()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
