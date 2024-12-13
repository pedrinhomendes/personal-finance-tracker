import pandas as pd
def analyze_spending_by_category(data):
    if data is not None:
        result = data.groupby("Description")["Amount"].sum()
        print(result)
    else:
        print("No data loaded. Please import a CSV file first.")

def calculate_avg_month_spending(data):
    if data is not None:
        data["Date"] = pd.to_datetime(data["Date"])
        spending_data = data[data["Amount"] < 0]
        spending_by_month = spending_data.groupby([data["Date"].dt.year, data["Date"].dt.month])["Amount"].sum()
        monthly_avg = spending_by_month.mean()
        print(f"Average Monthly Spending: {monthly_avg:.2f}")
    else:
        print("No data loaded. Please import a CSV file first.")

def show_top_spending_category(data):
    if data is not None:
        spending_data = data[data["Amount"] < 0]
        description_spending = spending_data.groupby("Description")["Amount"].sum()
        top_category = description_spending.idxmin()
        top_amount = description_spending.min()

        print(f"Top Spending Category: {top_category} with a total spending of {top_amount:.2f}")
    else:
        print("No data loaded. Please import a CSV file first.")