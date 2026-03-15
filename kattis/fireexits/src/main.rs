use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

const N: usize = 1000;
const D: usize = 1000;
const INF: u32 = u32::MAX;


fn main() {
    let mut c = [0; N];
    let mut g = [const { Vec::<usize>::new() }; N];
    let mut dp = [[INF; 2*D+1]; N];

    let mut io = IO::new();
    let (n, d): (usize, usize) = io.r2();
    for (i, x) in io.line().enumerate() {
        c[i] = x;
    }
    for _ in 0..n-1 {
        let (u, v): (usize, usize) = io.r2();
        g[u-1].push(v-1);
        g[v-1].push(u-1);
    }

    dfs(0, 0, &g, &c, &mut dp, d);
    println!("{}", dp[0][d]);
fn dfs(
        v: usize,
        p: usize,
        g: &[Vec<usize>; N],
        c: &[u32; N],
        dp: &mut [[u32; 2*D+1]; N],
        d: usize,
    ) {
        for &u in &g[v] {
            if u == p {
                continue;
            }
            dfs(u, v, g, c, dp, d);
        }
        if g[v].len() == 1 && p != v {
            for i in 0..d+1 {
                dp[v][i] = c[v];
            }
            for i in d+1..2*d+1 {
                dp[v][i] = 0;
            }
            return;
        }     
        
        let mut cost = c[v];
        for &u in &g[v] {
            if u == p {
                continue;
            }
            cost += dp[u][2*d];
        }
        dp[v][0] = cost;

        for i in 1..d+1 {
            let mut cost = 0;
            for &u in &g[v] {
                if u == p {
                    continue;
                }
                cost += dp[u][2*d-i];
            }
            dp[v][2*d-i+1] = cost;
            for &u in &g[v] {
                if u == p {
                    continue;
                }
                dp[v][i] = dp[v][i].min(cost - dp[u][2*d-i] + dp[u][i-1]);
            }
        }
        for i in 1..2*d+1 {
            dp[v][i] = dp[v][i].min(dp[v][i-1]);
        }
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
