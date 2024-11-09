#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Item {
    int weight, value;
};

bool compare(const Item& a, const Item& b) {
    return (double)a.value / a.weight > (double)b.value / b.weight;
}

double fractionalKnapsack(int W, vector<Item>& items) {
    sort(items.begin(), items.end(), compare);

    double maxProfit = 0.0;
    for (const auto& item : items) {
        if (W == 0) break;
        if (item.weight <= W) {
            maxProfit += item.value;
            W -= item.weight;
        } else {
            maxProfit += item.value * ((double)W / item.weight);
            break;
        }
    }
    return maxProfit;
}

int main() {
    int n, W;
    cout << "Enter number of items and max weight: ";
    cin >> n >> W;
    
    vector<Item> items(n);
    cout << "Enter weight and value of each item:\n";
    for (int i = 0; i < n; i++) {
        cin >> items[i].weight >> items[i].value;
    }

    cout << "Maximum profit: " << fractionalKnapsack(W, items) << endl;
    return 0;
}
