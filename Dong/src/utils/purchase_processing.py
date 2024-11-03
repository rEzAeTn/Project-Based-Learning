from typing import List, Tuple, Union

import pandas as pd


class DataProcessor:
    """
    This class processes a data frame containing information about purchases and can calculate:
    - total spent,
    - total share,
    - balances
    for each person involved in the purchases.
    """

    def __init__(self, data_frame):
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
                balances[payer] = balances.get(payer, 0) + row['amount_paid'] / len(row['payer_name'])
                # ! line down replace by line up
                # balances[payer] += row['amount_paid'] / len(row['payer_name'])

        # Round balance values to 2 decimal places
        rounded_balances = {name: round(value, 2) for name, value in balances.items()}

        return rounded_balances

    def create_summary_report_dataframe(self, ):
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