use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

const INF: f64 = 100_000.0;
const N: usize = 18;

fn main() {
    let mut io = IO::new();
    let n: usize = io.r();
    let mut dist = [[0.0; N]; N];
    let mut points: [(f64, f64, f64); N] = [(0.0, 0.0, 0.0); N];
    for i in 0..n {
        let (x1, y1, z1) = io.r3();
        points[i] = (x1, y1, z1);
        for j in 0..i {
            let (x2, y2, z2) = points[j];
            dist[i][j] = ((x1-x2).powi(2) + (y1-y2).powi(2) + (z1-z2).powi(2)).sqrt();
            dist[j][i] = dist[i][j];
        }
    }

    let mut dp = [[[INF; 2]; N]; 1 << N];
    for i in 1..N {
        dp[1 << i][i][0] = dist[i][0];
    }

    for mask in 0..(1 << N) {
        for i in 0..N {
            if mask & 1 << i == 0 { continue }
            dp[mask][i][1] = dp[mask][i][1].min(dp[mask][i][0]);
            for j in 0..N {
                if mask & 1 << j != 0 { continue }
                let nm = mask | (1 << j);
                dp[nm][j][0] = dp[nm][j][0].min(dp[mask][i][1] + dist[i][j]);
                dp[nm][j][1] = dp[nm][j][1].min(dp[mask][i][0]);
            }
        }
    }
    println!("{}", dp[(1 << n) - 1][0][1]);
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