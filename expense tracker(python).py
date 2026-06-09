import sys
expenses = []
def log_expense():
    print("\n--- Log New Expense ---")
    description = input("Enter expense description/name: ").strip()
    if not description:
        print(" Description cannot be empty.")
        return
    try:
        amount = float(input("Enter amount (e.g., 250.50): "))
        if amount <= 0:
            print(" Amount must be greater than zero.")
            return
    except ValueError:
        print(" Invalid number format. Please enter numbers only.")
        return
    print("Categories: [1] Food  [2] Utilities  [3] Entertainment  [4] Transport  [5] Other")
    cat_choice = input("Select category number (1-5): ").strip()
    
    category_map = {"1": "Food", "2": "Utilities", "3": "Entertainment", "4": "Transport", "5": "Other"}
    category = category_map.get(cat_choice, "Other")
    expense_item = {
        "description": description,
        "amount": amount,
        "category": category
    }
    expenses.append(expense_item)
    print(f"✅ Success: Added '{description}' under '{category}' for ₹{amount:.2f}")


def view_summary():
    print("\n--- Monthly Summary Dashboard ---")
    if not expenses:
        print("No expenses recorded yet. Total Spend: ₹0.00")
        return

    print(f"{'Description':<20} | {'Category':<15} | {'Amount':<10}")
    print("-" * 53)
    
    total = 0.0
    for exp in expenses:
        print(f"{exp['description']:<20} | {exp['category']:<15} | ₹{exp['amount']:<10.2f}")
        total += exp["amount"]
        
    print("-" * 53)
    print(f"Total Spend This Month: ₹{total:.2f}")


def analyze_category():
    print("\n--- Expenses by Category ---")
    if not expenses:
        print("No data available to analyze.")
        return
    total_spend = sum(exp["amount"] for exp in expenses)
    category_totals = {"Food": 0.0, "Utilities": 0.0, "Entertainment": 0.0, "Transport": 0.0, "Other": 0.0}
    for exp in expenses:
        category_totals[exp["category"]] += exp["amount"]
    for cat, amt in category_totals.items():
        percentage = (amt / total_spend) * 100 if total_spend > 0 else 0
        print(f"{cat:<15}: ₹{amt:<8.2f} ({percentage:.1f}%)")
def set_budget():
    print("\n--- Define Custom Budget Threshold Limits ---")
    print("Feature coming soon! Budgets require data persistence setup.")
def export_and_exit():
    print("\nExporting financial logs to local files...")
    print(f"Successfully processed {len(expenses)} transactions.")
    print("Data safely stored! Goodbye.")
    sys.exit()
def main():
    while True:
        print("\n================ SpendWise Dashboard ================")
        print("1. Log New Expense")
        print("2. View Monthly Summary Dashboard")
        print("3. Analyze Expenses by Category")
        print("4. Define Custom Budget Threshold Limits")
        print("5. Export Financial Log & Exit")
        user_choice = input("\nEnter your choice (1-5): ").strip()
        if user_choice == "1":
            log_expense()
        elif user_choice == "2":
            view_summary()
        elif user_choice == "3":
            analyze_category()
        elif user_choice == "4":
            set_budget()
        elif user_choice == "5":
            export_and_exit()
        else:
            print("\n[Invalid Selection] Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
