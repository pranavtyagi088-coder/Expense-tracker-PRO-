from expense_tracker.database import (
    init_db,
    add_expense,
    view_expenses,
    category_summary,
    delete_expense,
    update_expense,
    search_expense,
    export_to_csv,
    monthly_report,
    total_expense
)

from expense_tracker.validation import (
    validate_amount,
    validate_category,
    validate_date
)

from expense_tracker.charts import (
    pie_chart,
    bar_chart
)


def display_expenses(expenses):
    print("\n===== Expenses =====")
    print("-" * 70)
    print(f"{'ID':<5}{'Amount':<10}{'Category':<15}{'Description':<20}{'Date'}")
    print("-" * 70)

    for expense in expenses:
        print(
            f"{expense[0]:<5}"
            f"{expense[1]:<10}"
            f"{expense[2]:<15}"
            f"{expense[3]:<20}"
            f"{expense[4]}"
        )

    print("-" * 70)


def main():
    init_db()

    while True:

        print("\n========= Expense Tracker =========")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Delete Expense")
        print("5. Edit Expense")
        print("6. Search Expense")
        print("7. Export CSV")
        print("8. Monthly Report")
        print("9. Total Expense")
        print("10. Pie Chart")
        print("11. Bar Chart")
        print("12. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            amount = input("Enter amount: ")

            if not validate_amount(amount):
                print("❌ Invalid amount!")
                continue

            category = input("Enter category: ")

            if not validate_category(category):
                print("❌ Category cannot be empty!")
                continue

            description = input("Enter description: ")

            date = input("Enter date (YYYY-MM-DD): ")

            if not validate_date(date):
                print("❌ Invalid date format!")
                continue

            add_expense(
                float(amount),
                category,
                description,
                date
            )

            print("✅ Expense added successfully!")

        elif choice == "2":

            expenses = view_expenses()

            if expenses:
                display_expenses(expenses)
            else:
                print("\nNo expenses found.")

        elif choice == "3":

            summary = category_summary()

            if summary:

                print("\n===== Category Summary =====")
                print("-" * 35)
                print(f"{'Category':<20}{'Total'}")
                print("-" * 35)

                for category, total in summary:
                    print(f"{category:<20}₹{total}")

                print("-" * 35)

            else:
                print("\nNo expenses found.")

        elif choice == "4":

            try:
                expense_id = int(input("Enter Expense ID to delete: "))
            except ValueError:
                print("❌ Invalid ID")
                continue

            confirm = input("Are you sure? (y/n): ").lower()

            if confirm in ("y", "yes"):

                result = delete_expense(expense_id)

                if result:
                    print("✅ Expense deleted successfully!")
                else:
                    print("❌ Expense ID not found!")

            else:
                print("Deletion cancelled.")

        elif choice == "5":

            try:
                expense_id = int(input("Enter Expense ID to edit: "))
            except ValueError:
                print("❌ Invalid ID")
                continue

            amount = input("Enter new amount: ")

            if not validate_amount(amount):
                print("❌ Invalid amount!")
                continue

            category = input("Enter new category: ")

            if not validate_category(category):
                print("❌ Category cannot be empty!")
                continue

            description = input("Enter new description: ")

            date = input("Enter new date (YYYY-MM-DD): ")

            if not validate_date(date):
                print("❌ Invalid date!")
                continue

            result = update_expense(
                expense_id,
                float(amount),
                category,
                description,
                date
            )

            if result:
                print("✅ Expense updated successfully!")
            else:
                print("❌ Expense ID not found!")

        elif choice == "6":

            category = input("Enter category to search: ")

            expenses = search_expense(category)

            if expenses:
                display_expenses(expenses)
            else:
                print("\nNo matching expenses found.")

        elif choice == "7":

            export_to_csv()

            print("\n✅ Expenses exported successfully!")
            print("File saved as expenses.csv")

        elif choice == "8":

            month = input("Enter month (YYYY-MM): ")

            report = monthly_report(month)

            if report:

                print("\n===== Monthly Report =====")
                print("-" * 35)
                print(f"{'Category':<20}{'Total'}")
                print("-" * 35)

                grand_total = 0

                for category, amount in report:
                    print(f"{category:<20}₹{amount}")
                    grand_total += amount

                print("-" * 35)
                print(f"Grand Total: ₹{grand_total}")

            else:
                print("\nNo expenses found for this month.")

        elif choice == "9":

            total = total_expense()

            print(f"\n💰 Total Expense: ₹{total}")

        elif choice == "10":

            pie_chart()

        elif choice == "11":

            bar_chart()

        elif choice == "12":

            print("\n👋 Goodbye!")
            break

        else:

            print("❌ Invalid choice!")


if __name__ == "__main__":
    main()