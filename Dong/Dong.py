from typing import List, Tuple, Union
import pandas as pd



class Name:
    """
    This class represents a list of names.
    """

    def create_name_list(self, *args: str) -> List[str]:
        """
        Takes a variable number of arguments, each representing a name, and returns a set of unique names with proper capitalization.

        Parameters
        ----------
        args : str
            A variable number of arguments, each representing a name.

        Returns
        -------
        set
            A set of unique names with proper capitalization.
        """

        names = args
        unique_names = set(map(str.title, names))
        return unique_names



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

        if isinstance(payer_name, str):
            payer_name = (payer_name, )
        self.payer_name = payer_name

        if isinstance(consumer, str):
            consumer = (consumer, )
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



class PurchaseManager:
    """
    This class manages a list of purchases and can generate a data frame containing information about all purchases.
    """

    def __init__(self):
        # Initialize an empty list to store purchases
        self.purchases = []


    def add_purchase(self, purchase: Purchase):
        # Add a new purchase to the list
        self.purchases.append(purchase)
        return self.add_purchase


    def create_dataframe(self) -> pd.DataFrame:
        # Initialize empty lists to store data
        purchase_descriptions = []
        amounts_paid = []
        payer_names = []
        consumers = []

        # Loop through all purchases and extract data
        for purchase in self.purchases:
            purchase_descriptions.append(purchase.get_purchase_description())
            amounts_paid.append(purchase.get_amount_paid())
            payer_names.append(purchase.get_payer_name())
            consumers.append(purchase.get_consumer())

        # Create a dataset from extracted data
        dataset = {'purchase_description': purchase_descriptions,
                    'amount_paid': amounts_paid,
                    'payer_name': payer_names,
                    'consumer': consumers}

        # Create index labels for data frame
        index_labels = [f'Purchase {i+1}' for i in range(len(self.purchases))]

        # Create data frame from dataset and index labels
        data_frame = pd.DataFrame(dataset, index = index_labels)

        return data_frame



class DataProcessor:
    """
    This class processes a data frame containing information about purchases and can calculate:
    - total spent,
    - total share,
    - balances
    for each person involved in the purchases.
    """

    def __init__(self, data_frame: pd.DataFrame):
        # Initialize DataProcessor with given data frame
        self.data_frame = data_frame

        self.total_spent = self.calculate_total_spent()
        self.total_share = self.calculate_total_share()
        self.balances = self.calculate_balances()


    def calculate_total_spent(self) -> dict:
        # Initialize an empty dictionary to store total spent by each person
        total_spent = {}

        # Loop through all rows in data frame and calculate total spent by each person
        for index, row in self.data_frame.iterrows():
            split_amount = row['amount_paid'] / len(row['payer_name'])
            for payer in row['payer_name']:
                if payer not in total_spent:
                    total_spent[payer] = 0
                total_spent[payer] += split_amount

        # Round total spent values to 2 decimal places
        rounded_total_spent = {name: round(value, 2) for name, value in total_spent.items()}

        return rounded_total_spent


    def calculate_total_share(self) -> dict:
        # Initialize an empty dictionary to store total share of each person
        total_share = {}

        # Loop through all rows in data frame and calculate total share of each person
        for index, row in self.data_frame.iterrows():
            split_amount = row['amount_paid'] / len(row['consumer'])
            for consumer in row['consumer']:
                if consumer not in total_share:
                       total_share[consumer] = 0
                total_share[consumer] += split_amount

        # Round total share values to 2 decimal places
        rounded_total_share = {name: round(value, 2) for name, value in total_share.items()}

        return rounded_total_share


    def calculate_balances(self) -> dict:
        # Initialize an empty dictionary to store balances of each person
        balances = {}

        # Initialize balances for all payer names
        for name in self.data_frame['payer_name'].unique():
            balances[name] = 0

        # Loop through all rows in data frame and calculate balances of each person
        for index, row in self.data_frame.iterrows():
            split_amount = row['amount_paid'] / len(row['consumer'])
            for consumer in row['consumer']:
                if consumer not in balances:
                    balances[consumer] = 0
                balances[consumer] -= split_amount

            for payer in row['payer_name']:
                balances[payer] += row['amount_paid'] / len(row['payer_name'])

        # Round balance values to 2 decimal places
        rounded_balances = {name: round(value, 2) for name, value in balances.items()}

        return rounded_balances

    def create_summary_report_dataframe(self, ) -> pd.DataFrame:
        """
        Creates a summary report data frame containing information about
        - total spent
        - total share
        - balances
        for each person involved in the purchases.

        Parameters
        ----------
        data_frame : DataFrame
            A data frame containing information about the purchases.

        Returns
        -------
        DataFrame
            A data frame containing information about total spent, total share, and balances for each person.
        """

        # Extract unique names from the 'consumer' column in the data frame
        for column_name, column_data in self.data_frame.items():
            if column_name == 'consumer':
                column_consumer = column_data
            elif column_name == 'payer_name':
                colum_payer_name = column_data

        # Create a set of unique names from the 'consumer and payer_name' column data
        unique_names = set()
        # extract name from  each tuple 'column_consumer' and add name to 'unique_names' set
        for tuple_names in column_consumer:
            for name in tuple_names:
                unique_names.add(name)
        # extract name from  each tuple 'column_payer_name' and add name to 'unique_names' set
        for tuple_name in colum_payer_name:
            for name in tuple_name:
                unique_names.add(name)

        # Initialize an empty dataset to store summary data
        summary_dataset = {name: [] for name in unique_names}

        # Add total spent data to dataset
        for name in unique_names:
            if name in self.total_spent:
                summary_dataset[name].append(self.total_spent[name])
            else:
                summary_dataset[name].append(0)

        # Add total share data to dataset
        for name in unique_names:
            if name in self.total_share:
                summary_dataset[name].append(self.total_share[name])
            else:
                summary_dataset[name].append(0)


        # Add balance data to dataset
        for name in unique_names:
            if name in self.balances:
                summary_dataset[name].append(self.balances[name])
            else:
                summary_dataset[name].append(0)


        # Create data frame from dataset with appropriate index labels
        summary_dataframe = pd.DataFrame(summary_dataset, index = ['TOTAL SPENT', 'TOTEL SHARE', 'BALANCES'])

        return summary_dataframe
