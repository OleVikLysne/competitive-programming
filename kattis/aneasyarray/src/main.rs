struct SegmentTree<T> {
    tree: Vec<[T; 2]>,
    n: usize,
    op: fn(T, T) -> bool
}

impl<T> SegmentTree<T> 
    where
    T: Clone + Copy + Default + Eq,
{
    fn new(arr: &[T], op: fn(T, T) -> bool, default: T) -> Self {
        let n = arr.len();
        let mut tree = Vec::with_capacity(2*n);
        tree.extend(std::iter::repeat([default, default]).take(n));
        for x in arr {
            tree.push([*x, default]);
        }

        for i in (1..n).rev() {
            
            tree[i] = Self::op(&tree[i*2], &tree[i*2+1], op);
        }
        SegmentTree{tree, n, op}
    }

    fn op(v1: &[T; 2], v2: &[T; 2], _op: fn(T, T) -> bool) -> [T; 2] {
        let mut res: [T; 2] = [T::default(); 2];
        let mut i = 0;
        let mut j = 0;
        for k in 0..2 {
            if _op(v1[i], v2[j]) {
                res[k] = v1[i];
                i += 1;
            } else {
                res[k] = v2[j];
                j += 1;
            }
        }
        return res
    }

    // inclusive on both sides [l, r]
    fn query(&self, mut l: usize, mut r: usize)  -> [T; 2] {
        l += self.n;
        r += self.n;
        if l == r {
            return self.tree[l];
        }
        let mut res = Self::op(&self.tree[l], &self.tree[r], self.op);
        let mut pl = l / 2;
        let mut pr = r / 2;
        while pl != pr {
            if l % 2 == 0 {
                res = Self::op(&res, &self.tree[l+1], self.op);
            }
            if r % 2 == 1 {
                res = Self::op(&res, &self.tree[r-1], self.op);
            }
            l = pl;
            r = pr;
            pl /= 2;
            pr /= 2;
        }
        return res
    }
}

use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

fn main() {
    let mut io = IO::new();
    let (_, q): (usize, usize) = io.r2();
    let arr: Vec<i64> = io.vec();
    let min_tree = SegmentTree::new(&arr, |x, y| x < y, i64::MAX);
    let max_tree = SegmentTree::new(&arr, |x, y| x > y, i64::MIN);
    for _ in 0..q {
        let (mut l, mut r): (usize, usize) = io.r2();
        l -= 1;
        r -= 1;
        let min = min_tree.query(l + 1, r - 1);
        let max = max_tree.query(l + 1, r - 1);
        let res = (arr[l] * arr[r] * min[0] * min[1])
            .max(arr[l] * arr[r] * max[0] * max[1])
            .max(arr[l] * arr[r] * max[0] * min[0]);
        print!("{} ", res);
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
        unsafe { s.parse().unwrap_unchecked() }
    }

    fn parse_next<T: FromStr>(&self, line_split: &mut SplitAsciiWhitespace) -> T {
        unsafe { self.parse(line_split.next().unwrap_unchecked()) }
    }

    fn line<T: FromStr>(&mut self) -> impl Iterator<Item = T> + '_ {
        self._rl();
        return self.buf.split_ascii_whitespace().map(|x| self.parse(x));
    }

    fn linenl<T: FromStr>(&mut self, n: usize) -> impl Iterator<Item = T> + '_ {
        return (0..n).map(|_| self.r());
    }

    fn vec<T: FromStr>(&mut self) -> Vec<T> {
        return self.line().collect();
    }

    fn vecnl<T: FromStr>(&mut self, n: usize) -> Vec<T> {
        return self.linenl(n).collect();
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

    fn print_vec<T: Display>(&self, vec: &[T]) {
        for x in vec {
            print!("{} ", *x);
        }
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
}
