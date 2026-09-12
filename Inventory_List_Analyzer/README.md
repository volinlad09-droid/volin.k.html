# Inventory List Analyzer – Store Stock Review

## What it does
- Reads inventory data from a CSV file.
- Calculates total items, units and stock value.
- Identifies low-stock and out-of-stock products.
- Summarizes stock by category.
- Shows the top 10 products by stock value.

## CSV format
The CSV must contain:
`Item, Category, Quantity, Reorder_Level, Unit_Price`

## Run
```bash
python inventory_list_analyzer.py sample_inventory.csv
```

No external Python packages are required.
