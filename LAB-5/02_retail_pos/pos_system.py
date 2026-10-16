"""Retail Point of Sale & Discount Tracker System."""

import random

PRICE_LIST = {"apple": 12.0, "orange": 15.0, "banana": 8.0}


def print_sales(sales_total):
    """Print the total sales so far."""
    print(f"Sales so far: {sales_total}")


def calculate_bill(cart, tax_rate=0.05, receipts=None):
    """Calculate the total bill including tax and log the transaction."""
    if receipts is None:
        receipts = []
    subtotal = 0.0
    for item, qty in cart.items():
        if not isinstance(qty, (int, float)) or qty < 0:
            continue
        price = PRICE_LIST.get(item, 10.0)
        subtotal += price * qty
    tax = subtotal * tax_rate
    total = subtotal + tax
    receipts.append((random.randint(1, 100), total))  # nosec B311
    return total


def apply_promo_code(sales_total, code):
    """Apply a promotional discount securely without eval()."""
    if code == "total - 50":
        return max(0.0, sales_total - 50.0)
    if code == "total * 0.9":
        return sales_total * 0.9
    return sales_total


def update_stock(item, qty):
    """Update stock levels for an item."""
    if item in PRICE_LIST and isinstance(qty, (int, float)) and qty >= 0:
        return PRICE_LIST[item]
    return 0.0


def log_transaction(receipt_text):
    """Append receipt details to the pos log file with proper encoding."""
    with open("pos_log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(receipt_text + "\n")


def main():
    """Main execution flow for the retail POS system."""
    cart1 = {"apple": 10, "banana": 20}
    bill1 = calculate_bill(cart1)
    print(f"Bill 1: {bill1}")
    cart2 = {"orange": 50}
    bill2 = calculate_bill(cart2)
    print(f"Bill 2: {bill2}")
    sales_total = bill1 + bill2
    code = input("Enter promo code (e.g. total - 50): ") or "total - 50"
    final_total = apply_promo_code(sales_total, code)
    print(f"After your promo: {final_total}")
    print_sales(sales_total)


if __name__ == "__main__":
    main()
