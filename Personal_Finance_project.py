import pandas as pd
import data_management
import data_analysis
import visualization

def menu():
    print("==== Personal Finance Track ====")

    data = None

    while True:
        print("\n0. Import a CSV File")
        print("1. View All Transactions")
        print("2. View Transactions by Date Range")
        print("3. Add a Transaction")
        print("4. Edit a Transaction")
        print("5. Delete a Transaction")
        print("6. Analyze Spending by Category")
        print("7. Calculate Average Monthly Spending")
        print("8. Show Top Spending Category")
        print("9. Visualize Monthly Spending Trend")
        print("10. Save Transactions to CSV")
        print("11. Exit")
        choice = input("Choose an option (0-11): ")
        if choice == '0':
            data = data_management.load_transactions(data)
        elif choice == '1':
            data_management.view_transactions(data)
        elif choice == '2':
            data_management.view_transactions_by_date(data)
        elif choice == '3':
            data = data_management.add_transaction(data)
        elif choice == '4':
            data = data_management.edit_transaction(data)
        elif choice == '5':
            data = data_management.delete_transaction(data)
        elif choice == '6':
            data_analysis.analyze_spending_by_category(data)
        elif choice == '7':
            data_analysis.calculate_avg_month_spending(data)
        elif choice == '8':
            data_analysis.show_top_spending_category(data)
        elif choice == '9':
            visualization.visualize_monthly_spending(data)
        elif choice == '10':
            data_management.save_transactions(data)
        elif choice == '11':
            print("Exiting the Personal Finance Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 0 and 11.")


if __name__ == "__main__":
    menu()