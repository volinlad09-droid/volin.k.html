#!/usr/bin/env python3
"""
Inventory List Analyzer – Store Stock Review

A small command-line tool for reviewing store inventory from a CSV file.

CSV columns expected:
SKU, Product, Category, Quantity, Reorder_Level, Unit_Price

Example:
SKU,Product,Category,Quantity,Reorder_Level,Unit_Price
A001,Notebook,Stationery,25,10,80
A002,Pen,Stationery,6,10,20
A003,Chair,Furniture,0,2,2500

Run:
    python inventory_analyzer.py inventory.csv

Optional:
    python inventory_analyzer.py inventory.csv --output report.csv
"""

import argparse
import csv
from pathlib import Path


REQUIRED_COLUMNS = {
    "SKU",
    "Product",
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
                "Missing columns: " + ", ".join(sorted(missing))
            )

        items = []
        for row_number, row in enumerate(reader, start=2):
            try:
                quantity = int(float(row["Quantity"]))
                reorder_level = int(float(row["Reorder_Level"]))
                unit_price = float(row["Unit_Price"])
            except (TypeError, ValueError) as exc:
                raise ValueError(
                    f"Invalid numeric value on CSV row {row_number}: {exc}"
                ) from exc

            items.append(
                {
                    "SKU": row["SKU"].strip(),
                    "Product": row["Product"].strip(),
                    "Category": row["Category"].strip(),
                    "Quantity": quantity,
                    "Reorder_Level": reorder_level,
                    "Unit_Price": unit_price,
                }
            )

    return items


def analyze(items):
    for item in items:
        if item["Quantity"] <= 0:
            status = "OUT OF STOCK"
        elif item["Quantity"] <= item["Reorder_Level"]:
            status = "REORDER"
        else:
            status = "OK"

        item["Stock_Value"] = item["Quantity"] * item["Unit_Price"]
        item["Status"] = status

    total_value = sum(i["Stock_Value"] for i in items)
    out_of_stock = [i for i in items if i["Status"] == "OUT OF STOCK"]
    reorder = [i for i in items if i["Status"] == "REORDER"]
    low_stock = out_of_stock + reorder

    categories = {}
    for item in items:
        category = item["Category"] or "Uncategorized"
        categories.setdefault(category, {"items": 0, "quantity": 0, "value": 0.0})
        categories[category]["items"] += 1
        categories[category]["quantity"] += item["Quantity"]
        categories[category]["value"] += item["Stock_Value"]

    return {
        "total_items": len(items),
        "total_units": sum(i["Quantity"] for i in items),
        "total_value": total_value,
        "out_of_stock": out_of_stock,
        "reorder": reorder,
        "low_stock": low_stock,
        "categories": categories,
    }


def print_report(result):
    print("\n" + "=" * 60)
    print("INVENTORY LIST ANALYZER – STORE STOCK REVIEW")
    print("=" * 60)

    print(f"Products       : {result['total_items']}")
    print(f"Units in stock : {result['total_units']}")
    print(f"Stock value    : ₹{result['total_value']:,.2f}")
    print(f"Reorder items  : {len(result['reorder'])}")
    print(f"Out of stock   : {len(result['out_of_stock'])}")

    if result["low_stock"]:
        print("\nSTOCK ATTENTION")
        print("-" * 60)
        for item in result["low_stock"]:
            print(
                f"{item['SKU']:12} {item['Product'][:25]:25} "
                f"Qty: {item['Quantity']:5}  {item['Status']}"
            )
    else:
        print("\nAll products are above their reorder levels.")

    print("\nCATEGORY SUMMARY")
    print("-" * 60)
    for category, data in sorted(result["categories"].items()):
        print(
            f"{category[:25]:25} "
            f"Products: {data['items']:4}  "
            f"Units: {data['quantity']:6}  "
            f"Value: ₹{data['value']:,.2f}"
        )

    print("=" * 60)


def export_report(items, filename):
    fields = [
        "SKU",
        "Product",
        "Category",
        "Quantity",
        "Reorder_Level",
        "Unit_Price",
        "Stock_Value",
        "Status",
    ]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(items)


def main():
    parser = argparse.ArgumentParser(
        description="Analyze store inventory and identify stock requiring attention."
    )
    parser.add_argument("inventory", help="Path to the inventory CSV file")
    parser.add_argument(
        "--output",
        default="inventory_report.csv",
        help="Output CSV report (default: inventory_report.csv)",
    )
    args = parser.parse_args(25)

    try:
        items = load_inventory(args.inventory)
        if not items:
            print("No inventory records found.")
            return

        result = analyze(items)
        print_report(result)
        export_report(items, args.output)
        print(f"\nDetailed report saved to: {args.output}")

    except FileNotFoundError:
        print(f"Error: File not found: {args.inventory}")
    except ValueError as exc:
        print(f"Error: {exc}")


if __name__ == "__main__":
    main()
