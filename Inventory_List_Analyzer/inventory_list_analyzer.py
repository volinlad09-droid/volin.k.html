#python
"""
Inventory List Analyzer – Store Stock Review

A simple CSV-based inventory analyzer.

Input CSV columns:
    Item, Category, Quantity, Reorder_Level, Unit_Price

Example:
    Rice,Groceries,25,10,55.50
    Sugar,Groceries,6,10,48.00
    Soap,Household,18,8,32.00

Run:
    python inventory_list_analyzer.py inventory.csv
"""

import argparse
import csv
from collections import defaultdict


REQUIRED_COLUMNS = {
    "Item",
    "Category",
    "Quantity",
    "Reorder_Level",
    "Unit_Price",
}


def load_inventory(filename):
    with open(filename, "r", newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)

        if not reader.fieldnames:
            raise ValueError("CSV file has no header row.")

        missing = REQUIRED_COLUMNS - set(reader.fieldnames)
        if missing:
            raise ValueError(
                "Missing required columns: " + ", ".join(sorted(missing))
            )

        rows = []
        for line_no, row in enumerate(reader, start=2):
            try:
                item = row["Item"].strip()
                category = row["Category"].strip()
                quantity = int(float(row["Quantity"]))
                reorder_level = int(float(row["Reorder_Level"]))
                unit_price = float(row["Unit_Price"])

                if not item:
                    raise ValueError("Item name is empty.")
                if quantity < 0 or reorder_level < 0 or unit_price < 0:
                    raise ValueError("Quantity, reorder level and price must be >= 0.")

                row_data = {
                    "Item": item,
                    "Category": category,
                    "Quantity": quantity,
                    "Reorder_Level": reorder_level,
                    "Unit_Price": unit_price,
                    "Stock_Value": quantity * unit_price,
                }
                rows.append(row_data)

            except (ValueError, TypeError) as exc:
                raise ValueError(f"Invalid data on CSV line {line_no}: {exc}") from exc

    return rows


def analyze(rows):
    total_items = len(rows)
    total_units = sum(r["Quantity"] for r in rows)
    total_stock_value = sum(r["Stock_Value"] for r in rows)

    low_stock = [
        r for r in rows
        if r["Quantity"] <= r["Reorder_Level"]
    ]

    out_of_stock = [r for r in rows if r["Quantity"] == 0]

    category_stats = defaultdict(lambda: {
        "items": 0,
        "units": 0,
        "value": 0.0,
    })

    for r in rows:
        stats = category_stats[r["Category"]]
        stats["items"] += 1
        stats["units"] += r["Quantity"]
        stats["value"] += r["Stock_Value"]

    top_value = sorted(rows, key=lambda r: r["Stock_Value"], reverse=True)

    return {
        "total_items": total_items,
        "total_units": total_units,
        "total_stock_value": total_stock_value,
        "low_stock": low_stock,
        "out_of_stock": out_of_stock,
        "category_stats": dict(category_stats),
        "top_value": top_value,
    }


def print_report(report):
    print("\n" + "=" * 60)
    print("INVENTORY LIST ANALYZER – STORE STOCK REVIEW")
    print("=" * 60)

    print(f"Total inventory items : {report['total_items']}")
    print(f"Total units in stock  : {report['total_units']}")
    print(f"Total stock value     : ₹{report['total_stock_value']:,.2f}")
    print(f"Low-stock items       : {len(report['low_stock'])}")
    print(f"Out-of-stock items    : {len(report['out_of_stock'])}")

    print("\n--- LOW STOCK / REORDER ALERTS ---")
    if report["low_stock"]:
        for r in report["low_stock"]:
            status = "OUT OF STOCK" if r["Quantity"] == 0 else "REORDER"
            print(
                f"{status:14} | {r['Item']:<25} | "
                f"Qty: {r['Quantity']:<5} | Reorder level: {r['Reorder_Level']}"
            )
    else:
        print("No low-stock items.")

    print("\n--- CATEGORY SUMMARY ---")
    if report["category_stats"]:
        for category, stats in sorted(report["category_stats"].items()):
            print(
                f"{category:<20} | Items: {stats['items']:<4} | "
                f"Units: {stats['units']:<6} | Value: ₹{stats['value']:,.2f}"
            )
    else:
        print("No categories found.")

    print("\n--- TOP 10 ITEMS BY STOCK VALUE ---")
    for r in report["top_value"][:10]:
        print(
            f"{r['Item']:<25} | Qty: {r['Quantity']:<6} | "
            f"Unit price: ₹{r['Unit_Price']:>9,.2f} | "
            f"Stock value: ₹{r['Stock_Value']:>12,.2f}"
        )

    print("\n" + "=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze a store inventory CSV and show stock/reorder insights."
    )
    parser.add_argument(
        "csv_file",
        help="Path to inventory CSV file",
    )
    args = parser.parse_args()

    try:
        rows = load_inventory(args.csv_file)
        report = analyze(rows)
        print_report(report)
    except FileNotFoundError:
        print(f"Error: File not found: {args.csv_file}")
        raise SystemExit(1)
    except ValueError as exc:
        print(f"Error: {exc}")
        raise SystemExit(1)


if __name__ == "__main__":
    main()
