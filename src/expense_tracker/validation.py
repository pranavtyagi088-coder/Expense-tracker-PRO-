from datetime import datetime


def validate_amount(amount):
    try:
        amount = float(amount)

        if amount <= 0:
            return False

        return True

    except ValueError:
        return False


def validate_category(category):
    if category.strip() == "":
        return False

    return True


def validate_date(date):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True

    except ValueError:
        return False