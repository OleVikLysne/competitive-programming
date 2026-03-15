use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

type N = u32;
const MAX: usize = 200_001;
const MAX_LOG: usize = 18;

type AncMat = [[N; MAX]; MAX_LOG];

fn main() {
    let mut depth = [0; MAX];
    let mut anc_matrix: AncMat = [[0; MAX]; MAX_LOG];
    let mut prev = ['#'; MAX];
    let mut next = [N::MAX; MAX];
    let mut sort_map = [0; MAX];
    let mut nodes = [0; MAX];
    let mut cur_idx = 0;

    let mut io = IO::new();
    let (n, q): (u32, u32) = io.r2();
    let mut strings = Vec::with_capacity(n as usize);
    for i in 0..n {
        let string: String = io.r();
        strings.push((string, i));
    }
    strings.sort_unstable();
    for i in 0..n {
        let (string, j) = &strings[i as usize];
        sort_map[*j as usize] = i;
        nodes[i as usize] = add(
            string.chars(),
            &mut cur_idx,
            &mut prev,
            &mut next,
            &mut anc_matrix,
            &mut depth,
        )
    }

    for i in 1..MAX_LOG {
        for j in 0..MAX {
            anc_matrix[i][j] = anc_matrix[i - 1][anc_matrix[i - 1][j] as usize];
        }
    }

    let mut indices = [0; MAX];
    for _ in 0..q {
        let (k, l): (usize, usize) = io.r2();
        for (i, x) in io.line::<u32>().enumerate() {
            indices[i] = sort_map[(x-1) as usize];
        }
        indices[0..k].sort_unstable();
        let mut tot = 0;
        for i in 0..k-l+1 {
            let a = nodes[indices[i] as usize];
            let b = nodes[indices[i+l-1] as usize];
            let c = lca(a, b, &anc_matrix, &depth);
            let d = {
                if i+l < k {
                    lca(c, nodes[indices[i+l] as usize], &anc_matrix, &depth)
                } else {
                    0
                }
            };
            if d == c { continue }
            let e = {
                if i > 0 {
                    lca(c, nodes[indices[i-1] as usize], &anc_matrix, &depth)
                } else {
                    0
                }
            };
            if e == c { continue }
            tot += depth[c as usize] - depth[d as usize].max(depth[e as usize]);
        }
        println!("{}", tot);
    }
}

fn anc(mut v: N, mut k: u32, anc_matrix: &AncMat) -> N {
    let mut i = (u32::BITS - k.leading_zeros() + 1) as usize;
    while k != 0 {
        i -= 1;
        if k & 1 << i != 0 {
            v = anc_matrix[i][v as usize];
            k ^= 1 << i;
        }
    }
    return v;
}

fn lca(mut u: N, mut v: N, anc_matrix: &AncMat, depth: &[u32]) -> N {
    if depth[v as usize] > depth[u as usize] {
        std::mem::swap(&mut u, &mut v);
    }
    u = anc(u, depth[u as usize] - depth[v as usize], anc_matrix);
    if u == v {
        return v;
    }
    let log_d = (depth[v as usize]).ilog2() + 1;
    for i in (0..log_d as usize).rev() {
        if anc_matrix[i][u as usize] != anc_matrix[i][v as usize] {
            u = anc_matrix[i][u as usize];
            v = anc_matrix[i][v as usize];
        }
    }
    return anc_matrix[0][v as usize];
}

fn add(
    chars: Chars,
    cur_idx: &mut usize,
    prev: &mut [char],
    next: &mut [N],
    anc_matrix: &mut AncMat,
    depth: &mut [u32],
) -> N {
    let mut current: N  = 0;
    for x in chars {
        if x != prev[current as usize] {
            prev[current as usize] = x;
            *cur_idx += 1;
            anc_matrix[0][*cur_idx] = current;
            depth[*cur_idx] = depth[current as usize] + 1;
            next[current as usize] = *cur_idx as u32;
        }
        current = next[current as usize];
    }
    return current;
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
