use std::collections::BinaryHeap;
use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

const INF: i64 = 1 << 60;
const K: usize = 1000;
const N: usize = 1000;

fn main() {
    let mut io = IO::new();
    let (n, m): (usize, usize) = io.r2();
    let mut g = vec![Vec::new(); n];
    for _ in 0..m {
        let (mut u, mut v, w): (usize, usize, i64) = io.r3();
        u -= 1;
        v -= 1;
        g[u].push((v, w));
        g[v].push((u, w));
    }
    let mut dist: [[i64; N]; N] = [[INF; N]; N];
    for source in 0..n {
        dist[source][source] = 0;
        for v in 0..source {
            dist[source][v] = dist[v][source];
        }
        let mut pq = BinaryHeap::from_iter((0..source + 1).map(|i| (-dist[source][i], i)));
        while let Some((_, v)) = pq.pop() {
            for (u, w) in &g[v] {
                let u = *u;
                if dist[source][u] > dist[source][v] + w {
                    dist[source][u] = dist[source][v] + w;
                    pq.push((-dist[source][u], u));
                }
            }
        }
    }
    let k: usize = io.r();
    let mut ready = [0; K];
    let mut node = [0; K];
    let mut placed = [0; K];
    for i in 0..k {
        let (s, mut u, t): (i64, usize, i64) = io.r3();
        u -= 1;
        placed[i] = s;
        ready[i] = t;
        node[i] = u;
    }

    let mut lo = 0;
    let mut hi = 1 << 60;
    while lo < hi {
        let mi = (lo+hi)/2;
        if solve(mi, k, &dist, &placed, &ready, &node) {
            hi = mi
        } else {
            lo = mi + 1;
        }
    }
    println!("{}", lo);
}


fn bisect_right(arr: &[i64], val: i64, k: usize) -> usize {
    let mut lo = 0;
    let mut hi = k;
    while lo < hi {
        let mi = (lo+hi)/2;
        if arr[mi] <= val {
            lo = mi + 1;
        } else {
            hi = mi;
        }
    }
    return lo;
}

fn solve(d: i64, k: usize, dist: &[[i64; N]; N], placed: &[i64], ready: &[i64], node: &[usize]) -> bool {
    let mut dp = [[[INF; 2]; K + 1]; K];
    dp[0][1][0] = ready[0];
    for i in 0..k {
        for j in i + 1..k + 1 {
            for l in 0..2 {
                let t = dp[i][j][l];
                if t == INF { continue }
                let v = { if l == 0 { 0 } else { node[i] } };
                let ni = { if l == 1 { i + 1 } else { i } };

                if ni < j {
                    let nt = t + dist[v][node[ni]];
                    if nt - placed[ni] <= d {
                        let nj = j;
                        dp[ni][nj][1] = dp[ni][nj][1].min(nt);
                    }
                }
                if j < k {
                    let nt = ready[j].max(t + dist[v][0]);
                    if nt - placed[ni] <= d {
                        let nj = {
                            if nt == ready[j] { j+1 }
                            else { bisect_right(ready, nt, k) }
                        };
                        dp[ni][nj][0] = dp[ni][nj][0].min(nt);
                    }
                }
            }
        }
    }
    return dp[k-1][k][1] - placed[k-1] <= d;
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

    fn lineln<T: FromStr>(&mut self, n: usize) -> impl Iterator<Item = T> + '_ {
        return (0..n).map(|_| self.r());
    }

    fn vec<T: FromStr>(&mut self) -> Vec<T> {
        return self.line().collect();
    }

    fn vecln<T: FromStr>(&mut self, n: usize) -> Vec<T> {
        return self.lineln(n).collect();
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
        let vec_string = vec.iter().map(|x| x.to_string() + " ").collect::<String>();
        println!("{}", vec_string);
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
