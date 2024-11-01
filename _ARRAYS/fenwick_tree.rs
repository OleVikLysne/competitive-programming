struct FenwickTree<T> {
    tree: Vec<T>,
    n: isize,
}

impl<T> FenwickTree<T>
where
T: Clone + Copy + Default + Eq + std::ops::AddAssign,
{
    fn new(n: usize) -> Self {
        FenwickTree {
            tree: vec![T::default(); n + 1],
            n: n as isize,
        }
    }
    
    fn update(&mut self, i: usize, val: T) {
        let mut j = i as isize + 1;
        while j <= self.n {
            self.tree[j as usize] += val;
            j += j & -j
        }
    }
    
    // [0, r]
    fn query(&self, r: usize) -> T {
        let mut r = r as isize + 1;
        let mut s = T::default();
        while r > 0 {
            s += self.tree[r as usize];
            r -= r & -r
        }
        return s;
    }
}