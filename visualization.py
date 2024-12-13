import matplotlib.pyplot as plt
import pandas as pd

def visualize_monthly_spending(data):
    if data is not None:
        data["Date"] = pd.to_datetime(data["Date"])
        spending_data = data[data["Amount"] < 0]
        spending_by_month = spending_data.groupby(data["Date"].dt.to_period("M"))["Amount"].sum()
        spending_by_month.plot(kind="line", marker="o", title="Monthly Spending Trend")
        plt.xlabel("Month")
        plt.ylabel("Total Spending (Negative Amounts)")
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()
        plt.show()
    else:
        print("No data loaded. Please import a CSV file first.")