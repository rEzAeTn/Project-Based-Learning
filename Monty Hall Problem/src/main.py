import random
from typing import List, Tuple


class MontyHallProblem:
    """
    This class represents the Monty Hall problem. It includes methods to simulate a single game and multiple games.
    """

    def __init__(self):
        """
        Initialize the doors for the Monty Hall problem.
        """
        self.doors: list = ['goat', 'car', 'goat']
        self.door_revealed = None

    def reveal_door(self, initial_choice: int) -> int:
        """
        Reveal a door that is not the initial choice and does not have the car.

        :param initial_choice: The initial door choice.
        :return: The index of the revealed door.
        """
        doors_revealed = [i for i in range(3) if i != initial_choice and self.doors[i] != 'car']
        door_revealed = random.choice(doors_revealed)
        return door_revealed

    def monty_hall_game(self, initial_choice: int, switch_choice: bool) -> bool:
        """
        Simulate a single game of the Monty Hall problem.

        :param initial_choice: The initial door choice.
        :param switch_choice: A boolean indicating whether the player switches their choice.
        :return: True if the player wins, False otherwise.
        """
        # Shuffle the doors
        random.shuffle(self.doors)

        # Reveal a door that is not the initial choice and does not have the car
        self.door_revealed = self.reveal_door(initial_choice)

        # If the player switches, their final choice is the remaining door
        if switch_choice:
            final_choice = [i for i in range(3) if i != initial_choice and i != self.door_revealed][0]
        else:
            final_choice = initial_choice

        # The player wins if their final choice is the car
        return self.doors[final_choice] == 'car'

    def monty_hall_simulation(self, number_of_round: int, switch_choice: bool) -> Tuple[int, int]:
        """
        Simulate multiple rounds of the Monty Hall problem.

        :param number_of_round: The number of rounds to simulate.
        :param switch_choice: A boolean indicating whether the player switches their choice in each round.
        :return: The number of wins and losses.
        """
        # The player's initial choice is random in each round
        initial_choice = random.choice(range(3))

        # Count the number of wins
        num_wins = sum([self.monty_hall_game(initial_choice, switch_choice) for _ in range(number_of_round)])

        # The number of losses is the total rounds minus the number of wins
        num_losses = number_of_round - num_wins

        return num_wins, num_losses
