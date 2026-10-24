class Customer:
    def __init__(self):
        self.customer_id = ""
        self.customer_name = ""
        self.account_number = ""
        self.balance = 0
        self.credit_cards = []

    def create_customer(self):
        self.customer_id = input("Customer ID: ")
        self.customer_name = input("Customer name: ")
        self.account_number = input("Account number: ")
        self.balance = float(input("Initial balance: "))

    def display_customer(self):
        print("-----------------------------")
        print("Customer ID:", self.customer_id)
        print("Customer name:", self.customer_name)
        print("Account number:", self.account_number)
        print("Balance:", self.balance)
        print("Credit cards:")
        for card in self.credit_cards:
            print("  Card number:", card.card_number)

    def transfer_funds(self, beneficiary_customer_object, amount):
        if amount > self.balance:
            print("Not enough balance for this transfer.")
        else:
            self.balance = self.balance - amount
            beneficiary_customer_object.balance = beneficiary_customer_object.balance + amount
            print("Transfer completed.")

    def assign_card(self, card_object):
        self.credit_cards.append(card_object)
        print("Card assigned to", self.customer_name)


class Card:
    def __init__(self):
        self.card_number = ""
        self.cvv = ""
        self.expiry_date = ""
        self.balance = 0

    def create_card(self):
        self.card_number = input("Card number: ")
        self.cvv = input("CVV: ")
        self.expiry_date = input("Expiry date: ")
        self.balance = float(input("Card balance: "))

    def display_card(self):
        print("-----------------------------")
        print("Card number:", self.card_number)
        print("CVV:", self.cvv)
        print("Expiry date:", self.expiry_date)
        print("Balance:", self.balance)



customer_list = []
card_list = []

while True:
    print("Hello! Welcome to the Customer and Card Management System. Please select an option from the menu below:")
    print("===== MAIN MENU =====")
    print("1. Create Customer objects")
    print("2. Create Card objects")
    print("3. Transfer funds between customer objects")
    print("4. Assign card objects to customer objects")
    print("5. Display Customer Info")
    print("6. Display Card Info")
    print("7. Exit")

    option = input("Choose an option: ")

    if option == "1":
        new_customer = Customer()
        new_customer.create_customer()
        customer_list.append(new_customer)

    elif option == "2":
        new_card = Card()
        new_card.create_card()
        card_list.append(new_card)

    elif option == "3":
        sender_id = input("Sender customer ID: ")
        beneficiary_id = input("Beneficiary customer ID: ")
        sender_customer = None
        beneficiary_customer = None

        for customer in customer_list:
            if customer.customer_id == sender_id:
                sender_customer = customer
            if customer.customer_id == beneficiary_id:
                beneficiary_customer = customer

        if sender_customer is None or beneficiary_customer is None:
            print("Customer not found.")
        else:
            amount = float(input("Amount to transfer: "))
            sender_customer.transfer_funds(beneficiary_customer, amount)

    elif option == "4":
        customer_id = input("Customer ID: ")
        card_number = input("Card number: ")
        selected_customer = None
        selected_card = None

        for customer in customer_list:
            if customer.customer_id == customer_id:
                selected_customer = customer

        for card in card_list:
            if card.card_number == card_number:
                selected_card = card

        if selected_customer is None or selected_card is None:
            print("Customer or card not found.")
        else:
            selected_customer.assign_card(selected_card)

    elif option == "5":
        for customer in customer_list:
            customer.display_customer()


    elif option == "6":
        for card in card_list:
            card.display_card()

    elif option == "7":
        print("Goodbye! :)")
        break

    else:
        print("Invalid option.")