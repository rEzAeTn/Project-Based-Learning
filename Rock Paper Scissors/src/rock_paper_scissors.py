import random
from typing import List, Optional



class RockPaperScissors:
    def __init__(self, name: str) -> None:
        self.choices: List[str] = ['Rock', 'Paper', 'Scissors']
        self.player_name: str = name

    def get_player_choice(self) -> str:
        player_choice: str = input(f'Your choice ({self.choices}): ').title()
        if player_choice in self.choices:
            return player_choice

        print(f'Invalid input, must choice from ({self.choices}).')
        return self.get_player_choice()

    def get_computer_choice(self) -> str:
        computer_choice: str = random.choice(self.choices)
        return computer_choice

    def decide_winner(self, player_choice: str, computer_choice: str) -> str:
        if player_choice == computer_choice:
            return 'Tie!'

        # [(player_choice, computer_choice), (player_choice, computer_choice), (player_choice, computer_choice)]
        win_combinations: List[tuple] = [('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')]
        for win_combine in win_combinations:
            if (player_choice == win_combine[0]) & (computer_choice == win_combine[1]):
                return f'{self.player_name} Won!'

        return 'Oh No, Computer Won!'

    def play(self) -> None:
        player_choice: str = self.get_player_choice()
        computer_choice: str = self.get_computer_choice()
        print(f'{self.player_name} choice --> {player_choice} * {computer_choice} <-- Computer choice')
        print(self.decide_winner(player_choice, computer_choice))


if __name__ == "__main__":
    game: RockPaperScissors = RockPaperScissors('Reza')

    while True:
        game.play()

        continue_game: str = input('Game Again? Play again *Any Key* - Quit *Q*')
        if continue_game.upper() == 'Q':
            break
