const MAX: usize = 1_000_001;

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
    tree: [T; MAX + 1],
    n: isize,
}

impl<T> FenwickTree<T>
where
    T: Clone + Copy + Default + Eq + std::ops::AddAssign,
{
    fn new() -> Self {
        FenwickTree {
            tree: [T::default(); MAX + 1],
            n: MAX as isize,
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

fn query(t: usize, even_tree: &mut FenwickTree<i32>, odd_tree: &mut FenwickTree<i32>) -> i32 {
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
    unsafe {
        for i in io.line().map(|x| x.parse().unwrap_unchecked()) {
            change_frog(i, 1, &mut even_tree, &mut odd_tree, &even, &odd);
        }
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
        print!("{} ", query(t, &mut even_tree, &mut odd_tree))
    }
}