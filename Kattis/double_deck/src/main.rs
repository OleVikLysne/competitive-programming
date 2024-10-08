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

fn main() -> Result<(), std::num::ParseIntError> {
    let stdin = std::io::stdin();
    let mut buf = String::new();
    let _ = stdin.read_line(&mut buf);
    let mut nk = buf.split_ascii_whitespace();
    let n: usize = nk.next().unwrap().parse()?;
    let k: usize = nk.next().unwrap().parse()?;
    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let arr1: Vec<u32> = buf.split_ascii_whitespace().map(|x| x.parse::<u32>().unwrap()-1).collect();
    
    let mut m = vec![Vec::new(); n];
    for i in (0..n*k).rev() {
        m[arr1[i] as usize].push(i as u32);
    }
    
    let base = vec![0; n*k];
    let mut tree = SegmentTree::new(&base, std::cmp::max);
    buf.clear();

    let _ = stdin.read_line(&mut buf);
    for x in buf.split_ascii_whitespace().map(|x| x.parse::<usize>().unwrap()-1) {
        for i in m[x].iter().map(|x| *x as usize) {
            let v = {
                if i == 0 {
                    0
                } else {
                    tree.query(0, i-1)
                }
            };
            tree.update(i, v+1);
        }
    }
    println!("{}", tree.tree[1]);
    Ok(())
}