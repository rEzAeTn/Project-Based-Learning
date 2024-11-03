from typing import List, Tuple, Union

import pandas as pd


class PurchaseManager:
    """
    This class manages a list of purchases and can generate a data frame containing information about all purchases.
    """

    def __init__(self):
        # Initialize an empty list to store purchases
        self.purchases = []


    def add_purchase(self, purchase):
        # Add a new purchase to the list
        self.purchases.append(purchase)
        return self.add_purchase


    def create_dataframe(self):
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