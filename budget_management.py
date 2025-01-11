monthly_income = None
category_budgets = {}

def set_monthly_income(data):
    global monthly_income

    if data is not None:
        try:
            income = float(input("Enter your total monthly income: ").strip())
            monthly_income = income
            print(f"Your monthly income is set to: ${income:.2f}")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
def set_category_income(data):
    global category_budgets
    try:
        categories = ["Food", "Grocery", "Health Insurance", "Extra bill", "Gas", "Monthly Transportation fee", "College Payment", "Entertainment Expenses", "Uber"]
        for cat in categories:
            budget = float(input(f"Enter your budget for {cat}: ").strip())
            category_budgets[cat] = budget
        print("\nYour budgets have been set:")
        for category, budget in category_budgets.items():
            print(f" - {cat}: ${budget:.2f}")
    except ValueError:
        print("Invalid input. Please enter numeric values for budgets.")
def check_budget_status(data):
    if data is not None:
        try:
            if not category_budgets:
                print("No budgets set. Please set category budgets first.")
                return

            print("\n--- Budget Status ---")
            suggestions = []
            for category, budget in category_budgets.items():
                # Filter transactions by category
                category_spending = data[data["Category"] == category]["Amount"].sum()
                print(f"- {category}: ${abs(category_spending):.2f} / ${budget:.2f}", end=" ")

                if abs(category_spending) > budget:
                    print("(Alert: Exceeded budget!)")
                    suggestions.append(f"Consider reducing {category} spending or adjusting the budget.")
                else:
                    print("(Within budget)")

            # Display suggestions
            if suggestions:
                print("\nSuggestions:")
                for suggestion in suggestions:
                    print(f"- {suggestion}")
            else:
                print("You are within budget for all categories. Great job!")
        except KeyError:
            print("Error: Ensure your data includes a 'Category' column.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
    else:
        print("No data loaded. Please import a CSV file first.")



