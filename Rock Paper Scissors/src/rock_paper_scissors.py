import random
import sys
from typing import List


class RockPaperScissors:
    """
    A Rock-Paper-Scissors game between players or a player and the computer.

    Attributes
    ----------
    choices : List[str]
        The available choices in the game.

    Methods
    -------
    get_player_choice(player_name: str) -> str
        Prompts the player to select a choice and validates it.
    decide_winner(choice1: str, choice2: str) -> str
        Decides the winner based on the players' choices.
    play_game(player1: str, player2: str, rounds: int, is_computer: bool) -> None
        Plays the specified number of rounds and displays the results.
    """

    def __init__(self) -> None:
        """
        Initializes the RockPaperScissors game.
        """
        self.choices: List[str] = ['Rock', 'Paper', 'Scissors']

    def get_player_choice(self, player_name: str) -> str:
        """
        Prompts the player to select a valid choice.

        Parameters
        ----------
        player_name : str
            Name of the player.

        Returns
        -------
        str
            The validated player choice.
        """
        while True:
            choice = input(
                f"{player_name}, Enter your Choice "
                f"({', '.join(self.choices)} | Q): "
            ).title()
            if choice.upper() == "Q":  # Quit condition
                print("Goodbye!")
                sys.exit()  # Exit the program immediately
            if choice in self.choices:
                return choice
            print(f"Invalid input, please choose from {', '.join(self.choices)}.")

    def decide_winner(self, choice1: str, choice2: str) -> str:
        """
        Determines the outcome of a game round.

        Parameters
        ----------
        choice1 : str
            Choice of the first player.
        choice2 : str
            Choice of the second player.

        Returns
        -------
        str
            Result of the game round.
        """
        if choice1 == choice2:
            return "Game Tie!"
        
        win_combinations = [
            ('Rock', 'Scissors'),
            ('Paper', 'Rock'),
            ('Scissors', 'Paper')
        ]
        if (choice1, choice2) in win_combinations:
            return "Player 1"
        return "Player 2"

    def play_game(
        self, player1: str, player2: str, rounds: int, is_computer: bool
    ) -> None:
        """
        Conducts the specified number of rounds of Rock-Paper-Scissors.

        Parameters
        ----------
        player1 : str
            Name of the first player.
        player2 : str
            Name of the second player or 'Computer'.
        rounds : int
            Number of rounds to play.
        is_computer : bool
            Whether the game is against the computer.
        """
        print(f"\n{player1} vs {player2}")
        
        player1_score = 0
        player2_score = 0

        for round_num in range(1, rounds + 1):
            print(f"\nRound {round_num} | {player1} {player1_score} - "
                  f"{player2} {player2_score}")
            
            player1_choice = self.get_player_choice(player1)
            if is_computer:
                player2_choice = random.choice(self.choices)
            else:
                player2_choice = self.get_player_choice(player2)

            winner = self.decide_winner(player1_choice, player2_choice)

            print(f"{player1} chose {player1_choice} | "
                  f"{player2} chose {player2_choice}")
            
            if winner == "Player 1":
                print(f"{player1} Wins!")
                player1_score += 1
            elif winner == "Player 2":
                print(f"{player2} Wins!")
                player2_score += 1
            else:
                print(winner)

        print(f"Final Scores: {player1} {player1_score} - {player2} {player2_score}")
        if player1_score > player2_score:
            print(f"{player1} Overall Winner!")
        elif player2_score > player1_score:
            print(f"{player2} Overall Winner!")
        else:
            print("Game Tie!")


if __name__ == "__main__":
    # Create a game instance
    game = RockPaperScissors()

    while True:
        print("\nGame Mode:")
        print("1. Player vs Computer")
        print("2. Player vs Player")
        print("Q. Quit")
        
        mode = input("Enter your Choice: ").strip()
        if mode.upper() == "Q":
            print("Goodbye!")
            sys.exit()

        if mode == "1":
            player1_name = input("\nEnter Player 1's Name: ").strip().title() or "Player 1"
            rounds = int(input("Enter the Number of Rounds: "))
            game.play_game(player1_name, "Computer", rounds, is_computer=True)

        elif mode == "2":
            player1_name = input("Enter Player 1's Name: ").strip().title() or "Player 1"
            player2_name = input("Enter Player 2's Name: ").strip().title() or "Player 2"
            rounds = int(input("Enter the Number of Rounds: "))
            game.play_game(player1_name, player2_name, rounds, is_computer=False)

        else:
            print("Invalid Choice. Please try again.")
