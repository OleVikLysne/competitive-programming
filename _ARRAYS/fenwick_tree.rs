struct FenwickTree<T> {
    tree: Vec<T>,
    n: isize,
    op: fn(T, T) -> T,
    default: T
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
            None => vec![default; n+1]
        };
        FenwickTree {
            tree: tree,
            n: n as isize,
            op: op,
            default: default
        }
    }

    fn construct(arr: &[T], op: fn(T, T) -> T, default: T) -> Vec<T> {
        let mut tree = vec![default; arr.len()+1];
        for i in 1..tree.len() {
            tree[i] = op(tree[i], arr[i-1]);
            let j = i + (i as isize & -(i as isize)) as usize;
            if j < tree.len() {
                tree[j] = op(tree[j], tree[i]);
            }
        }
        return tree
    }

    fn update(&mut self, i: usize, val: T) {
        let mut j = i as isize + 1;
        while j <= self.n {
            self.tree[j as usize] = (self.op)(self.tree[j as usize], val);
            j += j & -j
        }
    }

    // [0, r]
    fn query(&self, r: usize) -> T {
        let mut r = r as isize + 1;
        let mut res = self.default;
        while r > 0 {
            res = (self.op)(res, self.tree[r as usize]);
            r -= r & -r
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