use std::fmt::Display;

struct IO {
    buf: String,
    stdin: std::io::Stdin,
}

#[allow(dead_code)]
impl IO {
    fn new() -> Self {
        IO {
            buf: String::new(),
            stdin: std::io::stdin(),
        }
    }

    fn parse<T: std::str::FromStr>(&self, s: &str) -> T {
        unsafe { s.parse::<T>().unwrap_unchecked() }
    }

    fn parse_next<T: std::str::FromStr>(
        &self,
        line_split: &mut std::str::SplitAsciiWhitespace,
    ) -> T {
        unsafe { self.parse(line_split.next().unwrap_unchecked()) }
    }

    fn r<T: std::str::FromStr>(&mut self) -> T {
        self.buf.clear();
        let _ = self.stdin.read_line(&mut self.buf);
        self.parse(self.buf.trim())
    }

    fn r2<T1, T2>(&mut self) -> (T1, T2)
    where
        T1: std::str::FromStr,
        T2: std::str::FromStr,
    {
        self.buf.clear();
        let _ = self.stdin.read_line(&mut self.buf);
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn r3<T1, T2, T3>(&mut self) -> (T1, T2, T3)
    where
        T1: std::str::FromStr,
        T2: std::str::FromStr,
        T3: std::str::FromStr,
    {
        self.buf.clear();
        let _ = self.stdin.read_line(&mut self.buf);
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn r4<T1, T2, T3, T4>(&mut self) -> (T1, T2, T3, T4)
    where
        T1: std::str::FromStr,
        T2: std::str::FromStr,
        T3: std::str::FromStr,
        T4: std::str::FromStr,
    {
        self.buf.clear();
        let _ = self.stdin.read_line(&mut self.buf);
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn r5<T1, T2, T3, T4, T5>(&mut self) -> (T1, T2, T3, T4, T5)
    where
        T1: std::str::FromStr,
        T2: std::str::FromStr,
        T3: std::str::FromStr,
        T4: std::str::FromStr,
        T5: std::str::FromStr,
    {
        self.buf.clear();
        let _ = self.stdin.read_line(&mut self.buf);
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn line(&mut self) -> std::str::SplitAsciiWhitespace {
        self.buf.clear();
        let _ = self.stdin.read_line(&mut self.buf);
        return self.buf.split_ascii_whitespace();
    }

    fn vec<T: std::str::FromStr>(&mut self) -> Vec<T> {
        self.buf.clear();
        let _ = self.stdin.read_line(&mut self.buf);
        return self
            .buf
            .split_ascii_whitespace()
            .map(|x| self.parse(x))
            .collect();
    }

    fn print_vec<T: Display>(&self, vec: &Vec<T>) {
        for x in vec {
            print!("{} ", *x);
        }
    }
}

struct FenwickTree<T> {
    tree: Vec<T>,
    n: usize,
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
            n: n,
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
        while i <= self.n {
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



fn main() {
    let mut io = IO::new();
    let (_, q): (u32, u32) = io.r2();
    let mut values: Vec<usize> = io.vec();
    let mut gems: Vec<usize> = io.r::<String>().chars().map(|x| (x.to_digit(10).unwrap()-1) as usize).collect();

    let mut trees = Vec::with_capacity(6);
    for k in 0..6 {
        let base: Vec<isize> = gems.iter().map(|x| (*x == k) as isize).collect();
        let tree = FenwickTree::new(base.len(), Some(&base), isize::wrapping_add);
        trees.push(tree);
    }

    for _ in 0..q {
        let (a, b, c): (char, usize, usize) = io.r3();

        if a == '1' {
            let k: usize = b-1;
            let p = c -1;
            let old_p = gems[k];
            trees[old_p].update(k, -1);
            trees[p].update(k, 1);
            gems[k] = p;
        }

        else if a == '2' {
            let p = b-1;
            let v = c ;
            values[p] = v;
        }

        else if a == '3' {
            let l: usize = b-1;
            let r: usize = c-1;
            let mut s: usize = 0;
            for (i, tree) in trees.iter().enumerate() {
                s += tree.sum(l, r) as usize * values[i];
            }
            println!("{}", s);
        }
    }
}
