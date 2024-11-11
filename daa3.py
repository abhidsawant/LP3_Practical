class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def compare(item):
    # Calculate the value-to-weight ratio for sorting
    return item.value / item.weight

def fractional_knapsack(W, items):
    # Sort items by value-to-weight ratio in descending order
    items.sort(key=compare, reverse=True)

    current_weight = 0  # Current weight in knapsack
    total_value = 0.0   # Total value in knapsack

    # Process each item
    for item in items:
        if current_weight + item.weight <= W:
            # If item can be added fully, add its weight and value
            current_weight += item.weight
            total_value += item.value
        else:
            # Take the fraction of the remaining capacity
            remaining_capacity = W - current_weight
            total_value += item.value * (remaining_capacity / item.weight)
            break  # No more items can be taken after this

    return total_value

# Main function
if __name__ == "__main__":
    n = int(input("Enter the number of items: "))
    items = []

    # Input item weights and values
    print("Enter the weight and value of each item:")
    for i in range(n):
        weight, value = map(int, input(f"Item {i + 1} weight and value: ").split())
        items.append(Item(weight, value))

    W = int(input("Enter the capacity of the knapsack: "))

    # Calculate maximum value
    max_value = fractional_knapsack(W, items)
    print("Maximum value the thief can carry:", max_value)
