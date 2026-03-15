use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};
use std::collections::HashMap;


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

fn main() {
    let mut io = IO::new();
    let mut inp = io.all();
    inp.pop();
    inp.pop();
    let mut male = vec![];
    let mut female = vec![];

    for line in inp.split("\n") {
        let mut iter = line.split_ascii_whitespace();
        let q = iter.next().unwrap();
        if q == "1" {
            let name = iter.next().unwrap();
            if iter.next().unwrap() == "1" {
                male.push(name);
            } else {
                female.push(name);
            }
        }
    }
    male.sort_unstable();
    female.sort_unstable();
    let mut m_map = HashMap::new();
    let mut f_map = HashMap::new();
    for i in 0..male.len() {
        m_map.insert(male[i], i);
    }
    for i in 0..female.len() {
        f_map.insert(female[i], i);
    }

    let mut m_tree = FenwickTree::new(male.len(), None, i32::wrapping_add);
    let mut f_tree = FenwickTree::new(female.len(), None, i32::wrapping_add);
    let mut m = vec![0; male.len()];

    for line in inp.split("\n") {
        let mut iter = line.split_ascii_whitespace();
        let q = iter.next().unwrap();
        if q == "1" {
            let name = iter.next().unwrap();
            if iter.next().unwrap() == "1" {
                let i = *m_map.get(name).unwrap();
                m_tree.update(i, 1);
                m[i] += 1;
            } else {
                let i = *f_map.get(name).unwrap();
                f_tree.update(i, 1);
            
            }
        } else if q == "2" {
            let name = iter.next().unwrap();
            if let Some(i) = m_map.get(name) {
                if m[*i] != 0 {
                    m_tree.update(*i, -1);
                    m[*i] -= 1;
                    continue
                }
            }
            f_tree.update(*f_map.get(name).unwrap(), -1);
        } else {
            let l = iter.next().unwrap();
            let r = iter.next().unwrap();
            let t = iter.next().unwrap();
            let res = {
                if t == "0"      {query(&male, l, r, &m_tree) + query(&female, l, r, &f_tree)}
                else if t == "1" {query(&male, l, r, &m_tree)}
                else             {query(&female, l, r, &f_tree)}
            };
            print!("{} ", res);
        }
    }
}

fn query(arr: &Vec<&str>, l: &str, r: &str, tree: &FenwickTree<i32>) -> i32 {
    let i = match arr.binary_search(&l) {
        Ok(v) => v,
        Err(v) => v
    };
    let j = match arr.binary_search(&r) {
        Ok(v) => v,
        Err(v) => v
    };
    return tree.sum(i, j-1);
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
