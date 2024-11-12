const MAX: usize = 1_000_001;
use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

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

    fn lineln<T: FromStr>(&mut self, n: usize) -> impl Iterator<Item = T> + '_ {
        return (0..n).map(|_| self.r())
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
    
    fn vecln<T: FromStr>(&mut self, n: usize) -> Vec<T> {
        return self.lineln(n).collect();
    }

    fn print_vec<T: Display>(&self, vec: &[T]) {
        for x in vec {
            print!("{} ", *x);
        }
    }
}


struct FenwickTree<T> {
    tree: [T; MAX+1],
}

#[allow(dead_code)]
impl<T> FenwickTree<T>
where
    T: Clone + Copy + Default + Eq + std::ops::Sub<Output = T> + std::ops::AddAssign
{
    fn new() -> Self {
        let tree = [T::default(); MAX+1];
        FenwickTree {
            tree: tree,
        }
    }

    fn update(&mut self, mut i: usize, val: T) {
        i += 1;
        while i < self.tree.len() {
            self.tree[i] += val;
            i += i & i.wrapping_neg();
        }
    }

    // [0, r]
    fn query(&self, mut r: usize) -> T {
        r += 1;
        let mut res = T::default();
        while r > 0 {
            res += self.tree[r];
            r -= r & r.wrapping_neg();
        }
        return res;
    }
}

fn moves(n: i32, mut k: i32) -> i32 {
    let mut sum_k = (k * (k + 1)) / 2;
    loop {
        if sum_k >= n && (sum_k - n) % 2 == 0 {
            return k;
        }
        k += 1;
        sum_k += k;
    }
}

fn update(pos: usize, tree: &mut FenwickTree<i32>, jump_arr: &Vec<(i32, usize)>, delta: i32) {
    // left
    tree.update(pos, -jump_arr[0].0 * delta);
    let mut prev = jump_arr[0].0;
    for (step_size, k) in &jump_arr[1..] {
        if pos + 1 <= *k {
            break;
        }
        let p = pos - k + 1;
        tree.update(p, delta * (prev - *step_size));
        prev = *step_size;
    }
    tree.update(0, delta * prev);

    // right
    let mut prev = 0;
    for (step_size, k) in jump_arr {
        let p = *k + pos;
        if p >= MAX {
            break;
        }
        tree.update(p, delta * (*step_size - prev));
        prev = *step_size
    }
}

fn change_frog(
    pos: usize,
    delta: i32,
    even_tree: &mut FenwickTree<i32>,
    odd_tree: &mut FenwickTree<i32>,
    even: &Vec<(i32, usize)>,
    odd: &Vec<(i32, usize)>,
) {
    if pos % 2 == 0 {
        update(pos, even_tree, even, delta);
        update(pos, odd_tree, odd, delta);
    } else {
        update(pos, even_tree, odd, delta);
        update(pos, odd_tree, even, delta);
    }
}

fn query(t: usize, even_tree: &FenwickTree<i32>, odd_tree: &FenwickTree<i32>) -> i32 {
    if t % 2 == 0 {
        return even_tree.query(t);
    }
    return odd_tree.query(t);
}

fn main() {
    let mut io = IO::new();
    let mut even = vec![(3, 2)];
    let mut odd = vec![(1, 1)];
    for i in 3..MAX {
        let arr = {
            if i % 2 == 0 {
                &mut even
            } else {
                &mut odd
            }
        };
        let m = moves(i as i32, arr[arr.len() - 1].0);

        if m != arr[arr.len() - 1].0 {
            arr.push((m, i));
        }
    }

    let mut even_tree = FenwickTree::new();
    let mut odd_tree = FenwickTree::new();
    let (_, mut t): (usize, usize) = io.r2();

    for i in io.line() {
        change_frog(i, 1, &mut even_tree, &mut odd_tree, &even, &odd);
    }

    let c = io.r();
    for _ in 0..c {
        let (qt, i): (char, usize) = io.r2();
        if qt == 't' {
            t = i;
        } else if qt == '+' {
            change_frog(i, 1, &mut even_tree, &mut odd_tree, &even, &odd);
        } else {
            change_frog(i, -1, &mut even_tree, &mut odd_tree, &even, &odd);
        }
        print!("{} ", query(t, &even_tree, &odd_tree))
    }
}