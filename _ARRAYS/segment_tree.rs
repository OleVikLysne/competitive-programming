// only tested with max queries

struct SegmentTree<T> {
    tree: Vec<T>,
    n: usize,
    op: fn(T, T) -> T
}

impl<T> SegmentTree<T> 
    where
    T: Clone + Copy + Default + Eq,
    {
    fn new(arr: &[T], op: fn(T, T) -> T) -> Self {
        let n = arr.len();
        let mut tree = vec![T::default(); 2*n];
        for i in 0..n {
            tree[i+n] = arr[i];
        }

        for i in (1..n).rev() {
            tree[i] = op(tree[i*2], tree[i*2+1]);
        }
        SegmentTree{tree, n, op}
    }

    fn update(&mut self, mut i: usize, val: T) {
        i += self.n;
        if self.tree[i] == val {
            return
        }
        self.tree[i] = val;
        while i > 1 {
            i /= 2;
            self.tree[i] = (self.op)(self.tree[2*i], self.tree[2*i+1]);
        }
    }

    // inclusive on both sides [l, r]
    fn query(&self, mut l: usize, mut r: usize)  -> T {
        l += self.n;
        r += self.n;
        if l == r {
            return self.tree[l];
        }
        let mut res = (self.op)(self.tree[l], self.tree[r]);
        let mut pl = l / 2;
        let mut pr = r / 2;
        while pl != pr {
            if l % 2 == 0 {
                res = (self.op)(res, self.tree[l+1]);
            }
            if r % 2 == 1 {
                res = (self.op)(res, self.tree[r-1]);

            }
            l = pl;
            r = pr;
            pl /= 2;
            pr /= 2;
        }
        return res
    }
}