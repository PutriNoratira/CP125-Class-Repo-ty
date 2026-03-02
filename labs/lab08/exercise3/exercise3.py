# Lab 08 Exercise 3: Product Price Lookup
# Write your code below:
import csv

def calculate_order_total(products_file, order_file, output_file):
    """
    Calculate total cost for each product in order.

    Args:
        products_file: path to products CSV (product_id,product_name,price)
        order_file: path to order CSV (product_id,quantity)
        output_file: path to output CSV file

    Returns:
        float: grand total of all orders
    """
    grand_total = 0.0
    prices = {}

    p_file = open(products_file, 'r')
    p_reader = csv.reader(p_file)
    
    is_header = True
    for row in p_reader:
        if is_header:
            is_header = False
            continue
        pid = row[0]
        price = float(row[2])
        prices[pid] = price
    p_file.close()

    o_file = open(order_file, 'r')
    out_file = open(output_file, 'w', newline='')
    
    o_reader = csv.reader(o_file)
    out_writer = csv.writer(out_file)
    
    out_writer.writerow(["product_id", "total_cost"])
    
    is_header = True
    for row in o_reader:
        if is_header:
            is_header = False
            continue
        pid = row[0]
        quantity = int(row[1])
        
        item_total = prices[pid] * quantity
        grand_total += item_total
        
        out_writer.writerow([pid, f"{item_total:.2f}"])
            
    o_file.close()
    out_file.close()

    return grand_total

# Test your code here
result = calculate_order_total("labs/lab08/exercise3/data/products.csv", "labs/lab08/exercise3/data/order.csv", "labs/lab08/exercise3/data/total.csv")
print(f"Grand total: ${result:.2f}")
