const MAX_SIZE: usize = 5*10_usize.pow(5);

struct SegmentTree<T> {
    tree: [[usize; 2]; MAX_SIZE*2],
    arr: [T; MAX_SIZE],
    op: fn(T, T) -> bool,
}

impl<T> SegmentTree<T>
where
    T: Clone + Copy + Default + Eq + Ord,
{
    fn new(arr: [T; MAX_SIZE], op: fn(T, T) -> bool) -> Self {
        let mut tree = [[0; 2]; MAX_SIZE*2];
        for i in 0..MAX_SIZE {
            tree[MAX_SIZE+i] = [i, i];
        }

        for i in (1..MAX_SIZE).rev() {
            tree[i] = Self::op(&tree[i * 2], &tree[i * 2 + 1], op, &arr);
        }
        SegmentTree { tree, arr, op}
    }

    fn op(v1: &[usize; 2], v2: &[usize; 2], _op: fn(T, T) -> bool, arr: &[T]) -> [usize; 2] {
        let mut res: [usize; 2] = [0; 2];
        let mut i = 0;
        let mut j = 0;
        for k in 0..2 {
            if ((i != 1 || v1[0] != v1[1]) && _op(arr[v1[i]], arr[v2[j]])) || (j == 1 && v2[0] == v2[1]) {
                res[k] = v1[i];
                i += 1;
            } else {
                res[k] = v2[j];
                j += 1
            }
        }
        return res
    }

    // inclusive on both sides [l, r]
    fn query(&self, mut l: usize, mut r: usize) -> [usize; 2] {
        l += MAX_SIZE;
        r += MAX_SIZE;
        if l == r {
            return self.tree[l];
        }
        let mut res = Self::op(&self.tree[l], &self.tree[r], self.op, &self.arr);
        let mut pl = l / 2;
        let mut pr = r / 2;
        while pl != pr {
            if l % 2 == 0 {
                res = Self::op(&res, &self.tree[l + 1], self.op, &self.arr);
            }
            if r % 2 == 1 {
                res = Self::op(&res, &self.tree[r - 1], self.op, &self.arr);
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
    let mut arr = [i64::MAX; MAX_SIZE];
    for (i, x) in io.line().enumerate() {
        arr[i] = x;
    }
    let min_tree = SegmentTree::new(arr, |x, y| x < y);
    let max_tree = SegmentTree::new(arr, |x, y| x > y);
    for _ in 0..q {
        let (mut l, mut r): (usize, usize) = io.r2();
        l -= 1;
        r -= 1;
        let min = min_tree.query(l+1, r-1);
        let max = max_tree.query(l+1, r-1);
        let mut res = (arr[l]*arr[r]*arr[min[0]]*arr[min[1]]).max(arr[l]*arr[r]*arr[max[0]]*arr[max[1]]);
        if max[0] != min[0] {
            res = res.max(arr[l]*arr[r]*arr[max[0]]*arr[min[0]]);
        }
        if max[0] != min[1] {
            res = res.max(arr[l]*arr[r]*arr[max[0]]*arr[min[1]]);
        }
        if min[0] != max[1] {
            res = res.max(arr[l]*arr[r]*arr[min[0]]*arr[max[1]]);
        }
        if min[1] != max[1] {
            res = res.max(arr[l]*arr[r]*arr[min[1]]*arr[max[1]]);
        }
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
