import pandas as pd

def critical_inventory(filename):
    df = pd.read_csv(filename)
    
    total_products = len(df)
    low_stock = df['StockLevel'] < df['ReorderThreshold']
    low_day = df['DaysSinceRestock'] > 30

    low_df = df.loc[low_stock & low_day, 'ProductName']
    critical_products = set(low_df)
    critical_count = len(critical_products)

    return {
        "total_products": total_products,
        "critical_count": critical_count,
        "critical_products": critical_products
    }

result = critical_inventory("labs/lab09/data/inventory.csv")
print(result)