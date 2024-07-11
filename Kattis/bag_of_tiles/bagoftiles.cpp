#include <iostream> 
#include <cstdio>
#include <vector>
using namespace std; 
  
int g;
int t, k, n;
int tiles[30];
int triangle[31][31];

int main() {
    for (int i = 0; i<31; i++) {
        for (int j = 0; j<31; j++) {
            triangle[i][j] = 1;
        }
    }
    for (int i = 1; i<31; i++) {
        for (int j = 1; j<i; j++) {
            triangle[i][j] = triangle[i-1][j] + triangle[i-1][j-1];
        }
    }

    scanf("%d", &g);
    for (int x=1; x<=g; x++) {
        scanf("%d", &n);
        int s = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &tiles[i]);
            s += tiles[i];
        }
        scanf("%d", &k);
        scanf("%d", &t);

        if ( (t+1)*(k+1) > ((s-t)+1) * ((n-k)+1) ) {
            k = n - k;
            t = s - t;
        }

        int dp[31][10001] = {};
        dp[0][0] = 1;
        vector<vector<int>> indices(k+1);
        indices[0].push_back(0);
        for (int z = n-1; z >= 0; z--) {
            int val = tiles[z];
            int u = max(0, k-z-1);
            for (int i = k-1; i >= u; i--) {
                for (int j : indices[i]) {
                    if (j+val <= t) {
                        if (dp[i+1][j+val] == 0) {
                            indices[i+1].push_back(j+val);
                        }
                        dp[i+1][j+val] += dp[i][j];
                    }
                    
                }
            }
        }
        int w = dp[k][t];
        int n_choose_k = triangle[n][k];
        printf("Game %d -- %d : %d\n", x, w, n_choose_k-w);
    }
}