# Inventory List Analyzer – Store Stock Review

## Files
- `inventory_analyzer.py` – main Python program
- `sample_inventory.csv` – sample inventory data

## Run

```bash
python inventory_analyzer.py sample_inventory.csv
```

To choose the output report filename:

```bash
python inventory_analyzer.py sample_inventory.csv --output inventory_report.csv
```

## Stock rules
- `OUT OF STOCK`: Quantity is 0 or less
- `REORDER`: Quantity is at or below Reorder_Level
- `OK`: Quantity is above Reorder_Level

The program also calculates total stock value and category summaries.
