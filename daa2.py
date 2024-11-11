import heapq
from collections import defaultdict

class HuffmanNode:
    def __init__(self, data, freq):
        self.data = data  # Character data
        self.freq = freq  # Frequency of the character
        self.left = None  # Left child in the Huffman tree
        self.right = None # Right child in the Huffman tree

    # Less than function to make nodes comparable by frequency, which allows the use of a priority queue
    def __lt__(self, other):
        
        return self.freq < other.freq

def store_codes(root, code, huffman_codes):
    # Recursively traverse the Huffman Tree and store codes for characters
    if root is None:
        return

    # If it's a leaf node, add the character and its code to the dictionary
    if root.left is None and root.right is None:
        huffman_codes[root.data] = code

    # Traverse left (append '0') and right (append '1') to build the binary code
    store_codes(root.left, code + "0", huffman_codes)
    store_codes(root.right, code + "1", huffman_codes)

def huffman_encoding(data, freq):
    # Step 1: Create a priority queue (min-heap) for Huffman nodes
    min_heap = [HuffmanNode(data[i], freq[i]) for i in range(len(data))]
    heapq.heapify(min_heap)

    # Step 2: Build the Huffman Tree
    while len(min_heap) > 1:
        # Pop the two nodes with the lowest frequency
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)

        # Merge the two nodes by creating a new internal node with the sum of their frequencies
        top = HuffmanNode('$', left.freq + right.freq)
        top.left = left
        top.right = right

        # Push the new node back into the priority queue
        heapq.heappush(min_heap, top)

    # Step 3: Store the Huffman codes
    huffman_codes = {}
    store_codes(min_heap[0], "", huffman_codes)

    # Step 4: Print the Huffman Codes
    print("Huffman Codes:")
    for char, code in huffman_codes.items():
        print(f"{char}: {code}")

    return huffman_codes

# Main function
data = ['a', 'b', 'c', 'd', 'e', 'f']
freq = [5, 9, 12, 13, 16, 45]
huffman_codes = huffman_encoding(data, freq)
``