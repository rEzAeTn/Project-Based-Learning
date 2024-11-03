from typing import List, Tuple, Union


class Purchase:
    """
    This class represents a purchase made by one or more people.
    """

    def __init__(self,
                 purchase_description: str,
                 amount_paid: float,
                 payer_name: tuple,
                 consumer: Union[str, Tuple[str]]
                ):
        """
        Initializes a Purchase object with the given purchase description, amount paid, payer name, and consumer(s).

        Parameters
        ----------
        purchase_description : str
            The description of the purchase.

        amount_paid : float
            The amount paid for the purchase.

        payer_name : str
            The name of the person who paid for the purchase.

        consumer : str or tuple of str
            The name(s) of the person(s) who consumed the purchase.
        """

        self.purchase_description = purchase_description
        self.amount_paid = amount_paid
        self.payer_name = payer_name
        self.consumer = consumer



    def get_purchase_description(self) -> str:
        """
        Returns the description of the purchase.

        Returns
        -------
        str
            The description of the purchase.
        """
        return self.purchase_description



    def get_amount_paid(self) -> float:
        """
        Returns the amount paid for the purchase.

        Returns
        -------
        float
            The amount paid for the purchase.
        """
        return self.amount_paid



    def get_payer_name(self) -> str:
        """
         Returns the name of the person who paid amount for the purchase.

         Returns
         -------
         str
             The name of the person who paid amount for the purchase.
         """
        # Remove Name Duplicates
        payer_name = set(self.payer_name)
        return tuple(payer_name)



    def get_consumer(self) -> Tuple[str]:
        """
         Returns the name(s) of the person(s) who consumed the purchase.

         Returns
         -------
         tuple of str
             The name(s) of the person(s) who consumed the purchase.
         """

        # Remove Name Duplicates
        consumer = set(self.consumer)
        return tuple(consumer)