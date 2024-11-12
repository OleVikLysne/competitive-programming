use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

fn main() {
    let mut io = IO::new();
    let n: usize = io.r();
    let mut arr = Vec::with_capacity(n);
    for _ in 0..n {
        let x: (i32, i32) = io.r2();
        arr.push(x);
    }
    arr.sort_by_key(|x| -x.1);
    let base: Vec<i32> = (0..2*10_i32.pow(6)+1).collect();
    let mut tree = SegmentTree::new( &base, i32::max);
    let mut s = 0;
    for (t, d) in arr {
        let x = tree.query(0, t as usize);
        if x != 0 {
            tree.update(x as usize, 0);
            s += d;
        }
    }
    println!("{}", s);
}

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

    fn _rl(&mut self) {
        self.buf.clear();
        let _ = self.stdin.read_line(&mut self.buf);
    }

    fn parse<T: FromStr>(&self, s: &str) -> T {
        unsafe { s.parse::<T>().unwrap_unchecked() }
    }

    fn parse_next<T: FromStr>(&self, line_split: &mut SplitAsciiWhitespace) -> T {
        unsafe { self.parse(line_split.next().unwrap_unchecked()) }
    }

    fn r<T: FromStr>(&mut self) -> T {
        self._rl();
        self.parse(self.buf.trim())
    }

    fn r2<T1, T2>(&mut self) -> (T1, T2)
    where
        T1: FromStr,
        T2: FromStr,
    {
        self._rl();
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn r3<T1, T2, T3>(&mut self) -> (T1, T2, T3)
    where
        T1: FromStr,
        T2: FromStr,
        T3: FromStr,
    {
        self._rl();
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn r4<T1, T2, T3, T4>(&mut self) -> (T1, T2, T3, T4)
    where
        T1: FromStr,
        T2: FromStr,
        T3: FromStr,
        T4: FromStr,
    {
        self._rl();
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
        T1: FromStr,
        T2: FromStr,
        T3: FromStr,
        T4: FromStr,
        T5: FromStr,
    {
        self._rl();
        let mut line_split = self.buf.split_ascii_whitespace();
        (
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
            self.parse_next(&mut line_split),
        )
    }

    fn line<T: FromStr>(&mut self) -> impl Iterator<Item = T> + '_ {
        self._rl();
        return self.buf.split_ascii_whitespace().map(|x| self.parse(x));
    }

    fn linenl<T: FromStr>(&mut self, n: usize) -> impl Iterator<Item = T> + '_ {
        return (0..n).map(|_| self.r());
    }

    fn chars(&mut self) -> Chars {
        self._rl();
        return self.buf.trim().chars();
    }

    fn all(&mut self) -> String {
        self.buf.clear();
        let _ = self.stdin.read_to_string(&mut self.buf);
        return self.buf.trim().to_string();
    }

    fn vec<T: FromStr>(&mut self) -> Vec<T> {
        return self.line().collect();
    }

    fn vecnl<T: FromStr>(&mut self, n: usize) -> Vec<T> {
        return self.linenl(n).collect();
    }

    fn print_vec<T: Display>(&self, vec: &[T]) {
        for x in vec {
            print!("{} ", *x);
        }
    }
}
