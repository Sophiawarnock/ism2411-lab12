
# Reflection 1: Python can automate repeated data tasks and handle larger
# workflows more easily than Excel. Excel is useful for visually exploring
# data, making charts, and performing quick calculations.

# Reflection 2: A business could keep a daily sales log. Append mode adds
# each new entry without deleting previous entries, creating a running history.

import csv
from datetime import datetime

# EXERCISE 2: Read and print raw rows
with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)

    for row in reader:
        print(row)

# EXERCISE 3: Skip the header
with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.reader(infile)

    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)

# EXERCISE 4: Compute totals
total_revenue = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])

        total = price * quantity
        total_revenue += total

        print(f"{product}: {quantity} units x ${price:.2f} = ${total:.2f}")

print(f"Total revenue: ${total_revenue:.2f}")

# EXERCISE 5: Filter and write
original_count = 0
written_count = 0

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.DictReader(infile)

    with open("data/cleaned.csv", "w", newline="") as outfile:
        fieldnames = ["Product", "Price", "Qty", "Total"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            original_count += 1
            price = float(row["price"])
            quantity = int(row["quantity"])
            total = price * quantity

            if total > 100:
                writer.writerow({
                    "Product": row["product"],
                    "Price": price,
                    "Qty": quantity,
                    "Total": total
                })
                written_count += 1

print("Original rows:", original_count)
print("Rows written:", written_count)

# EXERCISE 6: csv.DictReader
# reader uses numeric positions; DictReader uses column names.
# Use reader for simple positional data and DictReader when named columns
# make the code easier to understand.

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        total = float(row["price"]) * int(row["quantity"])
        print(row["product"], total)

# EXERCISE 7: Sales summary by product
summary = {}

with open("data/sales.csv", "r", newline="") as infile:
    reader = csv.DictReader(infile)

    for row in reader:
        product = row["product"]
        total = float(row["price"]) * int(row["quantity"])

        if product in summary:
            summary[product] += total
        else:
            summary[product] = total

for product in sorted(summary):
    print(product, f"${summary[product]:.2f}")

# EXERCISE 8: Append mode log
with open("data/run_log.txt", "a") as logfile:
    logfile.write(
        f"{datetime.now()} - Total revenue: ${total_revenue:.2f}\n"
    )

print("Sales report completed!")
