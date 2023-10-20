def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item['value_per_weight'] = item['value'] / item['weight']
    
    # Sort items in non-increasing order of value-to-weight ratio
    items.sort(key=lambda x: x['value_per_weight'], reverse=True)
    
    total_value = 0
    knapsack = []

    for item in items:
        if item['weight'] <= capacity:
            total_value += item['value']
            knapsack.append(item)
            capacity -= item['weight']
        else:
            fraction = capacity / item['weight']
            total_value += fraction * item['value']
            knapsack.append({'item': item['item'], 'weight': item['weight']*fraction, 'value': item['value']*fraction})
            break
    
    return total_value, knapsack


# Example Usage
items = [
    {'item': 'Item 1', 'weight': 10, 'value': 60},
    {'item': 'Item 2', 'weight': 20, 'value': 100},
    {'item': 'Item 3', 'weight': 30, 'value': 120},
]

capacity = 50

total_value, knapsack_items = fractional_knapsack(items, capacity)

print(f'Total value in the knapsack: {total_value}')
print('Selected items:')
for item in knapsack_items:
    print(f"Item: {item['item']}, Weight: {item['weight']}, Value: {item['value']}")
