# 📈💲 Personal Finance Tracker App

Objective: This project involves creating an interactive, text-based Personal Finance Tracker App that helps users manage and analyze their spending habits. Users can import a CSV file containing transaction data, perform operations like viewing, adding, editing, and deleting transactions, and analyze spending patterns. The app also includes data visualization capabilities, displaying monthly spending trends and top spending categories.

## 📑 Description
In this project, I developed a program to track my finances, organized into four files. The first file contains the main menu, which allows users to choose different actions related to their finances. The second file includes functions for managing transactions, such as loading a CSV file of bank transactions, viewing all transactions, filtering by date range, and adding, editing, or deleting individual transactions. The third file focuses on spending analysis, offering functions to analyze spending by category, calculate the average monthly spending, and identify the top spending category. Finally, the fourth file provides data visualization, showcasing the monthly spending trend.

## Installation
  1. Clone the repository:
     ```bash
     git clone git@github.com:pedrinhomendes/personal-finance-tracker.git

  2. Install dependencies:
     ```bash
     pip install -r requirements.txt
     

- Source: [Personal bank file](Student_Banking_Advantage_Plan_.csv)
- Format: CSV
- Size: 69 rows, 4 columns

## Tools and Libraries
- Python
  - Pandas
  - Matplotlib

## 💻 Usage
  1. Run the following command to start the application:
      ```bash
      python Personal_Finance_project.py

## 📂 Example CSV File

Here is an example of the CSV file format used to track expenses and income. This file includes 5 rows of the dataset:

| Date       | Category   | Type                  | Amount  |
|------------|------------|-----------------------|---------|
| 2024-11-18 | Grocery    | Debit                 | -20.6   |
| 2024-11-16 | Food       | Debit                 | -16.38  |
| 2024-11-15 | Food       | Debit                 | -36.84  |
| 2024-11-15 | Extra bill | Debit                 | -33.2   |
| 2024-11-15 | Salary     | Credit                | 589.82  |

Columns:
- Date: Transaction date (YYYY-MM-DD format).
- Category: Transaction Classification (e.g. , Grocery, Salary, Food).
- Type: Classification as Debit or Credit
- Amount: Expense or Income Amount

## Features

## License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/pedrinhomendes/personal-finance-tracker/blob/main/LICENSE) file for details.

