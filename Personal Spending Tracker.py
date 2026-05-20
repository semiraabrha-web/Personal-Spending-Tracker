# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 23:45:33 2026

@author: semir
"""


# -----------------------------
# Personal Spending Tracker
# CPS109 Project
# Problem Description:
# This program is a personal spending tracker that lets users track
# their daily, weekly, and monthly spending. Users can compare their
# spending to a budget and to previous periods, get motivational
# messages and tips, and save reports to files. It supports built-in
# data for testing and manual input for personalized tracking.
# -----------------------------

# -----------------------------
# Categories and budgets
# -----------------------------
categories = ["food", "transport", "others"]  # The categories we are tracking

daily_budget = [10, 5, 5]  # Budget for each category per day
weekly_budget = 100        # Total weekly budget
monthly_budget = 400       # Total monthly budget

# Previous totals to compare
previous_day_total = 15
previous_week_total = 95
previous_month_total = 380

# -----------------------------
# Built-in data examples
# -----------------------------
built_in_day = [12, 3, 6]  # Example daily spending (over budget)
built_in_week = [
    [10, 5, 3],
    [8, 2, 0],
    [12, 0, 1],
    [0, 5, 2],
    [6, 2, 0],
    [7, 3, 1],
    [5, 1, 0]
]
built_in_month = [
    [10,5,3],[8,2,0],[12,0,1],[0,5,2],[6,2,0],[7,3,1],[5,1,0],
    [9,4,2],[7,3,1],[10,1,0],[1,5,2],[5,2,1],[6,3,0],[4,1,0],
    [11,6,2],[8,3,1],[9,0,2],[2,4,1],[7,2,0],[5,3,1],[6,1,0],
    [12,5,3],[9,2,1],[11,1,2],[0,4,0],[6,2,1],[8,3,2],[7,1,0]
]

# -----------------------------
# Function to input daily spending
# -----------------------------
def input_day():
    day = []  # List to store spending for the day
    print("\nEnter your spending for the day:")
    for cat in categories:  # Loop through categories
        while True:
            try:
                val = float(input(f"{cat}: $"))  # Get input from user
                if val < 0:
                    print("Enter a positive number")  # Prevent negative input
                    continue
                day.append(val)
                break
            except:
                print("Invalid input")  # Handle non-number input
    return day

# -----------------------------
# Function to input weekly spending
# -----------------------------
def input_week():
    week = []  # List to store all 7 days
    print("\nEnter your spending for 7 days:")
    for i in range(1, 8):  # Loop for each day
        print(f"\nDay {i}")
        day = []  # Store daily spending
        for cat in categories:
            while True:
                try:
                    val = float(input(f"{cat}: $"))
                    if val < 0:
                        print("Enter a positive number")
                        continue
                    day.append(val)
                    break
                except:
                    print("Invalid input")
        week.append(day)
    return week

# -----------------------------
# Function to input monthly spending
# -----------------------------
def input_month():
    month = []  # Store all 4 weeks
    for w in range(1, 5):
        print(f"\n--- Week {w} ---")
        week = input_week()  # Call input_week() 4 times
        month.append(week)
    return month

# -----------------------------
# Function to analyze daily spending
# -----------------------------
def analyze_day(day, file=None):
    total = sum(day)  # Sum of all categories
    print(f"\nDaily total: ${total:.2f}")
    if file:
        file.write("\n--- Daily Report ---\n")
        file.write(f"Daily total: ${total:.2f}\n")

    # Compare to previous day
    if total > previous_day_total:
        print(f"You spent ${total - previous_day_total:.2f} more than yesterday")
        print("Your wallet is crying. Try to cut back a little.")
        if file:
            file.write(f"More than yesterday by ${total - previous_day_total:.2f}\n")
    else:
        print(f"You spent ${previous_day_total - total:.2f} less than yesterday")
        print("Good job! Keep it up!")
        if file:
            file.write(f"Less than yesterday by ${previous_day_total - total:.2f}\n")

    # Compare to daily budget
    if total > sum(daily_budget):
        print(f"You are over daily budget by ${total - sum(daily_budget):.2f}")
        print("Try to spend less tomorrow.")
        if file:
            file.write(f"Over daily budget by ${total - sum(daily_budget):.2f}\n")
    else:
        print(f"You are under daily budget. You saved ${sum(daily_budget) - total:.2f}")
        print("Nice! Keep it up.")
        if file:
            file.write(f"Under daily budget by ${sum(daily_budget) - total:.2f}\n")

# -----------------------------
# Function to analyze weekly spending
# -----------------------------
def analyze_week(week, file=None):
    total = sum(sum(day) for day in week)  # Sum for the week
    print(f"\nWeekly total: ${total:.2f}")
    if file:
        file.write("\n--- Weekly Report ---\n")
        file.write(f"Weekly total: ${total:.2f}\n")

    # Compare to previous week
    if total > previous_week_total:
        print(f"You spent ${total - previous_week_total:.2f} more than last week")
        print("Your wallet is crying. Try to cut back a little.")
        if file:
            file.write(f"More than last week by ${total - previous_week_total:.2f}\n")
    else:
        print(f"You spent ${previous_week_total - total:.2f} less than last week")
        print("Good job! Keep it up!")
        if file:
            file.write(f"Less than last week by ${previous_week_total - total:.2f}\n")

    # Compare to weekly budget
    if total > weekly_budget:
        print(f"You are over budget by ${total - weekly_budget:.2f}")
        print("Be careful. Small expenses add up quickly.")
        if file:
            file.write(f"Over weekly budget by ${total - weekly_budget:.2f}\n")
    else:
        print(f"You are under budget. You saved ${weekly_budget - total:.2f}")
        print("Nice! Keep it up!")
        if file:
            file.write(f"Under weekly budget by ${weekly_budget - total:.2f}\n")

# -----------------------------
# Function to analyze monthly spending
# -----------------------------
def analyze_month(month, file=None):
    total = sum(sum(day) for week in month for day in week)
    print(f"\nMonthly total: ${total:.2f}")
    if file:
        file.write("\n--- Monthly Report ---\n")
        file.write(f"Monthly total: ${total:.2f}\n")

    # Compare to previous month
    if total > previous_month_total:
        print(f"You spent ${total - previous_month_total:.2f} more than last month")
        print("This is not looking good. Try to control your spending.")
        if file:
            file.write(f"More than last month by ${total - previous_month_total:.2f}\n")
    else:
        print(f"You spent ${previous_month_total - total:.2f} less than last month")
        print("Good job! Keep it up!")
        if file:
            file.write(f"Less than last month by ${previous_month_total - total:.2f}\n")

    # Compare to monthly budget
    if total > monthly_budget:
        print(f"You are over budget by ${total - monthly_budget:.2f}")
        print("Be careful. Small expenses add up quickly.")
        if file:
            file.write(f"Over monthly budget by ${total - monthly_budget:.2f}\n")
    else:
        print(f"You are under budget. You saved ${monthly_budget - total:.2f}")
        print("Nice! Keep it up!")
        if file:
            file.write(f"Under monthly budget by ${monthly_budget - total:.2f}\n")

# -----------------------------
# Main Program Loop
# -----------------------------
print("Welcome to your Personal Spending Tracker!")

while True:
    print("\nOptions: daily / week / month / manual / exit")
    choice = input("What do you want to do? ").lower()

    if choice == "daily":
        sub_choice = input("Built-in or manual? ").lower()
        if sub_choice == "built-in":
            analyze_day(built_in_day)
        elif sub_choice == "manual":
            day = input_day()
            with open("manual.txt", "a") as file:
                analyze_day(day, file)
        else:
            print("Invalid option")

    elif choice == "week":
        sub_choice = input("Built-in or manual? ").lower()
        if sub_choice == "built-in":
            analyze_week(built_in_week)
        elif sub_choice == "manual":
            week = input_week()
            with open("manual.txt", "a") as file:
                analyze_week(week, file)
        else:
            print("Invalid option")

    elif choice == "month":
        sub_choice = input("Built-in or manual? ").lower()
        if sub_choice == "built-in":
            month = [built_in_month[i:i+7] for i in range(0, 28, 7)]
            analyze_month(month)
        elif sub_choice == "manual":
            month = input_month()
            with open("manual.txt", "a") as file:
                analyze_month(month, file)
        else:
            print("Invalid option")

    elif choice == "manual":
        print("You can select daily, week, or month in the next step.")

    elif choice == "exit":
        print("\nThank you for using Spending Tracker!")
        break

    else:
        print("Invalid choice, try again.")