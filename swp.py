import sys
import argparse
import pandas as pd
from datetime import datetime
from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference

def get_input(prompt):
    return input(prompt)

def calculate_swp(principal, tenure_years, annual_interest, monthly_withdraw):
    tenure_months = tenure_years * 12
    monthly_interest_rate = (annual_interest / 100) / 12
    current_amount = principal
    report = []
    total_withdrawn = 0

    for month in range(1, tenure_months + 1):
        interest_for_month = current_amount * monthly_interest_rate
        current_amount += interest_for_month

        if month > 1:  # Withdrawals start from the second month
            current_amount -= monthly_withdraw
            total_withdrawn += monthly_withdraw

        report.append({
            "Month": month,
            "Current Amount": current_amount,
            "Monthly Interest": interest_for_month,
            "Monthly Withdraw": monthly_withdraw,
        })

    total_earned = current_amount - principal + total_withdrawn
    return report, current_amount, total_withdrawn, total_earned

def save_to_excel(report, current_amount, total_withdrawn, total_earned):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"SWP_Report_{timestamp}.xlsx"
    
    df = pd.DataFrame(report)
    df.to_excel(filename, index=False, sheet_name='Report')

    summary = {
        "Total Current Amount": current_amount,
        "Total Withdrawn": total_withdrawn,
        "Total Earned": total_earned
    }
    summary_df = pd.DataFrame(summary, index=[0])
    with pd.ExcelWriter(filename, mode='a', engine='openpyxl') as writer:
        summary_df.to_excel(writer, index=False, sheet_name='Summary')

        # Create charts
        workbook = writer.book
        worksheet = workbook['Report']

        # Define a function to create and add a chart
        def create_chart(chart_title, y_col, position):
            chart = LineChart()
            chart.title = chart_title
            chart.style = 13
            chart.x_axis.title = "Month"
            chart.y_axis.title = "Amount"

            # Data for the chart
            data = Reference(worksheet,
                             min_col=y_col,
                             min_row=1,
                             max_row=len(report) + 1,
                             max_col=y_col)
            categories = Reference(worksheet,
                                   min_col=1,
                                   min_row=2,
                                   max_row=len(report) + 1)
            chart.add_data(data, titles_from_data=True)
            chart.set_categories(categories)

            # Add the chart to the worksheet
            worksheet.add_chart(chart, position)

        # Create individual charts for each metric
        create_chart("Current Amount Over Time", 2, "H5")  # Current Amount
        create_chart("Monthly Withdraw Over Time", 3, "H20")  # Monthly Withdraw
        create_chart("Monthly Interest Over Time", 4, "H35")  # Monthly Interest

def print_report(report, current_amount, total_withdrawn, total_earned):
    print("\nTable:")
    print("Month | Current Amount | Monthly Interest | Monthly Withdraw")
    for row in report:
        print(f"{row['Month']:<5} | {row['Current Amount']:<14.2f} | {row['Monthly Interest']:<16.2f} | {row['Monthly Withdraw']:<16.2f}")

    print("\nTotal:")
    print(f"Current amount (after tenure): {current_amount:.2f}")
    print(f"Total withdrawn (till tenure): {total_withdrawn:.2f}")
    print(f"Total earned (Total Withdrawn + Profit): {total_earned:.2f}")

def main():
    parser = argparse.ArgumentParser(description='Calculate Systematic Withdrawal Plan (SWP)')
    parser.add_argument('-P', '--principal', type=float, help='Principal Amount', required=False)
    parser.add_argument('-T', '--tenure', type=int, help='Tenure (in years)', required=False)
    parser.add_argument('-I', '--interest', type=float, help='Annual Interest (%)', required=False)
    parser.add_argument('-W', '--withdraw', type=float, help='Monthly Withdraw Amount', required=False)

    args = parser.parse_args()

    if None in [args.principal, args.tenure, args.interest, args.withdraw]:
        print("Please provide the following details:")
        if args.principal is None:
            args.principal = float(get_input("Enter Principal Amount: "))
        if args.tenure is None:
            args.tenure = int(get_input("Enter Tenure (in years): "))
        if args.interest is None:
            args.interest = float(get_input("Enter Annual Interest (%): "))
        if args.withdraw is None:
            args.withdraw = float(get_input("Enter Monthly Withdraw Amount: "))

    report, current_amount, total_withdrawn, total_earned = calculate_swp(args.principal, args.tenure, args.interest, args.withdraw)
    print_report(report, current_amount, total_withdrawn, total_earned)
    save_to_excel(report, current_amount, total_withdrawn, total_earned)

if __name__ == "__main__":
    main()
