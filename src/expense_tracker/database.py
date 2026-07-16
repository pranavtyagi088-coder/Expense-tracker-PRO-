import sqlite3
import csv
import logging

DB_NAME = "expenses.db"

logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        description TEXT,
        date TEXT NOT NULL
    )
    """)

    conn.commit()

    logging.info("Database initialized")

    conn.close()


def add_expense(amount, category, description, date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO expenses (amount, category, description, date)
        VALUES (?, ?, ?, ?)
    """, (amount, category, description, date))

    conn.commit()
    conn.close()


def view_expenses():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    conn.close()

    return expenses


def category_summary():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, SUM(amount)
        FROM expenses
        GROUP BY category
    """)

    summary = cursor.fetchall()

    conn.close()

    return summary


def delete_expense(expense_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    deleted = cursor.rowcount

    conn.commit()
    conn.close()

    return deleted


def update_expense(expense_id, amount, category, description, date):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE expenses
        SET amount = ?, category = ?, description = ?, date = ?
        WHERE id = ?
    """, (amount, category, description, date, expense_id))

    updated = cursor.rowcount

    conn.commit()
    conn.close()

    return updated


def search_expense(category):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT * FROM expenses
        WHERE category LIKE ?
    """, ('%' + category + '%',))

    expenses = cursor.fetchall()

    conn.close()

    return expenses


def export_to_csv():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    expenses = cursor.fetchall()

    with open("expenses.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Amount",
            "Category",
            "Description",
            "Date"
        ])

        writer.writerows(expenses)

    conn.close()


def export_to_csv():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    with open("expenses.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow([
            "ID",
            "Amount",
            "Category",
            "Description",
            "Date"
        ])

        writer.writerows(expenses)

    conn.close()


def monthly_report(month):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
                   SELECT category, SUM(amount)
                   FROM expenses
                   WHERE date LIKE ?
                   GROUP BY category
                   """, (month + "%",))

    report = cursor.fetchall()

    conn.close()

    return report
def total_expense():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(amount)
        FROM expenses
    """)

    total = cursor.fetchone()[0]

    conn.close()

    return total if total else 0
