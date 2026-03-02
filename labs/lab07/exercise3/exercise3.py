def compare_prices(store_a, store_b):
    results = {
        "only_a" : [],
        "a_cheaper" : [],
        "b_cheaper" : []
    }

    for product, price_a in store_a.items():
        if product not in store_b:
            results["only_a"].append(product)
        else:
            price_b = store_b[product]
            if price_a < price_b:
                results["a_cheaper"].append(product)
            elif price_b < price_a:
                results["b_cheaper"].append(product)

    results["only_a"].sort()
    results["a_cheaper"].sort()
    results["b_cheaper"].sort()

    return results

store_a = {"milk": 3.50, "bread": 2.00, "eggs": 5.00, "butter": 4.50}
store_b = {"milk": 3.00, "bread": 2.50, "eggs": 5.00, "coffee": 8.00}
result = compare_prices(store_a, store_b)
print(result["only_a"])
print(result["a_cheaper"])
print(result["b_cheaper"])
