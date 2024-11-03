from src.utils.inputs import Inputs
from src.utils.purchase_details import Purchase
from src.utils.purchase_management import PurchaseManager
from src.utils.purchase_processing import DataProcessor


def main():
    """
    Main function is manage purchases and data processing  and display summary.

    This function continuously takes inputs for purchase details,
    adds them to the purchase manager, and displays a summary if requested.
    The loop continues until the user decides not to add more purchases.
    """

    # Initialize input and purchase manager objects
    get_input = Inputs()
    purchase_manager = PurchaseManager()

    while True:
        # Get inputs for purchase details
        # TODO: get name partner and ceate grup
        # input_names = get_input.get_names()
        input_purchase_description = get_input.get_purchase_description()
        input_amount_paid = get_input.get_amount_paid()
        input_payer_name = get_input.get_payer_name()
        input_consumer = get_input.get_consumer_name()

        # Create a new purchase object from class Purchase with the inputs
        create_purchase = Purchase(purchase_description=input_purchase_description ,
                                   amount_paid=input_amount_paid,
                                   payer_name=input_payer_name,
                                   consumer=input_consumer
                                   )

        # Add the new purchase to the purchase_manager
        purchase_manager.add_purchase(create_purchase)

        # Ask if the user wants to view a summary
        suggest1 = input("View Status Summary, `Y or ...`")
        if suggest1.upper() == "Y":
            # Create a dataframe from the information about all purchasespurchases
            data_frame = purchase_manager.create_dataframe()
            # Create a DataProcessor object to process the dataframe
            data_processor = DataProcessor(data_frame)
            # Create object from DataProcessor Methods for calculation total spent, total share, balance, summare report
            total_spent = data_processor.calculate_total_spent()
            total_share = data_processor.calculate_total_share()
            balances = data_processor.calculate_balances()
            summary_report_dataframe = data_processor.create_summary_report_dataframe()

            # Print the summary details
            print(data_frame)
            print()
            print(f'total spent --> {total_spent}')
            print(f'total share --> {total_share}')
            print(f'Balances    --> {balances}')
            print()
            print(summary_report_dataframe)
            print()

        # Ask if the user wants to add a new purchase
        suggest2 = input("You Want Add a New Purchases, `Y or ...`")
        if suggest2.upper() == "Y":
            continue
        else:
            break

if __name__ == "__main__":
    main()
