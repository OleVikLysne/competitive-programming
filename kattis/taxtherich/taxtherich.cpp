#include <stdio.h>
#include <vector>
#include <iostream>


class FenwickTree {
private:
    std::vector<int> tree;
    int size;

public:
    FenwickTree(int n) {
        size = n;
        tree.resize(n + 1, 0); 
    }

    void update(int i, int delta) {
        i += 1;
        while (i <= size) {
            tree[i] += delta;
            i += i & -i;
        }
    }

    int query(int r) {
        r += 1;
        int sum = 0;
        while (r > 0) {
            sum += tree[r];
            r -= r & -r;
        }
        return sum;
    }
};

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL); std::cout.tie(NULL);
    int n;
    scanf("%d", &n);
    long total = 0;
    int app = 0;
    FenwickTree tree(10001);

    for (int i=1; i <= n; ++i) {
        int x;
        scanf("%d", &x);
        total += x;
        tree.update(x, 1);
        int avg = (total + i - 1) / i;
        if (tree.query(avg-1) > i / 2) {
            app++;
        }
    }
    std::cout << app << std::endl;
}