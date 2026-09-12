"""
Project: Inventory List Analyzer – Store Stock Review
Author: CareerX-AI

This program:
- Accepts multiple inventory items from the user
- Validates item names, categories, and quantities
- Uses strings, dictionaries, lists, sets, loops, and conditions
- Searches items/categories using substring logic
- Displays inventory summary and statistics
- Sorts items by quantity and categories alphabetically
"""

def get_non_empty_text(prompt):
    """Read and validate a non-empty text value."""
    while True:
        value = input(prompt).strip().lower()

        if value:
            return value

        print("Input cannot be empty. Please try again.")


def get_positive_quantity(prompt):
    """Read and validate a non-negative integer quantity."""
    while True:
        value = input(prompt).strip()

        if value.isdigit():
            quantity = int(value)

            if quantity >= 0:
                return quantity

        print("Please enter a valid non-negative whole number.")


def collect_inventory():
    """Collect multiple inventory records from the user."""
    inventory = []

    print("\nWelcome to Inventory List Analyzer!")

    while True:
        print("\nEnter item details")

        item_name = get_non_empty_text("Enter item name: ")
        category = get_non_empty_text("Enter category: ")
        quantity = get_positive_quantity("Enter quantity: ")

        item = {
            "name": item_name,
            "category": category,
            "quantity": quantity
        }

        inventory.append(item)

        while True:
            choice = input(
                "\nDo you want to add more items? (y/n): "
            ).strip().lower()

            if choice in ("y", "n"):
                break

            print("Please enter only 'y' or 'n'.")

        if choice == "n":
            break

    return inventory


def display_summary(inventory):
    """Display inventory statistics and summary information."""
    print("\n========== INVENTORY SUMMARY ==========")

    if not inventory:
        print("No inventory items were entered.")
        return

    item_names = [item["name"] for item in inventory]
    quantities = [item["quantity"] for item in inventory]
    categories = {item["category"] for item in inventory}

    total_items = len(inventory)
    total_quantity = sum(quantities)
    average_quantity = total_quantity / total_items
    most_stocked = max(inventory, key=lambda item: item["quantity"])
    least_stocked = min(inventory, key=lambda item: item["quantity"])

    # Dictionary mapping item names to quantities
    item_quantity_map = {
        item["name"]: item["quantity"] for item in inventory
    }

    print(f"\nTotal Different Items: {total_items}")
    print(
        "Explanation: You entered "
        f"{total_items} different items: "
        f"{', '.join(name.title() for name in item_names)}."
    )

    print(f"\nTotal Quantity in Stock: {total_quantity}")
    print(
        "Explanation: Sum of all quantities: "
        f"{' + '.join(str(qty) for qty in quantities)} = "
        f"{total_quantity}"
    )

    print(f"\nAverage Quantity per Item: {average_quantity:.2f}")
    print(
        f"Explanation: Average = {total_quantity} total / "
        f"{total_items} items"
    )

    print(
        f"\nMost Stocked Item: {most_stocked['name'].title()} "
        f"({most_stocked['quantity']} units)"
    )
    print(
        f"Explanation: {most_stocked['name'].title()} has the "
        "highest quantity among all items."
    )

    print(
        f"\nLeast Stocked Item: {least_stocked['name'].title()} "
        f"({least_stocked['quantity']} units)"
    )
    print(
        f"Explanation: {least_stocked['name'].title()} has the "
        "lowest quantity."
    )

    print("\n--------------------------------------")
    print(f"Unique Categories in Inventory: {categories}")
    print(
        "Explanation: Categories are taken from user input and "
        "converted to lowercase. No duplicates are shown here."
    )

    print("\nItem-to-Quantity Dictionary:")
    print(item_quantity_map)


def search_inventory(inventory):
    """Search items or categories using substring logic."""
    if not inventory:
        return

    search_term = input(
        "\nSearch item name or category (press Enter to skip): "
    ).strip().lower()

    if not search_term:
        return

    matches = [
        item for item in inventory
        if search_term in item["name"]
        or search_term in item["category"]
    ]

    print("\n========== SEARCH RESULTS ==========")

    if matches:
        for item in matches:
            print(
                f"- {item['name'].title()} | "
                f"Category: {item['category'].title()} | "
                f"Quantity: {item['quantity']}"
            )
    else:
        print("No matching items or categories found.")


def display_sorted_inventory(inventory):
    """Display items by quantity descending and categories alphabetically."""
    if not inventory:
        return

    print("\n--------------------------------------")
    print("📦 Items Sorted by Quantity (High to Low):")

    sorted_items = sorted(
        inventory,
        key=lambda item: item["quantity"],
        reverse=True
    )

    for index, item in enumerate(sorted_items, start=1):
        print(
            f"{index}. {item['name'].title()} - "
            f"{item['quantity']} units"
        )

    print(
        "\nExplanation: Items are sorted using the quantity "
        "field from highest to lowest."
    )

    print("\n--------------------------------------")
    print("📁 Categories in Alphabetical Order:")

    unique_categories = sorted(
        {item["category"] for item in inventory}
    )

    for index, category in enumerate(unique_categories, start=1):
        print(f"{index}. {category}")

    print(
        "\nExplanation: The set of unique categories was sorted "
        "alphabetically for display."
    )


def main():
    """Run the complete inventory analyzer."""
    inventory = collect_inventory()
    display_summary(inventory)
    search_inventory(inventory)
    display_sorted_inventory(inventory)

    print("\n========== END OF REPORT ==========")


if __name__ == "__main__":
    main()
