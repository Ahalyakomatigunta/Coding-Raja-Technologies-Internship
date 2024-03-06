import json

# Class to handle budget-related operations
class BudgetTracker:
    def _init_(self):
        self.transactions = []

    def add_transaction(self, type, category, amount):
        transaction = {
            'type': type,
            'category': category,
            'amount': float(amount)
        }
        self.transactions.append(transaction)
        print(f"{type.capitalize()} of ₹{amount} added under '{category}' category.")

    def calculate_budget(self):
        income = sum(t['amount'] for t in self.transactions if t['type'] == 'income')
        expenses = sum(t['amount'] for t in self.transactions if t['type'] == 'expense')
        return income - expenses

    def analyze_expenses(self):
        categories = set(t['category'] for t in self.transactions if t['type'] == 'expense')
        for category in categories:
            total = sum(t['amount'] for t in self.transactions if t['type'] == 'expense' and t['category'] == category)
            print(f"Total spent on {category}: ₹{total}")

    def save_transactions(self):
        with open('transactions.json', 'w') as file:
            json.dump(self.transactions, file)
        print("Transactions saved successfully.")

    def load_transactions(self):
        try:
            with open('transactions.json', 'r') as file:
                self.transactions = json.load(file)
            print("Transactions loaded successfully.")
        except FileNotFoundError:
            print("No previous transactions found. Starting fresh!")

# Main function to interact with the budget tracker
def main():
    budget_tracker = BudgetTracker()
    budget_tracker.load_transactions()

    while True:
        print("\n-- Budget Tracker --")
        print("1: Add Income")
        print("2: Add Expense")
        print("3: Check Budget")
        print("4: Analyze Expenses")
        print("5: Exit")
        choice = input("Choose an action: ")

        if choice == '1':
            amount = input("Enter the income amount: ")
            category = input("Enter the income source: ")
            budget_tracker.add_transaction('income', category, amount)
        elif choice == '2':
            amount = input("Enter the expense amount: ")
            category = input("Enter the expense category: ")
            budget_tracker.add_transaction('expense', category, amount)
        elif choice == '3':
            budget = budget_tracker.calculate_budget()
            print(f"Remaining Budget: ₹{budget}")
        elif choice == '4':
            budget_tracker.analyze_expenses()
        elif choice == '5':
            budget_tracker.save_transactions()
            print("Exiting. Have a great day!")
            break
        else:
            print("Invalid option, please try again.")

if _name_ == "_main_":
    main()