class Score:
    """
    A class used to represent the Score.

    Parameters
    ----------
    start_score : int, optional
        The initial score (default is 100)

    Attributes
    ----------
    score : int
        The current score
    """

    def __init__(self, start_score=100):
        """
        Initialize the Score class with an optional starting score.

        Parameters
        ----------
        start_score : int, optional
            The initial score (default is 100)
        """

        # Initialize the score with the given start_score
        self.score = start_score

    def decrement_score(self, penalty=5):
        """
        Decrease the score by a certain penalty.

        Parameters
        ----------
        penalty : int, optional
            The penalty amount to subtract from the score (default is 5)

        Returns
        -------
        int
            The updated score after applying the penalty.
        """
        self.score -= penalty  # Subtract the penalty from the score
        self.score = max(self.score, 0)  # Ensure the score doesn't go below 0

        # Return the updated score
        return self.score

    def return_score(self):
        """
        Return the current score.

        Returns
        -------
        int
            The current score.
        """
        
        # Return the current score
        return self.score  
