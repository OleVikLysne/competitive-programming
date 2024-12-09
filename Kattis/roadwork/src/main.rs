use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};
use std::collections::HashMap;

fn main() {
    let mut io = IO::new();
    let (time, n) = io.r2();
    let mut w = Vec::new();
    let mut e = Vec::new();
    for _ in 0..n {
        let (d, a, r): (char, i32, i32) = io.r3();
        if d == 'W' {
            w.push((a, r))
        } else {
            e.push((a, r))
        }
    }
    let mut mem = HashMap::new();
    println!("{}", solve(0, [0, 0], 0, [&w, &e], &mut mem, time).min(solve(0, [0, 0], 1, [&w, &e], &mut mem, time)))
}

fn solve(t: i32, idxs: [usize; 2], o: usize, arrs: [&[(i32, i32)]; 2], mem: &mut HashMap<(i32, usize, usize), i32>, time: i32) -> i32 {
    let i = idxs[0];
    let j = idxs[1];
    if i == arrs[0].len() && j == arrs[1].len() {
        return 0
    }
    if let Some(x) = mem.get(&(t, i, j)) {
        return *x
    }

    let mut res = 1 << 30;
    for next_o in [0, 1] {
        if idxs[next_o] < arrs[next_o].len() {
            let (a, r) = arrs[next_o][idxs[next_o]];

            let new_t = {
                if next_o == o {a.max(t)}
                else           {a.max(t+time-3)}
            };

            let mut new_idxs = idxs.clone();
            new_idxs[next_o] += 1;
            let mut new_res = solve(new_t+3, new_idxs, next_o, arrs, mem, time);
            if new_t > a + r {
                new_res += 1;
            }
            res = res.min(new_res);
        }
    }
    mem.insert((t, i, j), res);
    return res
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
