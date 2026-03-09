# Lab 08 Exercise 5: Sales Summary
# Write your code below:
import csv

def summarize_sales(input_file, output_file):
    """
    Calculate sales statistics: total, average, highest, and lowest revenue.

    Args:
        input_file: path to sales CSV (product,quantity,price)
        output_file: path to output text file

    Returns:
        tuple: (total, average, highest, lowest)
    """
    total_revenue = 0.0
    revenues = []
    
    infile = open(input_file, 'r')
    reader = csv.reader(infile)
    
    next(reader)

    for row in reader:
        quantity = int(row[1].strip())
        price = float (row[2].strip())
        revenue = quantity * price

        revenues.append(revenue)
        total_revenue += revenue
        
    infile.close()
    
    count = len(revenues)
    average_revenue = total_revenue / count
    highest_revenue = max(revenues)
    lowest_revenue = min(revenues)
    
    outfile = open(output_file, 'w')
    outfile.write(f"Total Revenue: ${total_revenue:.2f}\n")
    outfile.write(f"Average Revenue: ${average_revenue:.2f}\n")
    outfile.write(f"Highest Revenue: ${highest_revenue:.2f}\n")
    outfile.write(f"Lowest Revenue: ${lowest_revenue:.2f}\n")
    outfile.close()
    
    return (total_revenue, average_revenue, highest_revenue, lowest_revenue)

# Test your code here
result = summarize_sales("labs/lab08/exercise5/data/sales.csv", "labs/lab08/exercise5/data/summary.txt")
print(f"Total: ${result[0]:.2f}, Avg: ${result[1]:.2f}, High: ${result[2]:.2f}, Low: ${result[3]:.2f}")
