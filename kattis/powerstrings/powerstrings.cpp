#include <iostream>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    string s;
    while (true) {
        cin >> s;
        if (s == ".") break;
        int size = s.size();
        for (int factor = 1; factor <= size; factor++) {
            if (size % factor != 0) continue;
            bool broke = false;
            for (int i = factor; i < size; i++) {
                if (s[i-factor] != s[i]) {
                    broke = true;
                    break;
                }
            }
            if (!broke) {
                printf("%d\n", size / factor);
                break;
            }
        }
    }
}