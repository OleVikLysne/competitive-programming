use std::collections::HashSet;
use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

const INF: i32 = 1 << 30;

fn main() {
    let mut io = IO::new();
    let (n, x, y): (usize, i32, i32) = io.r3();
    let (r, j): (i32, i32) = io.r2();
    let scale = r*j;
    let x = x * scale;
    let y = y * scale;

    let mut stations = HashSet::new();
    stations.insert(42_195 * scale);
    stations.insert(0);
    for _ in 0..n {
        stations.insert(io.r::<i32>()*scale);
    }
    let mut stations: Vec<i32> = stations.into_iter().collect();
    stations.sort_unstable();
    let n = stations.len();
    
    let mut dp = vec![INF; n];
    dp[0] = 0;
    let mut idx = 0;
    for i in 0..n-1 {
        while idx < n-1 && stations[idx] - stations[i] <= x {
            idx += 1;
        }
        for k in [idx-1, idx, n-1] {
            let d = stations[k] - stations[i];
            let run_d = d.min(x);
            let jog_d = d - run_d;
            let next_t = dp[i] + jog_d / j + run_d / r + y;
            dp[k] = dp[k].min(next_t);
        }
    }
    let res = (dp[n-1] - y) / scale;
    let h = res / 3600;
    let s = res % 3600;
    let m = s / 60;
    let s = s % 60;
    println!("{:02}:{:02}:{:02}", h, m, s);
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