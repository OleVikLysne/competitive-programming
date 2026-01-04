use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

const INF: i32 = 1 << 30;

#[allow(non_snake_case)]
fn main() {
    let mut io = IO::new();
    let mut prize: Vec<i32> = Vec::new();
    let mut time: Vec<i32> = Vec::new();
    let mut deadline = Vec::new();
    let (n, T) = io.r2();
    for _ in 0..n {
        let (p, t, mut d) = io.r3();
        if d == -1 {
            d = INF;
        }
        prize.push(p);
        time.push(t);
        deadline.push(d);
    }
    let mut dist: Vec<Vec<i32>> = Vec::new();
    for _ in 0..n+2 {
        dist.push(io.vec::<i32>());
    }

    let bits = bits_table(n);

    let mut dp = vec![vec![INF; 1 << 20]; 20];
    for i in 0..n {
        if check(0, n, i, &dist, T, &deadline, &time) {
            dp[i][1<<i] = dist[n][i] + time[i];
        }
    }
    let mut best = (0, 0);
    for i in 1..n {
        for mask in bits[i-1].iter().map(|x| *x as usize) {
            for j in 0..n {
                let t = dp[j][mask];
                if t == INF {
                    continue
                }
                let mut tot = 0;
                for k in 0..n {
                    if mask & 1 << k != 0 {
                        tot += prize[k];
                        continue
                    }
                    if !check(t, j, k, &dist, T, &deadline, &time) {
                        continue
                    }
                    let new_mask = mask | 1 << k;
                    let new_t = t + dist[j][k] + time[k];
                    dp[k][new_mask] = new_t.min(dp[k][new_mask]);
                }
                best = best.max((tot, -(mask as i32)));
            }
        }
    }
    for i in 0..n {
        if dp[i][(1 << n)-1] != INF {
            best = (prize.iter().sum(), -((1 << n) - 1));
            break
        }
    }
    let total = best.0;
    let mask = -best.1;
    println!("{}", total);
    for i in 0..n {
        if mask & 1 << i != 0 {
            print!("{} ", i+1);
        }
    }

}


fn bits_table(n: usize) -> Vec<Vec<i32>> {
    let mut res: Vec<Vec<i32>> = vec![Vec::new(); n];
    for i in 1..(1<<n) as i32 {
        res[i.count_ones() as usize-1].push(i);
    }
    res
}

#[allow(non_snake_case)]
fn check(t: i32, i: usize, j: usize, dist: &Vec<Vec<i32>>, T: i32, deadline: &[i32], time: &[i32]) -> bool {
    if t + dist[i][j] + time[j] > deadline[j] {
        return false
    }
     if t + dist[i][j] + time[j] + dist[j][dist.len()-1] > T {
        return false
     }
     true
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

    fn linenl<T: FromStr>(&mut self, n: usize) -> impl Iterator<Item = T> + '_ {
        return (0..n).map(|_| self.r());
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

    fn vecnl<T: FromStr>(&mut self, n: usize) -> Vec<T> {
        return self.linenl(n).collect();
    }

    fn print_vec<T: Display>(&self, vec: &[T]) {
        for x in vec {
            print!("{} ", *x);
        }
    }
}