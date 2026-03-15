#include <bits/stdc++.h>

const int size = 1000;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(NULL);
    std::cout.tie(NULL);
    int n, q;
    int o, x, y;
    scanf("%d %d", &n, &q);
    std::vector<std::bitset<size>> matrix(size);
    for (int i = 0; i < n; i++) {
        matrix[i][i] = 1;
    }
    while (q--) {
        scanf("%d %d %d", &o, &x, &y);
        x--;
        y--;
        if (o == 1) {
            if (matrix[x][y]) {
                std::cout << "Jebb ";
            } else {
                std::cout << "Neibb ";
            }
        } else {
            for (int i = 0; i < n; i++) {
                if (matrix[i][x]) {
                    matrix[i] |= matrix[y];
                }
            }
        }
    }
}