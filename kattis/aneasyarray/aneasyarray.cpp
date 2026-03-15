#include <bits/stdc++.h>
using namespace std;

constexpr int MAX_SIZE = 5e5;

struct Pair {
    long long val;
    int idx;
    Pair(long long v = LLONG_MAX, int i = 0) : val(v), idx(i) {}
};

class SegmentTree {
private:
    vector<array<Pair, 2>> tree;
    
    array<Pair, 2> op(const array<Pair, 2>& v1, const array<Pair, 2>& v2) {
        array<Pair, 2> res;
        int i = 0, j = 0;
        for (int k = 0; k < 2; k++) {
            if (v1[i].val < v2[j].val) {
                res[k] = v1[i++];
            } else {
                res[k] = v2[j++];
            }
        }
        return res;
    }

public:
    SegmentTree(const vector<long long> &arr) {
        tree.resize(2 * MAX_SIZE);
        for (int i = 0; i < arr.size(); i++) {
            tree[MAX_SIZE + i][0] = Pair(arr[i], i);
            tree[MAX_SIZE + i][1] = Pair(LLONG_MAX, i);
        }
        
        // Build tree
        for (int i = MAX_SIZE - 1; i > 0; i--) {
            tree[i] = op(tree[i * 2], tree[i * 2 + 1]);
        }
    }
    
    array<Pair, 2> query(int l, int r) {  // inclusive [l, r]
        l += MAX_SIZE;
        r += MAX_SIZE;
        
        if (l == r) return tree[l];
        
        auto res = op(tree[l], tree[r]);
        int pl = l / 2;
        int pr = r / 2;
        
        while (pl != pr) {
            if (l % 2 == 0) {
                res = op(res, tree[l + 1]);
            }
            if (r % 2 == 1) {
                res = op(res, tree[r - 1]);
            }
            l = pl;
            r = pr;
            pl /= 2;
            pr /= 2;
        }
        return res;
    }
};

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    
    int n, q;
    cin >> n >> q;
    
    vector<long long> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }
    
    SegmentTree min_tree(arr);
    vector<long long> neg_arr(arr);
    for (auto& x : neg_arr) x = -x;
    SegmentTree max_tree(neg_arr);
    
    while (q--) {
        int l, r;
        cin >> l >> r;
        l--; r--;
        
        auto min = min_tree.query(l + 1, r - 1);
        auto max = max_tree.query(l + 1, r - 1);

        max[0].val = -max[0].val;
        max[1].val = -max[1].val;
        
        long long res = std::max(arr[l] * arr[r] * max[0].val * max[1].val, arr[l] * arr[r] * min[0].val * min[1].val);
        if (max[0].idx != min[0].idx) {
            res = std::max(res, arr[l] * arr[r] * max[0].val * min[0].val);
        }
        if (max[0].idx != min[1].idx) {
            res = std::max(res, arr[l] * arr[r] * max[0].val * min[1].val);
        }
        if (max[1].idx != min[0].idx) {
            res = std::max(res, arr[l] * arr[r] * max[1].val * min[0].val);
        }
        if (max[1].idx != min[1].idx) {
            res = std::max(res, arr[l] * arr[r] * max[1].val * min[1].val);
        }
        
        cout << res << '\n';
    }
    
    return 0;
}
