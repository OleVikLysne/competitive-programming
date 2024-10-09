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
        let mut tree = Vec::with_capacity(2*n);
        tree.extend(std::iter::repeat(T::default()).take(n));
        tree.extend(arr);

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


fn main() {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let mut foo = buf.split_whitespace();
    let _ = foo.next();
    let q: u32 = foo.next().unwrap().parse().unwrap();
    buf.clear();

    let _ = stdin.read_line(&mut buf);
    let mut values: Vec<u64> = buf.split_whitespace().map(|x| x.parse::<u64>().unwrap()).collect();
    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let mut gems: Vec<u8> = buf.trim().chars().map(|x| (x.to_digit(10).unwrap()-1) as u8).collect();
    buf.clear();

    let mut trees = Vec::with_capacity(6);
    for k in 0..6 {
        let base: Vec<u32> = gems.iter().map(|x| (*x == k) as u32).collect();
        let seg_tree = SegmentTree::new(&base, u32::wrapping_add);
        trees.push(seg_tree);
    }

    for _ in 0..q {
        let _ = stdin.read_line(&mut buf);
        let mut foo = buf.split_whitespace();
        let a = foo.next().unwrap();

        if a == "1" {
            let k: usize = foo.next().unwrap().parse::<usize>().unwrap()-1;
            let p: u8 = foo.next().unwrap().parse::<u8>().unwrap()-1;
            let old_p = gems[k] as usize;
            trees[old_p].update(k, 0);
            trees[p as usize].update(k, 1);
            gems[k] = p;
        }

        else if a == "2" {
            let p: usize = foo.next().unwrap().parse::<usize>().unwrap()-1;
            let v: u64 = foo.next().unwrap().parse().unwrap();
            values[p] = v;
        }

        else if a == "3" {
            let l: usize = foo.next().unwrap().parse::<usize>().unwrap()-1;
            let r: usize = foo.next().unwrap().parse::<usize>().unwrap()-1;
            let mut s: u64 = 0;
            for (i, tree) in trees.iter().enumerate() {
                s += tree.query(l, r) as u64 * values[i];
            }
            println!("{}", s);
        }
        buf.clear();
    }
}
