struct FenwickTree<T> {
    tree: Vec<T>,
    op: fn(T, T) -> T,
    default: T,
}

#[allow(dead_code)]
impl<T> FenwickTree<T>
where
    T: Clone + Copy + Default + Eq + std::ops::Sub<Output = T>,
{
    fn new(n: usize, arr: Option<&[T]>, op: fn(T, T) -> T) -> Self {
        let default = T::default();
        let tree = match arr {
            Some(v) => Self::construct(v, op, default),
            None => vec![default; n + 1],
        };
        FenwickTree {
            tree: tree,
            op: op,
            default: default,
        }
    }

    fn construct(arr: &[T], op: fn(T, T) -> T, default: T) -> Vec<T> {
        let mut tree = vec![default; arr.len() + 1];
        for i in 1..tree.len() {
            tree[i] = op(tree[i], arr[i - 1]);
            let j = i + (i & i.wrapping_neg());
            if j < tree.len() {
                tree[j] = op(tree[j], tree[i]);
            }
        }
        return tree;
    }

    fn update(&mut self, mut i: usize, val: T) {
        i += 1;
        while i < self.tree.len() {
            self.tree[i] = (self.op)(self.tree[i], val);
            i += i & i.wrapping_neg();
        }
    }

    // [0, r]
    fn query(&self, mut r: usize) -> T {
        r += 1;
        let mut res = self.default;
        while r > 0 {
            res = (self.op)(res, self.tree[r]);
            r -= r & r.wrapping_neg();
        }
        return res;
    }

    fn sum(&self, l: usize, r: usize) -> T {
        let res = self.query(r);
        if l > 0 {
            return res - self.query(l - 1);
        }
        return res;
    }
}