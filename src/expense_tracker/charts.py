import matplotlib.pyplot as plt
from expense_tracker.database import category_summary


def pie_chart():
    data = category_summary()

    if not data:
        print("No data available.")
        return

    labels = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(6, 6))
    plt.pie(amounts, labels=labels, autopct="%1.1f%%")
    plt.title("Expense Distribution")
    plt.show()


def bar_chart():
    data = category_summary()

    if not data:
        print("No data available.")
        return

    labels = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(8, 5))
    plt.bar(labels, amounts)
    plt.title("Expenses by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()