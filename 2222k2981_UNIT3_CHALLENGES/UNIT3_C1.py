def linear_search_product(products, target_product):
    indices = []
    for i, product in enumerate(products):
        if product == target_product:
            indices.append(i)
    return indices

# Example usage:
products = ["apple", "banana", "apple", "orange", "grape", "apple"]
target_product = "apple"
result = linear_search_product(products, target_product)
print(result)  # Output: [0, 2, 5]
target_product = "cherry"
result = linear_search_product(products, target_product)
print(result)  # Output: []
