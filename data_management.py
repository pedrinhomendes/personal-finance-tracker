import pandas as pd

def load_transactions(data):
    file_path = input("Enter the file path of the CSV: ").strip()
    try:
        data = pd.read_csv(file_path)
        required_columns = ["Date", "Description", "Type", "Amount"]
        if not all(col in data.columns for col in required_columns):
            print("Error: Missing required columns.")
            return None

        print("CSV File Imported Successfully!")
        print("Preview of the data:")
        print(data.head())
        return data
    except FileNotFoundError:
        print("Error: File not found. Please check the file path and try again.")
        return None
    except pd.errors.EmptyDataError:
        print("Error: The file is empty. Please provide a valid CSV file.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None


def view_transactions(data):
    if data is not None:
        print(data)
    else:
        print("No data loaded. Please import a CSV first.")
def view_transactions_by_date(data):
    if data is not None:
        try:
            start_date = pd.to_datetime(input("Enter start date (YYYY-MM-DD): "))
            end_date = pd.to_datetime(input("Enter end date (YYYY-MM-DD): "))
            filtered = data[(pd.to_datetime(data["Date"]) >= start_date) &
                            (pd.to_datetime(data["Date"]) <= end_date)]
            print(filtered)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("No data loaded. Please import a CSV file first.")


def add_transaction(data):
    if data is not None:
        try:
            # Input transaction details
            Date = input("Enter date (YYYY-MM-DD): ").strip()
            Description = input("Enter description: ").strip()

            # Validate the type input
            Type = input("Enter type (Debit or Credit): ").strip().capitalize()
            if Type not in ["Debit", "Credit"]:
                print("Invalid type. Please enter 'Debit' or 'Credit'.")
                return data

            Amount = float(input("Enter amount: ").strip())

            if Type == "Debit" and Amount > 0:
                Amount = -Amount
            elif Type == "Credit" and Amount < 0:
                Amount = abs(Amount)

            # Create a new row as a dictionary
            new_row = {"Date": Date, "Description": Description, "Type": Type, "Amount": Amount}
            new_row_df = pd.DataFrame([new_row])

            data = pd.concat([data, new_row_df], ignore_index=True)

            print("Transaction added successfully!")
            return data
        except ValueError:
            print("Invalid input. Please enter valid values.")
            return data
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return data
    else:
        print("No data loaded. Please import a CSV file first.")
        return None

def edit_transaction(data):
    if data is not None:
        try:
            index = int(input("Enter the index of the transaction to edit: "))
            if 0 <= index < len(data):
                print("Current transaction details:")
                print(data.loc[index])

                date = input("Enter new date (or press Enter to keep current): ").strip()
                description = input("Enter new description (or press Enter to keep current): ").strip()
                type = input("Enter new type (or press Enter to keep current): ").strip()
                amount = input("Enter new amount (or press Enter to keep current): ").strip()

                if date:
                    data.loc[index, "date"] = date
                if description:
                    data.loc[index, "description"] = description
                if type:
                    data.loc[index, "type"] = type
                if amount:
                    data.loc[index, "amount"] = float(amount)

                print("Transaction updated successfully!")
                return data
            else:
                print("Invalid index.")
                return data
        except Exception as e:
            print(f"Error: {e}")
            return data
    else:
        print("No data loaded. Please import a CSV file first.")
        return None

def delete_transaction(data):
    if data is not None:
        try:
            index = int(input("Enter the index of the transaction to delete: "))
            if 0 <= index < len(data):
                data = data.drop(index=index).reset_index(drop=True)
                print("Transaction deleted successfully!")
                return data
            else:
                print("Invalid index.")
                return data
        except ValueError:
            print("Invalid input. Please enter a valid index.")
            return data
    else:
        print("No data loaded. Please import a CSV file first.")
        return None

