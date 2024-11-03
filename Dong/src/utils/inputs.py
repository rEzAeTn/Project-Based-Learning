class Inputs():
    def __init__(self):
        pass


    def get_names(self):
        names = []
        while True:
            name = input("Enter Name Partners, `at the End Enter Q` ")
            if name.upper() == "Q":
                break
            names.append(name.strip())
        
        unique_names = set(map(str.title, names))
        return unique_names


    def get_purchase_description(self):
        input_purchase_description = input("Enter Description Purchase ")
        return input_purchase_description


    def get_amount_paid(self):
        while True:
            input_amount_paid = input("Enter Amount Paid ")
            try:
                amount_paid = float(input_amount_paid)
                if amount_paid.is_integer():
                    amount_paid = int(input_amount_paid)
            except ValueError:
                    print("Invalid Input: Please Try Again")
                    continue
            break

        return amount_paid


    def get_payer_name(self):
        names = []
        while True:
            name = input("Enter Payer Name, `at the End Enter Q` ")
            if name.upper() == "Q":
                break
            names.append(name.strip())
        
        unique_names = set(map(str.title, names))
        return unique_names


    def get_consumer_name(self):
        names = []
        while True:
            name = input("Enter Consumer Name, `at the End Enter Q` ")
            if name.upper() == "Q":
                break
            names.append(name.strip())
        
        unique_names = set(map(str.title, names))
        return unique_names
