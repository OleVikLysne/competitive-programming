use std::fmt::Display;
use std::io::Read;
use std::str::{Chars, FromStr, SplitAsciiWhitespace};
use std::collections::BinaryHeap;

const MAX: usize = 1<<19;
const MAXI: i32 = MAX as i32;
const BOUND: i32 = 200_000;

fn idx(v: i32) -> usize {
    return v.rem_euclid(MAXI) as usize
}

fn main() {
    let mut io = IO::new();
    let (n, t) = io.r2();
    let mut cheers = Vec::with_capacity(n+1);
    cheers.push((1, 1));
    for _ in 0..n {
        let (v, w) = io.r2();
        cheers.push((w, v));
    }
    let mut dist = [0; MAX];
    let mut prev_node = [i32::MAX; MAX];
    let mut prev_move = [u16::MAX; MAX];
    for i in 1..MAX {
        dist[i] = (i.min(MAX-i) + 1) as i32;
    }
    
    let mut pq = BinaryHeap::new();
    let mut indices: Vec<usize> = (0..n+1).collect();
    for i in (0..indices.len()).rev() {
        let k = indices[i];
        let (w, v) = cheers[k];
        let j = idx(v);
        if w < dist[j] {
            dist[j] = w;
            prev_node[j] = 0;
            prev_move[j] = i as u16;
            pq.push((-w, v));
        } else {
            indices.swap_remove(i);
        }
    }
    while let Some((d, v)) = pq.pop() {
        let d = -d;
        if dist[idx(v)] < d {
            continue
        }
        if v == t {
            let mut l = Vec::new();
            let mut v = v;
            while v != 0 {
                let j = idx(v);
                l.push(prev_move[j]+1);
                v = prev_node[j];
            }
            println!("{}", l.len());
            io.print_vec(&l);
            return
        }
        for i in (0..indices.len()).rev() {
            let k = indices[i];
            let (w, delta) = cheers[k];
            if dist[idx(delta)] < w {
                indices.swap_remove(i);
                continue
            }
            let u = v + delta;
            if u < -BOUND || u > BOUND {
                continue
            }
            let new_d = d + w;
            let j = idx(u);
            if new_d < dist[j] {
                dist[j] = new_d;
                prev_node[j] = v;
                prev_move[j] = k as u16;
                pq.push((-new_d, u));
            }
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