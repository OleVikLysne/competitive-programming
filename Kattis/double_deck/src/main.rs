struct SegmentTree {
    tree: Vec<i64>,
    n: usize,
}

impl SegmentTree {
    fn new(arr: &[i64]) -> Self {
        let n = arr.len();
        let mut tree = vec![0; 2*n];
        for i in 0..n {
            tree[i+n] = arr[i]; 
        }

        for i in (1..n).rev() {
            tree[i] = tree[i*2].max(tree[i*2+1]);
        }
        SegmentTree{tree, n}
    }

    fn update(&mut self, mut i: usize, val: i64) {
        i += self.n;
        self.tree[i] = val;
        while i > 1 {
            i /= 2;
            self.tree[i] = self.tree[2*i].max(self.tree[2*i+1]);
        }
    }

    fn query(&self, mut l: usize, mut r: usize)  -> i64 {
        l += self.n;
        r += self.n;
        if l == r {
            return self.tree[l];
        }
        let mut s = self.tree[l].max(self.tree[r]);
        let mut pl = l / 2;
        let mut pr = r / 2;
        while pl != pr {
            if l & 1 == 0 {
                s = s.max(self.tree[l+1]);
            }
            if r & 1 == 1 {
                s = s.max(self.tree[r-1]);
            }
            l = pl;
            r = pr;
            pl /= 2;
            pr /= 2;
        }
        return s
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
    let arr1: Vec<u64> = buf.split_ascii_whitespace().map(|x| x.parse::<u64>().unwrap()).collect();
    buf.clear();
    let _ = stdin.read_line(&mut buf);
    let arr2: Vec<u64> = buf.split_ascii_whitespace().map(|x| x.parse::<u64>().unwrap()).collect();
    
    let mut m = vec![Vec::new(); n];
    for i in (0..n*k).rev() {
        let x = arr2[i]-1;
        m[x as usize].push(i);
    }

    let base = vec![0; n*k];
    let mut tree = SegmentTree::new(&base);
    for x in arr1 {
        for i in &m[(x-1) as usize] {
            let v = {
                if *i == 0 {
                    0
                } else {
                    tree.query(0, (*i-1) as usize)
                }
            };
            tree.update(*i, v+1);
        }
    }
    println!("{}", tree.query(0, n*k-1));
    Ok(())
}