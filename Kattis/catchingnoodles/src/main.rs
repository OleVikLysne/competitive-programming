use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};
use std::collections::BinaryHeap;


const MOD: i64 = 10_i64.pow(9) + 7;

fn main() {
    let mut io = IO::new();
    let (n, m): (usize, usize) = io.r2();
    let mut og = vec![Vec::new(); n];
    for _ in 0..m {
        let (u, v, w): (usize, usize, i64) = io.r3();
        og[u].push((v, w));
        og[v].push((u, w));
    }

    let dist = dijkstra(&og, 0);
    let mut g = vec![Vec::new(); n];
    let mut rev_g = vec![Vec::new(); n];
    let mut in_deg = vec![0; n];
    let mut out_deg = vec![0; n];
    let mut mem = vec![-1; n];

    build_gs(0, &og, &mut g, &mut rev_g, &mut in_deg, &mut out_deg, &dist, &mut mem);
    let mut res = solve(0, &g, &mut in_deg);
    for (i, x) in solve(n-1, &rev_g, &mut out_deg).iter().enumerate() {
        res[i] = (res[i] * *x) % MOD;
        if res[i] == 0 {
            res[i] = -1;
        }
    }
    io.print_vec(&res);

}

fn solve(
    start: usize,
    g: &[Vec<usize>],
    in_deg: &mut [i32]
) -> Vec<i64> {
    let mut res = vec![0; g.len()];
    res[start] = 1;
    let mut stack = vec![start];
    while let Some(v) = stack.pop() {
        for u in g[v].iter() {
            in_deg[*u] -= 1;
            res[*u] = (res[*u] + res[v]) % MOD;
            if in_deg[*u] == 0 {
                stack.push(*u);
            }
        }
    }
    return res;
}

fn build_gs(
    v: usize, 
    og: &[Vec<(usize, i64)>], 
    g: &mut [Vec<usize>], 
    rev_g: &mut [Vec<usize>],
    in_deg: &mut [i32],
    out_deg: &mut [i32],
    dist: &[i64],
    mem: &mut [i32]
) -> i32 {
    if mem[v] != -1 {
        return mem[v];
    }
    let mut res = 0;
    if v == g.len()-1 {
        res = 1;
    }
    for (u, w) in og[v].iter() {
        if dist[*u] == dist[v] + w && build_gs(*u, og, g, rev_g, in_deg, out_deg, dist, mem) == 1 {
            g[v].push(*u);
            rev_g[*u].push(v);
            in_deg[*u] += 1;
            out_deg[v] += 1;
            res = 1;
        }
    }
    mem[v] = res;
    return res
}

fn dijkstra(g: &[Vec<(usize, i64)>], source: usize) -> Vec<i64> {
    let n = g.len();
    let mut dist = vec![i64::MAX; n];
    dist[source] = 0;
    let mut pq = BinaryHeap::from([(0, source)]);
    while let Some((mut d, v)) = pq.pop() {
        d = -d;
        if dist[v] < d {continue}
        for (u, w) in g[v].iter() {
            if dist[*u] > dist[v] + w {
                dist[*u] = dist[v] + w;
                pq.push((-dist[*u], *u));
            }
        }
    }
    return dist;

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
