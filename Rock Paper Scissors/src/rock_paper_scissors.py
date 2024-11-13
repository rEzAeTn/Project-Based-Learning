import random
from typing import List


class RockPaperScissors:
    """
    A Rock-Paper-Scissors game between a player and the computer.

    Attributes
    ----------
    player_name : str
        Name of the player.
    choices : List[str]
        The available choices in the game.

    Methods
    -------
    get_player_choice() -> str
        Prompt the player to select a choice, validates it, and returns it.
    get_computer_choice() -> str
        Randomly selects a choice for the computer.
    decide_winner(player_choice: str, computer_choice: str) -> str
        Decides the winner based on the player's and computer's choices.
    play() -> None
        Plays a round of the game and prints the result.
    """

    def __init__(self, name: str) -> None:
        """
        Initializes the RockPaperScissors game with the player's name.

        Parameters
        ----------
        name : str
            The name of the player.
        """
        self.choices: List[str] = ['Rock', 'Paper', 'Scissors']
        self.player_name: str = name

    def get_player_choice(self) -> str:
        """
        Prompts the player to select a valid choice and returns it.

        Returns
        -------
        str
            The validated player choice.
        """
        while True:
            # Prompt player and format input
            player_choice = input(
                f'Your choice ({", ".join(self.choices)}): '
            ).title()
            if player_choice in self.choices:
                return player_choice

            print(f'Invalid input, must choose from {self.choices}.')

    def get_computer_choice(self) -> str:
        """
        Randomly selects a choice for the computer.

        Returns
        -------
        str
            The computer's choice.
        """
        computer_choice: str = random.choice(self.choices)
        return computer_choice

    def decide_winner(self, player_choice: str, computer_choice: str) -> str:
        """
        Determines the outcome of a game round.

        Parameters
        ----------
        player_choice : str
            The player's choice.
        computer_choice : str
            The computer's choice.

        Returns
        -------
        str
            Result of the game round.
        """
        if player_choice == computer_choice:
            return 'Tie!'

        # Define win conditions as tuples
        win_combinations = [
            ('Rock', 'Scissors'),
            ('Paper', 'Rock'),
            ('Scissors', 'Paper')
        ]
        
        # Check if player's choice matches any winning combination
        if (player_choice, computer_choice) in win_combinations:
            return f'{self.player_name} Won!'
        
        return 'Oh No, Computer Won!'

    def play(self) -> None:
        """
        Conducts a single round of Rock-Paper-Scissors, printing choices and
        the result of the game.
        """
        player_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()

        # Show the choices made by player and computer
        print(
            f'{self.player_name} choice --> {player_choice} * '
            f'{computer_choice} <-- Computer choice'
        )

        # Display the result
        print(self.decide_winner(player_choice, computer_choice))


if __name__ == "__main__":
    game = RockPaperScissors('User')

    while True:
        # Play a round of the game
        game.play()

        # Check if the player wants to continue
        continue_game = input('Game Again? Play again *Any Key* - Quit *Q* ')
        if continue_game.upper() == 'Q':
            break
