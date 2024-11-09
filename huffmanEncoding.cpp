#include <iostream>
#include <queue>
#include <vector>
#include <string>

using namespace std;

// Node class to represent each character and its frequency
class Node {
public:
    int freq;
    string symbol;
    Node* left;
    Node* right;
    string huff;

    Node(int f, string s, Node* l = nullptr, Node* r = nullptr) 
        : freq(f), symbol(s), left(l), right(r), huff("") {}

    // Overload the less-than operator for priority queue sorting
    bool operator<(const Node& other) const {
        return freq > other.freq; // For min-heap, use freq < other.freq
    }
};

// Recursive function to print Huffman codes from the tree
void printNodes(Node* node, string val = "") {
    string newval = val + node->huff;
    if (node->left) {
        printNodes(node->left, newval);
    }
    if (node->right) {
        printNodes(node->right, newval);
    }
    if (!node->left && !node->right) {
        cout << node->symbol << " -> " << newval << endl;
    }
}

int main() {
    vector<string> chars = {"a", "b", "c", "d", "e", "f"};
    vector<int> freqs = {5, 9, 12, 13, 16, 45};

    // Priority queue to implement min-heap
    auto compare = [](Node* left, Node* right) { return left->freq > right->freq; };
    priority_queue<Node*, vector<Node*>, decltype(compare)> nodes(compare);

    // Insert all characters and their frequencies into the priority queue
    for (int i = 0; i < chars.size(); i++) {
        nodes.push(new Node(freqs[i], chars[i]));
    }

    // Combine nodes until only one node remains
    while (nodes.size() > 1) {
        Node* left = nodes.top();
        nodes.pop();
        Node* right = nodes.top();
        nodes.pop();

        // Assign '0' and '1' to left and right children
        left->huff = "0";
        right->huff = "1";

        // Combine the nodes
        Node* newnode = new Node(left->freq + right->freq, left->symbol + right->symbol, left, right);
        nodes.push(newnode);
    }

    // Print Huffman codes for each character
    printNodes(nodes.top());

    // Clean up allocated nodes
    delete nodes.top();

    return 0;
}
