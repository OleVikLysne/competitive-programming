use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};

const INF: i32 = 1 << 30;

fn lep(mask: u16, i: u8, g: &[Vec<u8>], mem: &mut [Vec<i32>], inf_visit: &mut Vec<(u16, u8)>) -> i32 {
    if mask & 1 << i != 0 {
        return 0
    }
    let mut best = 0;
    for u in &g[i as usize] {
        if mask & 1 << u != 0 {continue}
        best = best.max(villagers(mask, *u, g, mem, inf_visit));
    }
    best = best.max(villagers(mask, i, g, mem, inf_visit));
    best
}


fn villagers(mask: u16, i: u8, g: &[Vec<u8>], mem: &mut [Vec<i32>], inf_visit: &mut Vec<(u16, u8)>) -> i32 {
    if mem[mask as usize][i as usize] != -1 {
        return mem[mask as usize][i as usize]
    }
    mem[mask as usize][i as usize] = INF;
    let mut best = INF;
    for v in 0..g.len() {
        if mask & 1 << v != 0 {
            for u in &g[v] {
                if mask & 1 << u != 0 {continue}
                best = best.min(1 + lep((mask ^ (1 << v)) | (1 << u), i, g, mem, inf_visit));
            }
        }
    }
    if best == INF {
        inf_visit.push((mask, i));
    }
    mem[mask as usize][i as usize] = best;
    best
}

fn main() {
    let mut io = IO::new();
    for c in 1..41 {
        let line: String = io.r();
        if line == "0" {break}
        let mut iter = line.split_ascii_whitespace();
        let v: usize = io.parse_next(&mut iter);
        let n: usize = io.parse_next(&mut iter);
        let mut e: usize = io.parse_next(&mut iter);

        let mut g: Vec<Vec<u8>> = vec![Vec::new(); n];
        while e > 0 {
            for elem in io.line::<String>() {
                e -= 1;
                let mut iter = elem.chars();
                let a = iter.next().unwrap() as u8 - b'A';
                let b = iter.next().unwrap() as u8 - b'A';
                g[a as usize].push(b);
                g[b as usize].push(a);
            }
        }
        let mut best = INF;
        let mut combinations = Vec::new();
        combs(n, v, &mut combinations, &mut vec![false; 1 << n], 0, 0);
        let mut mem = vec![vec![-1; n]; 1 << n];
        let mut inf_visit = Vec::new();
        for mask in combinations {
            let mut temp = 1;
            for i in 0..n {
                if mask & 1 << i != 0 {continue}
                temp = temp.max(villagers(mask, i as u8, &g, &mut mem, &mut inf_visit));
                for (m, j) in inf_visit.iter() {
                    mem[*m as usize][*j as usize] = -1;
                }
                inf_visit.clear();
            }
            best = best.min(temp);
        }
        if best != INF {
            println!("CASE {}: {}", c, best)
        } else {
            println!("CASE {}: {}", c, "NEVER")
        }
    }
}


fn combs(n: usize, v: usize, res: &mut Vec<u16>, visited: &mut Vec<bool>, mask: u16, c: u8) {
    if visited[mask as usize] {return}
    visited[mask as usize] = true;
    if c == v as u8 {
        res.push(mask);
        return
    }
    for i in 0..n {
        if mask & 1 << i == 0 {
            combs(n, v, res, visited, mask | 1 << i, c+1);
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
